from bs4 import BeautifulSoup as bs
import requests
import re

def getHeadline(targetURL): # gets headline of article
    somePage = requests.get(href)
    someSoup = bs(somePage.content, 'html.parser')
    cleanedHeadline = re.sub(' - BBC News', '', someSoup.find('title').string)
    return cleanedHeadline

def getArticle(targetURL):
    somePage = requests.get(href)
    someSoup = someSoup = bs(somePage.content, 'html.parser')
    # TODO: needs to also get titles from the article as well
    #articleContent = someSoup.find_all('')

def checkDuplicate(array3D, targetURL): # check for duplicate URL in 3d arra
    itemFound = False
    for array in array3D:
        if array[1] == targetURL:
            itemFound = True
    return itemFound             

url = "https://www.bbc.co.uk/news"
page = requests.get(url)
soup = bs(page.content, 'html.parser')

# GET ALL NEWS PAGE URLS & CORRESPONDING HEADLINE
newsLinks = [] # will be 3D array
for link in soup.find_all(class_ = 'gs-c-promo-heading'):
    href = str(link.get('href'))
    if href != "None":
        if (href.startswith('https')) == False: # modify if not full url
            href = 'https://www.bbc.co.uk' + href
            if (href.startswith('https://www.bbc.co.uk/news/') == True):
                headline = getHeadline(href)
                if checkDuplicate(newsLinks, href) == False:
                    tempArray = [headline, href]
                    newsLinks.append(tempArray)

# DISPLAY NEWS TO USER
print ("BBC News articles: \n")
counter = 0
for array in newsLinks:
    counter += 1
    print (str(counter) + ")", array[0])

while True:
    chosenValue = int(input("\nSelect an article number: "))
    articleName = newsLinks[chosenValue - 1][0]
    print ("Selected '" + articleName + "', Select an action from below:")
    chosenAction = int(input("1 to read article, 2 to save article, 3 to select a different article: "))
    if chosenAction == 1:
        pass
    else:
        print ("\n test")

# TODO: don't display articles that have only a video and no text