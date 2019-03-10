import re
import time
from urllib import request, parse


# 搜索小说名字
def search_book(bookname):
    url = 'https://www.biquge5200.cc/modules/article/search.php?searchkey=' + parse.quote(bookname)
    response = request.urlopen(url)
    content = response.read().decode('gbk')
    menu = []
    key = 0
    # 获取小说名称
    name = re.findall(r'<tr>.*?<a.*?>(.*?)</a>.*?</tr>', content, re.S | re.M)
    # 获取链接
    href = re.findall(r'<tr>.*?<a.*?href="(.*?)">.*?</a>.*?</tr>', content, re.S | re.M)
    # 获取作者
    author = re.findall(r'<tr>.*?<td class="odd"><a.*?</a></td>.*?<td class="odd">(.*?)</td>', content, re.S | re.M)

    for line in author:
        print(str(key) + '书名：' + name[key] + '>>作者：' + line)
        menu.append({'name': name[key], 'href': href[key]})
        key += 1
    if menu:
        select_key = -1
        while int(select_key) >= key or int(select_key) < 0:
            select_key = int(input('请输入你要下载的小说序号：'))
        return menu[int(select_key)]
    return []


# 获取小说目录
def get_novel_menu(url):
    response = request.urlopen(url)
    content = response.read().decode('gbk')
    noveList = []
    # 小说章节标题
    title = re.findall(r'<dd>.*?<a href=".*?">(.*?)</a>.*?</dd>', content, re.S | re.M)
    # 小说章节链接
    href = re.findall(r'<dd>.*?<a href="(.*?)">.*?</dd>', content, re.S | re.M)
    k = 0
    for i in title:
        noveList.append({'title': title[k], 'href': href[k]})
        k += 1
    return noveList


# 获取小说内容
def get_novel_content(title, url):
    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    response = request.urlopen(request.Request(url, headers=headers))
    content = response.read().decode('gbk')
    # 小说内容
    text = re.findall(r'<div id="content".*?>(.*?)</div>', content, re.S | re.M)
    return str(title) + '\r\n' + str(text)


# if __name__ == '__main__':
info = []
while not info:
    book_name = input('请输入你要查找的小说名: ')
    info = search_book(book_name)
# 获取小说目录链接
menu_lists = get_novel_menu(info['href'])
if not menu_lists:
    print('该小说没有下载的目录')
    exit(0)
# 下载小说目录中的具体内容
for i in menu_lists:
    print('正在下载：' + i['title'])
    content = get_novel_content(i['title'], i['href'])
    with open('syqn.txt', 'a') as f:
        f.write(content)
        f.close()

    time.sleep(0.1)
