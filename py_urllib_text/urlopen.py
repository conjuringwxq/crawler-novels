from urllib import request

if __name__ == '__main__':
    url = "http://stock.eastmoney.com/news/1407,20170807763593890.html"
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)

    # format:格式化输出字符串
    # geturl:   返回请求的url
    print("URL: {0}".format(rsp.geturl()))
    # info:     返回元信息
    print("Info: {0}".format(rsp.info()))
    # getcode:  返回浏览器状态码
    print("Code: {0}".format(rsp.getcode()))
    html = rsp.read()
    html = html.decode()

