#coding=utf-8
import  requests
import re

def Get_icp(domian):
    # domian="sina.com"
    url="http://icp.chinaz.com/"+domian
    k=requests.get(url).content.decode()

    # # print(x.decode())
    a=re.compile("主办单位名称</span><p>(.*?)<")
    b=re.compile('主办单位性质</span><p><strong class="fl fwnone">(.*?)<')
    c=re.compile('网站备案/许可证号</span><p><font>(.*?)<')
    d=re.compile('网站名称</span><p>(.*?)<')
    e=re.compile('网站首页网址</span><p class="Wzno">(.*?)<')
    f=re.compile('审核时间</span><p>(.*?)<')
    print(a.findall(k))
    print(b.findall(k))
    print(c.findall(k))
    print(d.findall(k))
    print(e.findall(k))
    print(f.findall(k))

