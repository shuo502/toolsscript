#conding=utf-8
# import requests
# u7rl='https://proxyapi.mimvp.com/api/fetchopen.php?orderid=868040630715106492&num=20&http_type=5&anonymous=5&ping_time=1&transfer_time=5&request_method=3&result_fields=1,2&result_sort_field=4'
# url='https://proxyapi.mimvp.com/api/fetchopen.php?orderid=868040630715106492&num=1&http_type=5&result_fields=1,2,3'
# # s=requests.get(url).content.decode()
# print(s.split(','))
# s=b'124.16.112.104:1080,Socks5,\xe9\xab\x98\xe5\x8c\xbf'.decode()
from pyvirtualdisplay import Display
from selenium import webdriver
display = Display(visible=0, size=(900, 800))
display.start()
driver = webdriver.Firefox()
driver.get('http://www.haosou.com')
print (driver.title)