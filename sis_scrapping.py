from bs4 import BeautifulSoup
import requests

def scraper(year, subject):
    link=f"https://sis.rpi.edu/rss/bwckctlg.p_display_courses?term_in={year}09&call_proc_in=&sel_subj=&sel_levl=&sel_schd=&sel_coll=&sel_divs=&sel_dept=&sel_attr=&sel_subj={subject}"
    s = requests.Session()
    webpage_response = s.get(link)
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    for row in soup.find_all('td'):
        #print(row)
        if row['class'] == ['nttitle']:
            name = row.a
            print(name.contents[0])

scraper(2023, "BIOL")