# conding=utf-8
import re

def log_file(myfile='log', alliplist=[], piclist=[], piclist_a=[], re_s=1, n=[]):

    if len(alliplist) == 0: alliplist = []
    if len(piclist) == 0:  piclist = []
    if len(piclist_a) == 0:  piclist_a = []
    if len(n) == 0:  n = []
    print(myfile)
    logfile =path + str(myfile)
    s = open(logfile, 'r', encoding='utf-8').read()
    if re_s == 1:
        y = r2.findall(s)
    else:
        print("abc")
        y = r1.findall(s)

    for i in y:
        piclist.append(i[2])
        if i[0] not in alliplist:
            alliplist.append(i[0])
            piclist_a.append(i[2])
            n.append(i)
            print(i)
    print('总计访问IP ' + str(len(y)))
    print(str(myfile) + " 综合IP去重IP  " + str(len(n)))
    # pic_us(piclist)

    return alliplist, piclist, piclist_a


def pic_us(piclist,url):
    zz = []
    ee = {}
    for i in piclist:
        if i not in zz:
            zz.append(i)
            ee[i] = 1
        else:
            ee[i] = int(ee[i]) + 1
    # print(ee)
    x = 0
    for i in ee:
        x = x + ee[i]
        print(url+ i, ee[i])
    print(x)


r2 = re.compile(' (.*?) .*? \[(.*?)\] .*? \"GET /subject_tv/images/(.*?) HTTP/1.1\" 200 ')
r1 = re.compile('(.*?) - - \[(23.*?)\] \"GET /subject_tv/images/(.*?) HTTP/1.1\"')
path = 'C:\\Users\\dd\\Desktop\\temp\\'
url=""

ip = []
pic = []
pic_a = []
ip, pic,pic_a = log_file("xx", ip, pic, pic_a)

ip, pic,pic_a = log_file("cxx.log", ip, pic, pic_a, 2)
pic_us(pic)

pic_us(pic_a,url)
