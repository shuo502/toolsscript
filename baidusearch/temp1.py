import requests
key="新消息"
url="http://www.baidu.com/s?wd=%s&pn=20" %str(key)
# url="http://www.baidu.com/link?url=XyQ1B9ZzFGlrL5WRblmecfkpb3TkslEIN7wgyCsNT_o-SRhy8uAL4cDzXzyNd-E-n_q3gBMPnhlqJinNi98S34gzw3RXHP324aMAmeW6bBToaDj_A_DtETiYXLMh2Cr5"
k=requests.get(url)
# print(k.url)# url 地址
# print(k.text) # crontor
# print(k)
#nums_text
import reh
try:
    r=requests.get(url).content.decode("utf-8")
except:
    r=requests.get(url).content.decode("gbk")
    # r=requests.get(url).content
import re

# print(x[2][:x[2].find('div id="rs">')])

xs = re.compile('<table cellpadding(.*?)</table>')  # js
findallkey = re.compile('百度为您找到相关结果约(.*?)个', re.I)  # js
print("总计内容有：",findallkey.findall(r))
# x=r.split('class="cr-content "')
# print(len(x))
# print(r)
k=xs.findall(r)[0]
# print(k)
sotherkey=re.compile("<th><a .*?>(.*?)</a></th>")
print("相关：",sotherkey.findall(k))
contentall=re.compile('</a></h3><div .*?">(.*?)</div><div class="f13">.*?decoration:none;">(.*?)</a>.*?"title":"(.*?)","url":"(.*?)"')
# print(x[2])

s=contentall.findall(r)
print("keycontent:",s)
for i in s:

    print("key content: %s"%reh.filter_tags(i[0]))
    print("display url: %s" %reh.filter_tags(i[1]))
    print("key title: %s" %reh.filter_tags(i[2]))
    print("key link url: %s" %reh.filter_tags(i[3]))
# skey = re.compile('<title>(.*?)_百度搜索</title>', re.I)  # js