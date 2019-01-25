#conding=utf-8
from selenium import webdriver
import RandomHeaders
import requests
# f90fda7e11da
# 10fbb76e34
url='https://proxyapi.mimvp.com/api/fetchopen.php?orderid=868040630715106492&num=1&http_type=5&result_fields=1,2,3'
url='https://proxyapi.mimvp.com/api/fetchopen.php?orderid=868040630715106492&num=1&http_type=2&result_fields=1,2,3'
s=requests.get(url).content.decode().split(",")[0].split(":")
print(s)
# s=['124.16.112.104', '1080']
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", RandomHeaders.LoadHeader()["User-Agent"])
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", str(s[0]))
profile.set_preference("network.proxy.http_port", int(s[1]))
profile.set_preference("network.proxy.ssl", str(s[0]))
profile.set_preference("network.proxy.ssl_port", int(int(s[1])))
profile.set_preference('network.proxy.socks', str(s[0]))
profile.set_preference('network.proxy.socks_port', int(int(s[1])))
profile.update_preferences()
drivers = webdriver.Firefox(firefox_profile=profile)
#############################################################################
# url = 'http://132.232.249.247:81/ip'
url = 'https://baidu.com/'
drivers.get(url)
print(drivers.page_source)

