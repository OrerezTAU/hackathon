

import requests
from bs4 import BeautifulSoup
import re

import requests
from bs4 import BeautifulSoup
#import readData
# from readData import cleanhtml




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


def get_all_div(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.content, "html.parser")

    return soup.find("div", {"id": "div_data"})


def get_course_name(dic, url):
    get_name = get_all_div(url).find("div", {"class": "data-table-row course-name-number"})
    get_all_param = (get_name.findAll("div", {"class": "data-table-cell"}))
    for i in range(len(get_all_param)):
        val = (cleanhtml(get_all_param[i].find("small", {"class": "data-table-cell-label"})))
        type = cleanhtml(get_all_param[i].find("span"))
        dic[val] = type

def get_course_data(dic, url):
    get_course_time_location = get_all_div(url).find("div", {"class": "data-table-row course-time-location"})
    get_all_param = (get_course_time_location.findAll("div", {"class": "data-table-cell"}))
    for i in range(len(get_all_param)):
        val = (cleanhtml(get_all_param[i].find("small", {"class": "data-table-cell-label"})))
        type = cleanhtml(get_all_param[i].find("span"))
        dic[val] = type


def get_proff_name(dic,url):
    get_name = get_all_div(url).find("div", {"class": "data-table-row course-proff-names"})
    get_all_param = (get_name.findAll("div", {"class": "data-table-cell"}))
    for i in range(len(get_all_param)):
        val = (cleanhtml(get_all_param[i].find("small", {"class": "data-table-cell-label"})))
        type = cleanhtml(get_all_param[i].find("span"))
        dic[val] = type


dic_course_data={}
# get_course_name(dic_course_data)
print(get_proff_name(dic_course_data, "https://www.ims.tau.ac.il/Tal/Syllabus/Syllabus_L.aspx?course=0609120001&year=2021"))
# print(get_course_data(dic_course_data))
# print(dic_course_data)