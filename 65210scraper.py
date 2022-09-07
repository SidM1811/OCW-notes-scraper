import requests
from bs4 import BeautifulSoup
import wget

URL = "https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2005/pages/lecture-notes/"
prefix = "https://ocw.mit.edu"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
soup.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))
results = soup.find_all("a")
links = []
for result in results:
    try:
        t = result["href"]
        links.append(t)
    except KeyError:
        pass
links = list(filter(lambda x:x.startswith('/courses/6-854j-advanced-algorithms-fall-2005/resources/n'),links))
for link in links:
    new_page = requests.get(prefix+link)
    new_soup = BeautifulSoup(new_page.content, "html.parser")
    new_soup.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))
    new_results = new_soup.find_all("a",class_="download-file")
    for new_result in new_results:
        try:
            print(prefix+new_result["href"])
            wget.download(prefix+new_result["href"])
        except KeyError:
            print(new_result)
        except Exception as e:
            print(e)