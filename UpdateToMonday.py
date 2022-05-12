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

def errors_found(nested_dict):
    if 'errors' in nested_dict.keys():
        print(nested_dict['errors'])
        return True
    if 'error_code' in nested_dict.keys():
        print(nested_dict['error_code'])
        return True
    return False


'''
Adds a new group to board and returns its id.
:param group_name str: the name of the group to add
:returns str new_group_id: the id of the new group'''


def add_group_to_board(group_name):
    nested_dict = monday_client.groups.create_group(my_board_id, group_name)
    if errors_found(nested_dict):
        return
    new_group_id = nested_dict['data']['create_group']['id']
    return new_group_id


'''
Adds a new item to a specific group in the board and returns its id.
:param group_id str: the id of the group to add
:returns str item_id: the id of the new item'''


def add_item_to_group(group_id, dic):
    col_val = {
        "dropdown6": 'faculty',
        "text_2": dic['שם הקורס'],
        "text3": 'professor',
        "status5": 'final_assignment',
    }
    if 'מטלה סופית' not in dict(dic).keys():
        col_val['date'] = '2000-01-01'
    else:
        col_val['date'] = dic['מטלות סופית']
    nested_dict = monday_client.items.create_item(board_id=my_board_id, group_id=group_id, item_name=dic['מספר קורס'],
                                                  column_values=col_val,
                                                  create_labels_if_missing=True)
    if errors_found(nested_dict):
        return
    new_item_id = nested_dict['data']['create_item']['id']
    return new_item_id


'''
Updates the value of item with given id if exists
:param item_id str: the id of the item to change
:param column_id str: the id of the column where we want to change
:param value: the new value which we want to set
'''


def update_item(item_id, column_id, value):
    nested_dict = monday_client.items.change_item_value(board_id=my_board_id, item_id=item_id, column_id=column_id,
                                                        value=value)
    errors_found(nested_dict)


'''
deletes the group with given id if exists
:param group_to_delete_id str: the id of the group to delete
'''


def delete_group(group_to_delete_id):
    nested_dict = monday_client.groups.delete_group(board_id=my_board_id, group_id=group_to_delete_id)
    errors_found(nested_dict)


# Returns id of the first group with given name, if no such group exists, return none
def get_group_id_by_name(group_name):
    basic_jason = monday_client.groups.get_groups_by_board(board_ids=[my_board_id])
    dict1 = dict(basic_jason)
    if errors_found(dict1):
        return
    dict2 = dict1.get('data')
    lst = dict2.get('boards')
    dict3 = lst[0]
    lst_of_groups = dict3.get('groups')
    for i in range(len(lst_of_groups)):
        group_dict = (dict)(lst_of_groups[i])
        if (str)(group_dict.get('title')) == group_name:
            return group_dict.get('id')
    return None


'''Adds a new column to the board and returns its id.
:param col_name str: the name of the column to add
:param col_type str: the type of the column, to see legal types access monday api
:returns str new_column_id: the id of the new column'''


def add_column(col_name, col_type):
    query = 'mutation{create_column(board_id: 2663503698, title:' + col_name + ', column_type:' + col_type + ') {id title description}}'
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    nested_dict = r.json()
    new_col_id = nested_dict['data']['create_column']['id']
    return new_col_id


def delete_item(item_id):
    nested_dict = monday_client.items.delete_item_by_id(item_id=item_id)
    errors_found(nested_dict)
