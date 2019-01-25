#conding=utf-8
from selenium import webdriver
import RandomHeaders
print(RandomHeaders.LoadHeader())
ua={'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Upgrade-Insecure-Requestss': '1', 'Cache-Control': 'max-age=0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 '}

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", ua)
# profile.set_preference('network.proxy.type', 0)
# profile.set_preference('network.proxy.http', '119.101.117.204')
# profile.set_preference('network.proxy.http_port', 9999)
# profile.set_preference('network.proxy.ssl', '119.101.114.47')
# profile.set_preference('network.proxy.ssl_port', 9999)
profile.update_preferences()#重载
driver = webdriver.Firefox(profile)
# driver.get('http://ip138.com/')
# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://www.baidu.com/')
#！！！
# from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities
# dcap=dict(DesiredCapabilities.FIREFOX)
url = 'http://132.232.249.247:81/ip'
driver.get(url)
#---------------------------cookie--------------


print(driver.get_cookies())
driver.delete_all_cookies()
driver.add_cookie({'name':'JSESSIONID','value':'6D456EFBA48EE57A09A033xxxxxxxxxxxx'})
driver.get(url)

# javasprite
# firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference("permissions.default.stylesheet",2)
# firefox_profile.set_preference("permissions.default.image",2)
# firefox_profile.set_preference("javascript.enabled",False)
# firefox_profile.update_preferences()
# firefox = webdriver.Firefox(firefox_profile)



proxys="--proxy-server=http://118.89.150.117:1080"
chromeOptions.add_argument(proxys)

chromeOptions.add_argument('user-agent='+ ua)
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(chrome_options = chromeOptions)