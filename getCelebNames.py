import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://www.celebritytweet.com/"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
celebs = soup.find("div", {"class":"userNavigation"})

for anchor in celebs.findAll('a',href=True):
    print anchor['href'].strip('/')


