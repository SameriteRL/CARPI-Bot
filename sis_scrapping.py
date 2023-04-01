from bs4 import BeautifulSoup
import requests

class Course:
    def __init__(self, name):
        self.name = name
        
    def desc(self, desc):
        self.description = desc

def scraper(year, subject):
    link=f"https://sis.rpi.edu/rss/bwckctlg.p_display_courses?term_in={year}09&call_proc_in=&sel_subj=&sel_levl=&sel_schd=&sel_coll=&sel_divs=&sel_dept=&sel_attr=&sel_subj={subject}"
    s = requests.Session()
    webpage_response = s.get(link)
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    courses = []
    x = -1
    for row in soup.find('table', {"class": "datadisplaytable"}).find_all('td'):
        #print(row)
        if row['class'] == ['nttitle']:
            name = row.a
            c = Course(name.contents[0])
            courses.append(c)
            x += 1
            #print(name.contents[0])
        if row['class'] == ['ntdefault']:
            if (x > -1):
                print(x)
                print(row.contents[0])
                courses[x].desc(row.contents[0])
                print("=======")
                print(list(row.children))
                print("=======")
                break
        
    y = 0
    # for course in courses:
    #     if ((course.description and course.description.strip())):
    #         print(course.name)
    #         print(course.description)
    #     else:
    #         print(f"{course.name} is empty")
    #         y+=1

    print(len(courses))
    print(f"{y} courses have no description")

def scraper2(year, subject):
    link=f"https://sis.rpi.edu/rss/bwckctlg.p_display_courses?term_in={year}09&call_proc_in=&sel_subj=&sel_levl=&sel_schd=&sel_coll=&sel_divs=&sel_dept=&sel_attr=&sel_subj={subject}"
    s = requests.Session()
    webpage_response = s.get(link)
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    courses = []
    
    row = soup.find('table', {"class": "datadisplaytable"}).find_all('td', {"class": "ntdefault"})
    print(row[0].contents[0])


scraper(2023, "BIOL")