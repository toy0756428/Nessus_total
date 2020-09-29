#encoding:UTF-8
import os
import urllib.request
from bs4 import BeautifulSoup

b = 0
j = 0
o = 0
p = 0
count = 0
os.listdir(r'C:\Users')
for url in os.listdir(r'C:\Users'):
    domain = os.path.abspath(r'C:\Users')
    url = os.path.join("file:///" + domain, url)
    #url = "file:///C:/Users"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data,"html.parser")

    ip = soup.find_all(style="margin: 0 0 10px 0; color: #000000;")
    for number in ip:
        count += 1
        #print(number.string)

    critical = soup.find_all(class_= '#d43f3a')
    a = 0
    for c in critical:
        a += int(c.string)
    #print(a)
    b += a

    high = soup.find_all(class_='#ee9336')
    i = 0
    for h in high:
        i += int(h.string)
    #print(i)
    j += i

    medium = soup.find_all(class_='#fdc431')
    n = 0
    for m in medium:
        n += int(m.string)
    #print(n)
    o += n

    low = soup.find_all(class_='#3fae49')
    k = 0
    for l in low:
        k += int(l.string)
    #print(k)
    p += k

print("Critical：" + str(b))
print("High：" + str(j))
print("Medium：" + str(o))
print("Low：" + str(p))
print("IP_Count：" + str(count))