from selenium import webdriver
from selenium.webdriver.common.proxy import *
from base64 import b64encode
def spider_url_firefox_by_socks(url,x):
    browser = None
    display = None

    ## 授权密码，请见米扑代理会员中心： https://proxy.mimvp.com/usercenter/userinfo.php?p=whiteip
    mimvp_proxy = x
    print(x)
    proxy_config = Proxy({
        'proxyType': ProxyType.MANUAL,  # 1
        'httpProxy': mimvp_proxy['ip'] + ":" + str(mimvp_proxy['port_https']),
        'sslProxy': mimvp_proxy['ip'] + ":" + str(mimvp_proxy['port_https']),
        'socksProxy': mimvp_proxy['ip'] + ":" + str(mimvp_proxy['port_socks']),
        'ftpProxy': mimvp_proxy['ip'] + ":" + str(mimvp_proxy['port_https']),
        'noProxy': 'localhost,127.0.0.1',
        'socksUsername': mimvp_proxy['username'],
        'socksPassword': mimvp_proxy['password'],
    })

    # try:
        # display = Display(visible=0, size=(800, 600))
        # display.start()

    profile = webdriver.FirefoxProfile()

    # add new header
    profile.add_extension("modify_headers-0.7.1.1-fx.xpi")
    profile.set_preference("extensions.modify_headers.currentVersion", "0.7.1.1-fx")
    profile.set_preference("modifyheaders.config.active", True)
    profile.set_preference("modifyheaders.headers.count", 1)
    profile.set_preference("modifyheaders.headers.action0", "Add")
    profile.set_preference("modifyheaders.headers.name0", "Proxy-Switch-Ip")
    profile.set_preference("modifyheaders.headers.value0", "yes")
    profile.set_preference("modifyheaders.headers.enabled0", True)

    # add proxy
    profile.set_preference('network.proxy.type', 1)  # ProxyType.MANUAL = 1
    if url.startswith("http://"):
        profile.set_preference('network.proxy.http', mimvp_proxy['ip'])
        profile.set_preference('network.proxy.http_port', mimvp_proxy['port_https'])  # 访问http网站
    elif url.startswith("https://"):
        profile.set_preference('network.proxy.ssl', mimvp_proxy['ip'])
        profile.set_preference('network.proxy.ssl_port', mimvp_proxy['port_https'])  # 访问https网站

    # Proxy auto login （自动填写密码，进行代理授权）
    profile.add_extension('close_proxy_authentication-1.1.xpi')
    credentials = '{username}:{password}'.format(username=mimvp_proxy['username'],
                                                 password=mimvp_proxy['password'])  # auth
    credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
    profile.set_preference('extensions.closeproxyauth.authtoken', credentials)

    profile.update_preferences()

    browser = webdriver.Firefox(profile)  # 打开 FireFox 浏览器
    browser.get(url)
    content = browser.page_source
    # print("content: " + str(content))
    # finally:
    #     pass
        # if browser: browser.quit()
        # if display: display.stop()
if __name__=='__main__':
    pass
    s={
        'ip': '140.143.62.84',  # ip
        'port_https': 62288,  # http, https
        'port_socks': 62287,  # socks5
        'username': 'mimvp-user',
        'password': 'mimvp-pass'
    }
    import requests

    # f90fda7e11da
    # 10fbb76e34
    url = 'https://proxyapi.mimvp.com/api/fetchsecret.php?orderid=868040630715106492&num=1&http_type=5&result_fields=1,2,3'
    # s = requests.get(url).content.decode().split(",")[0].split(":")
    s=['117.69.51.96', '37154']
    print(s)
    url="https://baidu.com"
    key={'ip':str(s[0]),'port_https': int(s[1]),  'port_socks': int(s[1]),   'username': 'f90fda7e11da', 'password': '10fbb76e34' }
    spider_url_firefox_by_socks(url,key)