import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

UNIVERSITY_OF_WATERLOO_COURSE_INDEX = 'https://ugradcalendar.uwaterloo.ca/page/Course-Descriptions-Index'


courses_map = {}


def extract_course_code(str):
    return ' '.join(str.split(' ')[:2])


def populate_courses_from(dest):
    res = requests.get('https://ugradcalendar.uwaterloo.ca' + dest)
    soup = BeautifulSoup(res.text, features='html.parser')
    course_list = soup.select('center table')
    for course in course_list:
        courses_map[extract_course_code(course.tr.b.text)] = course.tr.next_sibling.b.text


def traverse_html():
    res = requests.get(UNIVERSITY_OF_WATERLOO_COURSE_INDEX)
    soup = BeautifulSoup(res.text, features='html.parser')
    links = soup.find_all('a')
    for link in tqdm(links):
        try:
            dest = link['href']
            if dest.find('/courses') == 0:
                populate_courses_from(dest)
        except:
            pass


traverse_html()
for key, val in courses_map.items():
    print(f'{key} - {val}')

