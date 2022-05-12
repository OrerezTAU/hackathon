import monday
from monday import MondayClient
import requests
from bs4 import BeautifulSoup
import re
# from readData import cleanhtml
import readData


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

req = requests.get("https://www.ims.tau.ac.il/Tal/Syllabus/Syllabus_L.aspx?course=0366110101&year=2020", headers=headers, verify=False)

soup = BeautifulSoup(req.content, "html.parser")

dic_course_data={}
get_course_all_data = soup.find("div", {"id": "div_data"})

# def get_proff_name(dic):
#     get_name = get_course_all_data.find("div", {"class": "data-table-row course-proff-names"})
#     get_all_param = (get_name.findAll("div", {"class": "data-table-cell"}))
#     for i in range(len(get_all_param)):
#         val = (readData.cleanhtml(get_all_param[i].find("small", {"class": "data-table-cell-label"})))
#         type = readData.cleanhtml(get_all_param[i].find("span"))
#         dic[val] = type


def get_course_name(dic):
    get_name = get_course_all_data.find("div", {"class": "data-table-row course-name-number"})
    get_all_param = (get_name.findAll("div", {"class": "data-table-cell"}))
    for i in range(len(get_all_param)):
        val = (readData.cleanhtml(get_all_param[i].find("small", {"class": "data-table-cell-label"})))
        type = readData.cleanhtml(get_all_param[i].find("span"))
        dic[val] = type

def get_course_data(dic):
    get_course_time_location = get_course_all_data.find("div", {"class": "data-table-row course-time-location"})
    get_all_param = (get_course_time_location.findAll("div", {"class": "data-table-cell"}))
    for i in range(len(get_all_param)):
        val = (readData.cleanhtml(get_all_param[i].find("small", {"class": "data-table-cell-label"})))
        type = readData.cleanhtml(get_all_param[i].find("span"))
        dic[val] = type
    return dic

get_course_name(dic_course_data)
# get_proff_name(dic_course_data)
print(get_course_data(dic_course_data))
# print(dic_course_data)