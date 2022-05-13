import monday
from monday import MondayClient
import requests
from bs4 import BeautifulSoup
import re
import Course

import getDataForCourse
import getDataForCourse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}


URL_list =[("https://exact-sciences.tau.ac.il/yedion/shar_ruach", "node-12227"), \
           ("https://exact-sciences.tau.ac.il/yedion/computer_courses", "node-12150"), \
           ("https://engineering.tau.ac.il/yedion/2020-21/9_7441", "node-7441"), \
           ("https://lifesci.tau.ac.il/yedion/ba-courses-list", "node-4621"), \
           ("https://social-sciences.tau.ac.il/yedion/2020-21/klalfaculty", "node-9045")]


#("https://exact-sciences.tau.ac.il/yedion/math_single_major", "node-12020")


def convert_str(string):
    li = list(string.split(" "))
    return li


def cleanhtml(text):
    text = str(text)
    new_str = ""
    flag = False
    for char in text:
        if char == '<' or char == '\n':
            flag = True
            continue
        if char == '>':
            flag = False
            # new_str += "\n"
            continue
        if not flag:
            new_str += char
    return new_str


def createURL(course_id):

    # if len > standard
    course_s = "0"+str(course_id)+"01"
    if len(course_s) == 10:
        return "https://www.ims.tau.ac.il/Tal/Syllabus/Syllabus_L.aspx?course="\
            + course_s + "&year=2021"
    else:
        return "1"


def getIDS(site_inst):
    req = requests.get(site_inst[0], headers=headers)

    soup = BeautifulSoup(req.content, "html.parser")

    res = soup.find("div", {"id": site_inst[1]})

    ids_dirty = cleanhtml(str(res))
    dirty_list = convert_str(ids_dirty)
    list_result = []

    for id_str in dirty_list:
        tmp = ""
        id_val = 0
        for char in id_str:
            if 57 >= ord(char) >= 48:
                tmp += char
        if tmp != '' and int(tmp) > 10000:
            if len(tmp) > 8:
                tmp = tmp[2:]
            if len(tmp) != 8:
                continue
            list_result.append(int(tmp))
    return list_result[2:]


def getAllIds(Ulist):
    all_ids = []
    for URL in Ulist:
        if URL != '1':
            all_ids.append(getIDS(URL))
    return all_ids


def get_courses_dict():
    dic_course_data={}

    g_list = getAllIds(URL_list)

    for i in range(len(g_list)):
        for j in range(len(g_list[i])):
            url_of_course = (createURL(g_list[i][j]))
            tmp_dic = {}
            if url_of_course != '1' and url_of_course != "https://www.ims.tau.ac.il/Tal/Syllabus/Syllabus_L.aspx?course=0368331101&year=2021":

                try:
                    getDataForCourse.get_course_name(tmp_dic, url_of_course)
                    getDataForCourse.get_course_data(tmp_dic, url_of_course)
                    getDataForCourse.get_proff_name(tmp_dic, url_of_course)
                except:
                    continue
                    # new_url = url_of_course[:78]
                    # new_url += "2020"
                    # getDataForCourse.get_course_name(dic_course_data, new_url)
                    # getDataForCourse.get_course_data(dic_course_data, new_url)
                    # getDataForCourse.get_proff_name(dic_course_data, new_url)
                dic_course_data[g_list[i][j]] = tmp_dic

                continue
    return dic_course_data
    #     req = requests.get(createURL(g_list[0][i]), headers=headers)
    #
    #     soup = BeautifulSoup(req.content, "html.parser")
    #
    #     print(soup.prettify())
