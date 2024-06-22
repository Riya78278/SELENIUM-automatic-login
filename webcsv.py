from bs4 import BeautifulSoup as soup
import requests
import csv
source=requests.get("https://myaccount.google.com/u/1/personal-info?hl=en&utm_source=OGB&utm_medium=act")
webpage=soup(source.content,features="html.parser")
print(webpage.prettify())
basicinfo=[]
for i in webpage.find_all(class_="Voxjqf"):
    string=i.p.text
    basicinfo.append(string.strip())

filename='file.csv'
with open(filename,"w",encoding="utf-8")as f:
    f.write=csv.writer(f)
    f.write.writerow(['No.','basicinfo'])
    for i in range(len(basicinfo)):
        f.write.writerow([i+1,basicinfo[i]])


