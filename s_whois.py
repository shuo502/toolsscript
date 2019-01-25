#coding=utf-8
from dwhois import whoiskey
# a=whoiskey("baidu.com")
# print(a)
import re


#
# print(a)
def s_whois(domain):
    a = whoiskey(domain)
    print(a)
    b=re.compile("Domain Name: (.*?)\n")
    c=re.compile("Registrar: (.*?)\n")
    d=re.compile("Creation Date: (.*?)\n")
    # e=re.compile("Updated Date: (.*?)\n")
    f=re.compile("Registry Expiry Date: (.*?)\n")
    g=re.compile("Name Server: (.*?)\n")
    if len(d.findall(a))==0 :d=re.compile('Registration Time: (.*?)\n')
    if len(f.findall(a))==0 :f=re.compile('Expiration Time: (.*?)\n')
    print(b.findall(a))
    print(c.findall(a))
    print(d.findall(a))
    # print(e.findall(a))
    print(f.findall(a))
    print(g.findall(a))
    import time
    z=(int(time.mktime(time.strptime(f.findall(a)[0][:10],"%Y-%m-%d")))-time.time())/3600/24
    print(int(z))

    # https://domainapi.aliyun.com/onsale/search?fetchSearchTotal=true&token=tdomain-aliyun-com:BsKGJvEZlR5205aTheGfWpIlkrlSx1cz&currentPage=2&pageSize=50&productType=2&searchIntro=false&keywordAsPrefix=false&keywordAsSuffix=false&exKeywordAsPrefix=false&exKeywordAsSuffix=false&exKeywordAsPrefix2=false&exKeywordAsSuffix2=false&callback=jQuery111108396808333749162_1544676257265&_=1544676257279
    # https://mi.aliyun.com/
s_whois("chery.vip")