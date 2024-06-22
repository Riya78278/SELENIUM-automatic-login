from bs4 import BeautifulSoup
import requests
url="https://myaccount.google.com/u/1/personal-info?hl=en&utm_source=OGB&utm_medium=act"
def get_data(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lmxl")
    info=soup.find_all("name","birthday","gender",class="Voxjqf")
    data=p[]
                                   
            