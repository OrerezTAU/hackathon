import monday
from monday import MondayClient
import requests
from bs4 import BeautifulSoup
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

req = requests.get("https://www.ims.tau.ac.il/Tal/Syllabus/Syllabus_L.aspx?course=0366110101&year=2020", headers=headers)

soup = BeautifulSoup(req.content, "html.parser")

res = soup.find("div", {"id" : "div_dataToc"})

res2 = soup.find('p').get_text()
# for tag in soup.findAll('p'):
#     print(tag.get_text())


#cleantext = BeautifulSoup(res, "lxml").text

def cleanhtml(text):
    new_str = ""
    flag = False
    for char in str(res):
        if char == '<':
            flag = True
            continue
        if char == '>':
            flag = False
            new_str += "\n"
            continue
        if not flag:
            new_str += char
    return new_str


print(cleanhtml(res))