import monday
from monday import MondayClient
import requests
from bs4 import BeautifulSoup
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}


URL_list =[("https://exact-sciences.tau.ac.il/yedion/shar_ruach", "node-12227"), \
           ("https://exact-sciences.tau.ac.il/yedion/computer_courses", "node-12150"), \
           ("https://exact-sciences.tau.ac.il/yedion/math_single_major", "node-12020")]


def convert_str(string):
    li = list(string.split(" "))
    return li


def cleanhtml(text):
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
    return "https://www.ims.tau.ac.il/Tal/Syllabus/Syllabus_L.aspx?course="+course_id+"01&year=2021"


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
            list_result.append(int(tmp))
    return list_result[2:]


def getAllIds(Ulist):
    all_ids = []
    for URL in Ulist:
        all_ids.append(getIDS(URL))
    return all_ids


print(getAllIds(URL_list))

