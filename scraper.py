from bs4 import BeautifulSoup as bs
import requests
import re

def getHeadline(targetURL): # gets headline of article
    somePage = requests.get(href)
    someSoup = bs(somePage.content, 'html.parser')
    cleanedHeadline = re.sub(' - BBC News', '', someSoup.find('title').string)
    return cleanedHeadline

url = "https://www.bbc.co.uk/news"
page = requests.get(url)
soup = bs(page.content, 'html.parser')

# GET ALL NEWS PAGE URLS & CORRESPONDING HEADLINE
newsLinks = {}
for link in soup.find_all(class_ = 'gs-c-promo-heading'):
    href = str(link.get('href'))
    if href != "None":
        if (href.startswith('https')) == False: # modify if not full url
            href = 'https://www.bbc.co.uk' + href
            if (href.startswith('https://www.bbc.co.uk/news/') == True):
                headline = getHeadline(href)
                newsLinks.update({href : headline})

print (newsLinks)
# TODO: remove duplicates from newsLinks dictionary

""" newsLinksDict = {}
for link in newsLinks:
    somePage = requests.get(link)
    someSoup = bs(somePage.content, 'html.parser')
    print (someSoup.find('title')) """