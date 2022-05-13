
import readData
import UpdateToMonday as monday_update
import extract_TAUfactor

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
    #monday_update.add_item_to_group(monday_update.get_group_id_by_name('Exact Sciences Courses'),'0368-4086-01','מדעי המחשב', '0368-4086-01', 'נושאים מתקדמים בלמידה חישובית ואופטימיזציה','דר תומר קורן','אחר')

    dict_av = extract_TAUfactor.return_dict()
    dict = readData.get_courses_dict()
    monday_update.push_all_items(dict)


# file_name = "courses.json"
# file_dict = json.loads(file_name)
# for course in file_dict:
#     course_type = course["type"]
#     faculty = course["faculty"]
#     course_num = course["course_number"]
#     course_name = course["course_name"]
#     proff = course["professor"]
#     exam_essay = course["exam_essay"]
#     exam_date = course["exam_date"]
#     nakaz = course["nakaz"]
#     Course = course(course_type,faculty,course_num,course_name,proff,exam_essay,exam_date,nakaz)



e


