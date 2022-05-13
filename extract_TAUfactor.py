import json
import requests
import urllib
import readData


def create_dict(curses):
    course_dict1 = {}
    for course in curses:
        course_str = course[:4] + "-" + course[4:]
        course_dict1[course_str] = ""
    return course_dict1


def return_dict():
    URL = "https://www.tau-factor.com/api/v1/courses/?course_code="
    course_dict = create_dict(readData.nadavwrap())
    for course in course_dict.keys():
        if course[1] == '3':
            URL += str(course)
            response = urllib.request.urlopen(URL)
            try:
                data = json.loads(response.read())
                course_dict[course] = data["results"][0]["instances"][0]["statistics"]["mean"]
            except:
                continue
            URL = str("https://www.tau-factor.com/api/v1/courses/?course_code=")
    return course_dict
