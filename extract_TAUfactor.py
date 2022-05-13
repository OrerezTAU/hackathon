import json
import requests
import urllib
import readData

course_dict = {}
URL = "https://www.tau-factor.com/api/v1/courses/?course_code="


def create_dict(curses):
    course_dict1 = {}
    for course in curses:
        print(course)
        course_str = course[:4] + "-" + course[4:]
        course_dict1[course_str] = ""
    return course_dict1


course_dict = create_dict(readData.nadavwrap())

for course in course_dict.keys():
    URL += str(course)
    response = urllib.request.urlopen(URL)
    data = json.loads(response.read())
    course_dict[course] = data["results"][0]["instances"][0]["statistics"]["mean"]
    URL = str("https://www.tau-factor.com/api/v1/courses/?course_code=")

print(course_dict)