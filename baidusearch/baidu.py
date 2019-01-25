import re


import re
from bs4 import BeautifulSoup
import requests

def get_html(url):
    print(url)
    try :
        rs = requests.get(url)
    except:
        try:
            rs = requests.get(url,allow_redirects=False)
        except:
            return
    try:
        print(rs.url)
        r = rs.content.decode("utf-8")
    except:
        print(rs.url)
        r = rs.content.decode("gbk")
    return r

def spider_baidu(key,pn=0,t=0):
    if key==None:return

    if "str" in str(type(key)):
        key = str(key)
        if t!=0:
            if pn<t:
                t_a=t
                t=pn
                pn=t_a
            urlall=[]
            for i in range(int(int(t / 10)), int(int(pn / 10))):
                url = "http://www.baidu.com/s?wd=%s&pn=%s " % (str(key), str(i*10))
                urlall.append(url)
        if pn==0:
            url = "http://www.baidu.com/s?wd=%s" % str(key)
            return get_html(url)
        else:
            url = "http://www.baidu.com/s?wd=%s&pn=%s " % (str(key),str(pn))
            return get_html(url)
            pass
        return
    for i in key:
        url=i
        # filter_baidu(get_html(url))
        return get_html(url)
    return

def bs4_filter_html(html):
    if html==None :return
    s = BeautifulSoup(html ,'html.parser')
    y = s.find_all(id="rs")  # 相关
    print(y[0].text)
    z = s.find_all(id="page")  # 分页
    print(z[0].text)
    x = s.find_all(class_='result c-container ')
    j=1
    arr=[]
    for i in x:
        print(j)
        j=j+1
        t = i.h3.text
        print(t)
        try:
            c = i.find_all(class_='c-abstract')[0].text
            print(c)
        except:
            pass
        try:
            tk = re.compile('target="_blank">(.*?)</a>.*?title":"(.*?)","url":"(.*?)".*?}" href="(.*?)"')
            arrinfo=tk.findall(str(i.find_all(class_='f13')))
            arr.append(arrinfo)
            print(arrinfo)
        except:
            pass
    return arr
def save_file(n,s,t='w'):
    if n==None and s==None:return

    file_name=str(n)+".txt"
    str_r=str(s)
    print(file_name)
    f=open(file_name, t,encoding='utf-8')
    f.write(str_r)
    f.close()
if __name__=="__main__":
    import time

    all=bs4_filter_html(spider_baidu("用户协议",90))
    for i in all:
        tr = re.compile("http?://|.*?\.(.*?)/")
        a = tr.findall(str(i[0][0]))[0]
        try:
            a=a+str(time.time()*1000)[5:13]
            x=BeautifulSoup(get_html(i[0][2]),'html.parser').body.text
            save_file(a,x)
        except:
            save_file("err", i[0][2],"a")
            pass
