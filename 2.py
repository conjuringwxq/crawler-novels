from urllib import request, parse
from bs4 import BeautifulSoup
import re
import time


def search_book(book_name):
    url = 'https://www.biquge5200.cc/modules/article/search.php?searchkey=' + parse.quote(book_name)
    response = request.urlopen(url)
    content = response.read().decode('gbk')
    menu = []
    key = 0
    # 获取小说名称
    name = re.findall(r'<tr>.*?<a.*?>(.*?)</a>.*?</tr>', content, re.S | re.M)
    # 获取链接
    href = re.findall(r'<tr>.*?<a.*?href="(.*?)">.*?</a>.*?</tr>', content, re.S | re.M)
    # 获取作者
    allTd = re.findall(r'<tr>.*?<td class="odd">.*?</td>.*?</tr>', content, re.S | re.M)
    menu.append({'name': name, 'href': href})
    for line in allTd:
        arg = line.split('</td>')
        author = arg[2][22:]
        print(str(key) + '书名：' + name[key] + '>>作者：' + author)
        key += 1

    if menu:
        select_key = -1
        while select_key >= key or select_key < 0:
            select_key = int(input('请输入你要下载的小说序号：'))
        return menu[int(select_key)]
    return []


# def main():
#     book_name = input('请输入小说名字:')
#     search_book(book_name)
#     key += 1
#     soup = BeautifulSoup(content, 'html.parser')
#     print()


if __name__ == '__main__':
    info = []
    while not info:
        book_name = input('请输入你要查找的小说名: ')
        info = search_book(book_name)



