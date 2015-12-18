from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://google.com")
bsObj = BeautifulSoup(html.read())
print(bsObj.head)
