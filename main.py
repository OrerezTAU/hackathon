import monday.query_joins
import requests
import json

from monday import MondayClient

apiKey = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE1OTY0Njg5NSwidWlkIjozMDE2NzQ2MywiaWFkIjoiMjAyMi0wNS0wOVQxODoyMTozMS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTE4NzU5MjIsInJnbiI6InVzZTEifQ.udfx4p8dqK-8wlbhOKRmHNp__YYuOMrVkI5ZWvOwqSo'
headers = {"Authorization": apiKey}
my_board_id = 2663503698
apiUrl = "https://api.monday.com/v2"
monday_client = MondayClient(apiKey)


# def initiate_board_id():
#     board = monday_client.boards.fetch_boards()
#     dict1 = dict(board)
#     dict2 = dict1.get('data')
#     lst = dict2.get('boards')
#     dict3 = lst[0]
#     global my_board_id
#     my_board_id = dict3.get('id')


def add_group_to_board(group_name):
    new_group = monday_client.groups.create_group(my_board_id, group_name)
    dict1 = dict(new_group)
    dict2 = dict1.get('data')
    dict3 = dict2.get('create_group')
    new_group_id = dict3.get('id')
    return new_group_id


def add_item_to_group(group_id, item_name, faculty, course_num, course_name, professor, final_assignment, final_date):
    col_val = {
        "dropdown6": faculty,
        "text_1": course_num,
        "text_2": course_name,
        "text3": professor,
        "status5": final_assignment,
        "date": final_date}
    item = monday_client.items.create_item(board_id=my_board_id, group_id=group_id, item_name=item_name,
                                           column_values=col_val,
                                           create_labels_if_missing=True)
    dict1 = dict(item)
    dict2 = dict1.get('data')
    dict3 = dict2.get('create_item')
    new_item_id = dict3.get('id')
    return new_item_id


def update_item(item_id, column_id, value):
    monday_client.items.change_item_value(board_id=my_board_id, item_id=item_id, column_id=column_id, value=value)


def delete_group(group_to_delete_id):
    monday_client.groups.delete_group(board_id=my_board_id, group_id=group_to_delete_id)


# Returns id of the first group with given name, if no such group exists, return none
def get_group_id_by_name(group_name):
    basic_jason = monday_client.groups.get_groups_by_board(board_ids=[my_board_id])
    dict1 = dict(basic_jason)
    dict2 = dict1.get('data')
    lst = dict2.get('boards')
    dict3 = lst[0]
    lst_of_groups = dict3.get('groups')
    for i in range(len(lst_of_groups)):
        group_dict = (dict)(lst_of_groups[i])
        if (str)(group_dict.get('title')) == group_name:
            return group_dict.get('id')
    return None


def add_column(col_name, col_type):
    query = 'mutation{create_column(board_id: 2663503698, title:' + col_name +', column_type:'+col_type+') {id title description}}'
    print(query)
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    print(r.text)


if __name__ == '__main__':
    # group = add_group_to_board("Exact Sciences Courses")
    # item_id1 = add_item_to_group(group, "0368-1105-01", "מדעי המחשב", "0368-1105-01", "מבוא מורחב למדעי המחשב",
    #                              "דר אמיר רובינשטיין"
    #                              , "מבחן", "2021-01-01")
    #
    # item_id2 = add_item_to_group(group, "0366-2010-01", "מתמטיקה", "0366-2010-01", "מבוא להסתברות",
    #                              "דר בועז אברהם סלומקה"
    #                              , "מטלה", "2023-04-05")

    # group_id = get_group_id_by_name("Exact Sciences Courses")
    add_column("average", "numbers")
