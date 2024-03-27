from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

#Insert the URL when prompted in terminal window

#This code will serve as the answer for both the programming assignment.

url = input("Enter URL - https://www.py4e.com/code3/urllinks.py?PHPSESSID=c5944f202bbf3829f3f6c49af05bd62f")


pos = int(input("Enter the position -http://py4e-data.dr-chuck.net/known_by_Fikret.html ")) - 1
count = int(input("Enter the count - http://py4e-data.dr-chuck.net/known_by_Fikret.html"))
count1 = 0
while(count1 < count):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0
for value in tags:
    temp = int(value.contents[0])
    sum = sum + temp
print(sum)
