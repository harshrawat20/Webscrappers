import requests
from bs4 import BeautifulSoup
username1=input("Enter username \n")
url=f"https://github.com/{username1}"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
name=soup.find(itemprop="name").text.strip()
print(f"Name:{name}")
username=soup.find(itemprop="additionalName").text.strip()
print(f"Username:{username}")
details=soup.find(class_="flex-order-1 flex-md-order-none mt-2 mt-md-0").find_all("span")
print(f"followers :{details[0].text}")
print(f"following :{details[1].text}")
print(f"Stars :{details[2].text}")
