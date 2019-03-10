import re
from urllib.request import urlopen
response = urlopen("http://www.sohu.com")
data = response.read()
data = data.decode("utf-8")
urls = re.findall(r'<a.*?href="(.+?)".*?</a>', data.replace(' ', ''), re.I)
urls = str(urls)
with open('b.txt', 'w', encoding='utf-8') as file:
    file.write(urls)
