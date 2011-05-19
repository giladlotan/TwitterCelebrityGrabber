import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://www.celebritytweet.com/"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
celebs = soup.find("div", {"class":"userNavigation"})

f = open('celebs.txt','w')

for anchor in celebs.findAll('a',href=True):
    a = anchor['href'].strip('/')
    f.write(a)
    f.write('\n')

f.close()
