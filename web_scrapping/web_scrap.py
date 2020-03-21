_author_ = "aman"
import requests
from bs4 import BeautifulSoup

URL = "https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22general%20physician%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=qwe"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

dr_tags  = soup.findAll('h2')
doc_list = []
for name in dr_tags:
    name_str = str(name)
    end_index = name_str.find("</h2>")
    st_index = name_str.find(">Dr.")
    doc_list.append(name_str[st_index:end_index].replace(">",""))
doc_count = len(doc_list)
doc_names = ",".join(doc_list)
print(doc_names)
print(doc_count)

