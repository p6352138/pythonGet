from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.taptap.com/top/download')

bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find_all("div","taptap-top-card")

for text in text_list:
    print(text.get_text())

html.close()