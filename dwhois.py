#coding=utf-8
# #查询 备案 查询域名
#国内云商绑定用户域名的时候利用这个查询域名是否备案。
#查询是否有收录
import socket
import random
import time
import sys
from whoishost import whoishost
stki=31413
# print(sys.version_info >= (3,3))  #判断系统版本是否大于或等于3.3
# print(sys.version_info.major)     #打印大版本号
# print(sys.version_info.minor)     #打印小版本号
if sys.version_info.major==3:
    py=True
else:
    py=False
def whoiskey(ikey,ss="0"):

    # if not whoishost:whoishost='whois.cnnic.cn'
    try:
        if ss=="0":
            nichost,word,key=whoishost(ikey)
        else:
            nichost=ss
            key=ikey
        print(ikey)
        print(nichost)
        if nichost == "[Null]": return nichost
        timeout = 2
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect(('whois.internic.net', 43))
        # s.connect(('whois.cira.ca', 43))
        s.connect((nichost, 43))
        if py:
            e = b'%b \r\n' % bytes(key, encoding="utf8")
        else:
            e = b'%s \r\n' % bytes(key, )
        print(e)
        s.send(e)
        response =b''
        # response =s.recv(4096)
        while True:
            data = s.recv(4096)
            response += data
            if not data :
                break
        s.close()
        if py:
            return response.decode()
        else:
            return response.decode("utf-8")
    except:
        return "time out or other err"

def keywork():
    key=[]
    # for i in range(48,58):#Nb
    #     v=chr(i)
    #     key.append(v)
    for i in range(97,123):#Str
        v = chr(i)
        key.append(v)
    pass
    print(len(key))
    return key

def keylist(key):
    keydic=[]
    for j in key:
        keydic.append(j)
        for k in key:
            keydic.append(j+""+k)
            for m in key:
                keydic.append(j+""+k+""+m)
                for n in key:
                    keydic.append(j+""+k+""+m+""+n)
    return keydic

def secrdict():
    return keylist(keywork())

def radomkey(keydic,n=100):
    strn=random.sample(keydic, n)
    # strn=random.randrange(0,len(keydic))
    dk=keydic[strn]
    return dk

def okw(value,tfile="file.txt",op='a'):
    # oks = open(k[1][1] + 'ok.txt', 'a')
    oks = open(tfile, op)
    x=value
    if py:
        # ve=b'%b \r\n' % bytes(x, encoding="utf8")
        oks.write(str(x))
        oks.close()
    else:
        oks.write(x.encode("gbk") + "\n")
        oks.close()
    print("!!!!!!!", x)

def searchd(k,n):
     return radomkey(secrdict,n)

def forwhois():
    secrdict

def search(d="xx.cn",keydic="",st=0,mend=0):
    if keydic=="":keydic=secrdict()
    k=whoishost(d)
    dot=k[1][1]
    fil = dot + 'ok.txt'
    nic=k[0]#注册局
    f = open(k[1][1]+'file.txt', 'a')
    okd=[]

    if mend==0:mend=len(keydic)
    for i in range(st,mend):
        key=keydic[i]+dot
        x=whoiskey(key,nic)
        if py:
            # ve=b'%b \r\n' % bytes(x, encoding="utf8")
            f.write(str(x))
        else:
            f.write(x.encode("gbk") + "\n")
        if "too short" in x:
            x=whoiskey(key,nic)
        if "No matching" in x:
            okd.append(key)
            val=key+"\n"
            okw(val,fil)
        if "No match for" in x:
            okd.append(key)
            val = key + "\n"
            okw(val, fil)
    f.close()
    return "ok---"+str(okd)

if __name__ =="__main__":
    search("mm.net")
    # okd=[]
    # keydic=secrdict()
    # k=whoishost("bbc.cn")
    # nic=k[0]#注册局
    # f = open(k[0]+'file.txt', 'a')
    # for i in range(stki,len(keydic)):
    #     try:
    #         print("--",i,"--")
    #         dk=keydic[i]+".cn"
    #         print(dk)
    #         time.sleep(1)
    #         x=whoiskey(dk,nic)
    #         if "[Null]" not in x:
    #             if "too short"in x:
    #                 x=whoiskey(dk,nic)
    #             # print(x)
    #             if "No matching" in x:
    #                 okd.append(dk)
    #                 print("!!!!!!!",x)
    #             if "No match for" in x:
    #                 # print(x)
    #                 okd.append(dk)
    #                 print("!!!!!!!", x)
    #             print(i,"--")
    #             if okd:print("--------",okd)
    #             x=x+str(i)
    #             if py:
    #                 # ve=b'%b \r\n' % bytes(x, encoding="utf8")
    #                 x=str(x)
    #                 f.write(x)
    #             else:
    #                 f.write(x.encode("gbk") + "\n")
    #     except  :
    #         print("@---ERR:%s---@" % str(keydic[i]))
    #         print("@---ERR:id---@" ,i)
    #         pass
    # f.close()
    #
    # # print("------------------------------------------------")
    # print("-------st----------")
    # print(okd)
    # print("-------end----------")
