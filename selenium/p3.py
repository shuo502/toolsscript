from selenium import webdriver
# import RandomHeaders
import os
import time

######THIS CLEARS OUT THE SCREEENSHOTS FOLDER#############3
for items in [file for file in os.listdir('Screenshots') if file.endswith('.png')]:
    os.remove('Screenshots/{}'.format(items))
################################

SizeDiscrepancy = 1000

##########PROXIES#################
proxies = [{"ip": '104.144.1.00', "port": '3190'}, {"ip": '104.144.45.91', "port": '3190'}]
# Above is just an example of the format to be used

input('You are about to open {} individual windows...  Continue?'.format(len(proxies)))

#########URL################3
url = 'http://132.232.249.247:81/ip'
# Use whatever URL you'd like to open here

ua={'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Upgrade-Insecure-Requestss': '1', 'Cache-Control': 'max-age=0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 '}

for proxy in proxies:
    profile = webdriver.FirefoxProfile()
    # IF this doesn't work, use a different selenium webdriver

    #########THIS PART SETS UP THE PROXIES######################3
    # profile.set_preference("general.useragent.override", RandomHeaders.LoadHeader())
    profile.set_preference("general.useragent.override",ua)
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", str(proxy['ip']))
    profile.set_preference("network.proxy.http_port", int(proxy['port']))
    profile.set_preference("network.proxy.ssl", str(proxy['ip']))
    profile.set_preference("network.proxy.ssl_port", int(int(proxy['port'])))
    profile.set_preference('network.proxy.socks', str(proxy['ip']))
    profile.set_preference('network.proxy.socks_port', int(int(proxy['port'])))
    profile.update_preferences()
    drivers = webdriver.Firefox(firefox_profile=profile)
    #############################################################################

    # GO TO URL
    drivers.get(url)
    #############################

    # SAVE SCREENSHOT
    drivers.save_screenshot('Screenshots/{}.png'.format(str(proxy['ip']) + ':' + str(proxy['port'])))
##############################


########################################################################
FileSize = 0
for screenshot in [file for file in os.listdir('Screenshots') if file.endswith('.png')]:
    FileSize = + os.path.getsize('Screenshots/{}'.format(screenshot))
AverageFileSize = FileSize / len([file for file in os.listdir('Screenshots') if file.endswith('.png')])
for screenshot in [file for file in os.listdir('Screenshots') if file.endswith('.png')]:
    if abs(int(os.path.getsize('Screenshots/{}'.format(screenshot))) - int(FileSize)) > SizeDiscrepancy:
        print('Window: {} is different from the other windows'.format(str(screenshot).replace('.png', '')))
#######THIS bases the similarity of windows based on file size of the screenshot.  A completely black screenshot or a 404
# page is going to be a different size than a correctly loaded page.  Change that
