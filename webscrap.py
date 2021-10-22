import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode= ssl.CERT_NONE
c=0
s=0

url=input("Enter-")
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,"html.parser")

tags=soup('span')
for tag in tags:
   y=int(tag.text)
   s=s+y
   c=c+1

print("Count",c)
print("Sum",s)
