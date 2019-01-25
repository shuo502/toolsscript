# # 启动google浏览器
from selenium import webdriver
import time

from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
ua='Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
proxys="--proxy-server=http://118.89.150.117:1080"
chromeOptions.add_argument(proxys)
chromeOptions.add_argument('user-agent='+ ua)
browser = webdriver.Chrome(chrome_options = chromeOptions)
browser.get('http://132.232.249.247:81/ip')
browser.quit()
print(browser.page_source)
# browser.get('https://132.232.249.247')

# # # browser.quit()


import requests
s=requests.get('https://www.xicidaili.com/').content.decode()
print(s)






# # 启动火狐浏览器
# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://www.baidu.com/')
#
# # 启动IE浏览器
# from selenium import webdriver
#
# browser = webdriver.Ie()
# browser.get('http://www.baidu.com/')
#    1.chromedriver 下载地址：https://code.google.com/p/chromedriver/downloads/list
#      2.Firefox的驱动geckodriver 下载地址：https://github.com/mozilla/geckodriver/releases/
#      3.IE的驱动IEdriver 下载地址：http://www.nuget.org/packages/Selenium.WebDriver.IEDriver/
