import UpdateToMonday as monday_update

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
    dict = {'מספר קורס': '0366-1101-01', 'שם הקורס': 'חשבון דיפרנציאלי ואינטגרלי 1א', 'אופן ההוראה': 'שיעור', 'שעות סמסטריאליות': '4', 'סמסטר': 'א\' תשפ"א', 'יום': 'ג', 'שעות': '12:00-14:00', 'בניין': "צ'ק פוינט", 'חדר': '001'}
    #monday_update.add_item_to_group(monday_update.get_group_id_by_name('Exact Sciences Courses'),'0368-4086-01','מדעי המחשב', '0368-4086-01', 'נושאים מתקדמים בלמידה חישובית ואופטימיזציה','דר תומר קורן','אחר')
    monday_update.add_item_to_group(group_id=monday_update.get_group_id_by_name("Exact Sciences Courses"),dic=dict)


