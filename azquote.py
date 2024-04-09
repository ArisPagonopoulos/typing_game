import requests
import string
import re
import random
from typeit import typegame
import os
from bs4 import BeautifulSoup

#os.chdir("c:\\users\\aris\\mypythonscripts")
#parser=htmlparser.HTMLParser()
res=requests.get("https://www.azquotes.com/")
text=res.text
#finding all the authors	
authorlinks=re.findall("\/author\/(\d+\-\w+)",text)
#choosing one at random
author=random.choice(authorlinks)
site=requests.get("https://www.azquotes.com/author/"+author)
text=site.text
soup = BeautifulSoup(text, 'html.parser')
#fidning all of his/her quotes
quotes = [q.get_text() for q in soup.find_all("a",class_="title")]
#for i,q in enumerate(s):
#	s[i]=htmlparser.unescape(q)
#name of the author
author = re.sub("[\d]","",author).replace("-"," ").replace("_"," ")
#words per minute
wpm = typegame(random.choice(quotes), author)
print("Words per minute: {0:.2f}".format(wpm))