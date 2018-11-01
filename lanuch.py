from urllib.request import urlopen

html = urlopen('https://www.taptap.com/top/download')

bs_obj = BeautifulSoup(html.read(),'html.parser')

print(html.read())
html.close()