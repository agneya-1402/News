import requests
from bs4 import BeautifulSoup
import pyttsx3
voice=pyttsx3.init()
url = ("https://timesofindia.indiatimes.com/us")
page = requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
a=soup.find_all("figcaption")

#print("----------------News---------------")
b1=(a[0].get_text())
b2=(a[1].get_text())
b3=(a[2].get_text())
b4=(a[3].get_text())
b5=(a[4].get_text())
b6=(a[5].get_text())
b7=(a[6].get_text())
b8=(a[7].get_text())
b9=(a[8].get_text())
def news():
    print(b1)
    voice.say(b1)
    print(b2)
    voice.say(b2)
    print(b3)
    voice.say(b3)
    print(b4)
    voice.say(b4)
    print(b5)
    voice.say(b5)
    print(b6)
    voice.say(b6)
    print(b7)
    voice.say(b7)
    print(b8)
    voice.say(b8)
    print(b9)
    voice.say(b9)
    voice.runAndWait()

