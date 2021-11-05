from bs4 import BeautifulSoup as bs
import requests
#import re

url = "https://www.bbc.co.uk/news"
page = requests.get(url)
soup = bs(page.content, 'html.parser')

# GET ALL NEWS PAGE URLS
newsLinks = []
for link in soup.find_all(class_ = 'gs-c-promo-heading'):
    href = str(link.get('href'))
    if href != "None":
        if (href.startswith('https')) == False: # modify if not full url
            href = 'https://www.bbc.co.uk' + href
            if (href.startswith('https://www.bbc.co.uk/news/') == True):
                newsLinks.append(href)

# GET HEADLINES

