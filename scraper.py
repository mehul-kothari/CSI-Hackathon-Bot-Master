import requests
from bs4 import BeautifulSoup
import bs4
import re
filename = "rules.txt"
f = open(filename, "w")
start_url = "https://www.lords.org/mcc/laws-of-cricket/laws/"
r = requests.get(start_url)
bs = BeautifulSoup(r.text)
l = bs.findAll('a', attrs = {"class":"title link"})
l = [i.get('href') for i in l]
l = l[:-5]
for url in l:
    url = "https://www.lords.org" + url
    print(url)
    r = requests.get(url)
    bs = BeautifulSoup(r.text)
    b = bs.find('div', attrs={"class":"sixteen columns headerstrip"})
    s = b.contents[1].string.strip()
    f.write(s + "\n")
    a = bs.find('div', attrs={"class":"textcontent"})
    if a != None:
        for child in a.descendants:
            if type(child) is not bs4.element.Tag:
                s = child.string
                x = re.search("Marylebone Cricket Club 2013", s)
                if x != None:
                    break
                print("BEFORE: ", s, sep = '\n')
                s = s.strip()
                l = s.split()
                l = [i.strip() for i in l]
                s = ' '.join([i for i in l])
                print("AFTER: ", s, sep = '\n')
                f.write(s + "\n")
    f.write("\n\n\n\n\n")
