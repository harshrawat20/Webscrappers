import requests
from bs4 import BeautifulSoup
url="https://inshorts.com/en/read"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
cardstacks=soup.find_all('div',class_='news-card')

def write_into(row):
    with open('news_data.txt','a') as textFile:
        writer=txt.writer(textFile)
        writer.writerrow(row)
    textfile.close()

print("--------------------------NEW-----------------------------------------------------------------------------------")

for card in cardstacks:
    print("----TITLE:----")
    title=card.find('span',attrs={"itemprop": "headline"}).text
    print(title)

    print("----DATE:----")
    on=card.find('span',class_='date').text
    print(on)

    print("----DESCRIPTION:----")
    descrip=card.find('div',attrs={"itemprop": "articleBody"}).text
    print(descrip)

    print("----AUTHOR:----")
    author=card.find('span',class_='author').text
    print(author)

    print("----SOURCE----")
    read_more=card.find('a',class_='source')
    if read_more is None:
        link="Not Available"
        print(link)

    else:
        link=read_more.get('href')
        source=read_more.text
        print(source)
        print(link)
    print("\n")

    print("--------------------------NEW-----------------------------------------------------------------------------------")

print("TOtal News Showing:",len(cardstacks))

    

    