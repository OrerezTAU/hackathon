import monday
from monday import MondayClient
import requests
from bs4 import BeautifulSoup
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}


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


def getIDS():
    req = requests.get("https://exact-sciences.tau.ac.il/yedion/shar_ruach", headers=headers, verify=False)

    soup = BeautifulSoup(req.content, "html.parser")

    res = soup.find("div", {"id": "node-12227"})

    ids_dirty = cleanhtml(str(res))
    dirty_list = convert_str(ids_dirty)
    # print(dirty_list)
    list_result = []

    for id_str in ids_dirty:
        for char in id_str:
            if char :
                list_result.append(id_str)
    return list_result


# print(getIDS())


def getName(soup_res):
    pass


# for tag in soup.findAll('p'):
#     print(tag.get_text())


#cleantext = BeautifulSoup(res, "lxml").text




# print(cleanhtml(table_res))
