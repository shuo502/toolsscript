#conding=utf-8

from PIL import Image
import imageio,os
def downpiont(img):
    #下白边
    img_array = img.load()
    w=int(img.size[0])
    h=int(img.size[1])
    k=h
    print(img.size)
    if w <h:
        k=w
    n=""
    for i_t in range(k):
        i=k-i_t-1
        t_i=img_array[int(i), int(i)]
        if len(t_i)==4:
            xx = sum(t_i)-255
        else:
            xx = sum(t_i)
        if xx < 100:
            print(i)
            n = i
            break
    for i_i_i in range(n,w):
        wx=[]
        for i in range(h):
            t_i=img_array[i_i_i, int(i)]
            if len(t_i)==4:
                xx = sum(t_i)-255
            else:
                xx = sum(t_i)
            if xx < 156:
                wx.append(1)
            else:
                wx.append(0)
        if (sum(wx)) == 0:
            w_t = i_i_i+1
            print("w:", i_i_i)
            break

    for i_i_i in range(n,h):
        wx = []
        for i in range(w):
            t_i=img_array[int(i), i_i_i]
            if len(t_i)==4:
                xx = sum(t_i)-255
            else:
                xx = sum(t_i)
            if xx < 156:
                wx.append(1)
            else:
                wx.append(0)
        if (sum(wx)) == 0:
            h_t = i_i_i+1
            print("h:", i_i_i)
            break
    return w_t, h_t


def uppiont(img):
    #上白边
    w_t, h_t=0,0
    img_array = img.load()
    w=int(img.size[0])
    h=int(img.size[1])
    k = h
    if w < h:
        k = w
    n=""
    for i_t in range(k):
        i=i_t
        t_x=img_array[int(i), int(i)]
        if len(t_x)==4:
            xx = sum(t_x)-255
        else:
            xx = sum(t_x)
        if xx <100: #hei 0<255bai
            print(i)
            n=i
            break
    #shu
    for i_i in range(n):
        n_t1=int(n)-int(i_i)
        wx=[]
        for i in range(h):
            t_x=img_array[n_t1, int(i)]
            if len(t_x) == 4:
                xx = sum(t_x) - 255
            else:
                xx = sum(t_x)
            if xx<156:
                wx.append(1)
            else:
                wx.append(0)
        if (sum(wx) )==0:
            w_t = n_t1-1
            print("w:", w_t)
            break
    #heng
    for i_i in range(n):
        n_t1 = int(n) - int(i_i)
        wx = []
        for i in range(w):
            t_x=img_array[int(i), n_t1]
            if len(t_x) == 4:
                xx = sum(t_x) - 255
            else:
                xx = sum(t_x)
            if xx < 156:
                wx.append(1)
            else:
                wx.append(0)
        if (sum(wx)) == 0:
            h_t = n_t1-1
            print("h:", h_t)
            break
    return w_t,h_t

def qubian(files,p=[]):
    print(files)
    img=Image.open(files)
    x2,y2=downpiont(img)
    x1,y1=uppiont(img)
    x=[x1,y1,x2,y2]
    # #
    # print(x1,y1,x2,y2)
    img_x=img.crop(x)#裁剪
    if len(p)>0:
        out = img_x.resize((p), Image.ANTIALIAS)  # 缩放
        return out
    return img_x
    #


def merge(templatefiles,img_c,savefile='./out.png'):
    #合成图片 模板 图片 保存位置
    template_img = Image.open(templatefiles)
    box=(311,1028,762,1479)
    region = img_c.resize((box[2] - box[0], box[3] - box[1]))
    template_img.paste(region, box)
    template_img.save(savefile)  # 保存图片


def lsfile(path_i='./',x='none'):
    #遍历文件夹
    if path_i[-1]=="/":
        filenames = sorted(str(path_i)+str(fn) for fn in os.listdir(path_i))
        print(filenames)
        if 'none' not in x:
            filenames = sorted((str(path_i)+str(fn) for fn in os.listdir(path_i) if fn.endswith(x)))
        # filenames.sort(reverse=True)

        # filenames = []
        return filenames
    else:
        filenames = sorted(str(path_i) + str(fn) for fn in os.listdir(path_i))
        print(filenames)
        if 'none' not in x:
            filenames = sorted((str(path_i) + str(fn) for fn in os.listdir(path_i) if fn.endswith(x)))
        # filenames.sort(reverse=True)

        # filenames = []
        return filenames
        return []

def files(img_path='./pic/'):
    s=[]
    import os
    # img_path = './pic/'
    img_list = os.listdir(img_path)
    img_list.sort()
    img_list.sort(key=lambda x: int(x[:-4]))  ##文件名按数字排序
    img_nums = len(img_list)
    for i in range(img_nums):
        img_name = img_path + img_list[i]
        s.append(img_name)
        # print(img_name)
    return s

def create_gif(filenamess,name='gif.gif'):
    #合成GIF 动态图片 duration=1 间隔秒
    imagess=[]
    filenames=lsfile(filenamess)
    print(filenames)
    images = []
    # if s=="k":
    for filename in filenames:
        print(filename)
        imagess.append(imageio.imread(filename))
    print(imagess)
    imageio.mimsave(name, imagess,duration=1)
    # else:
    #     i=1
    #     for filename in filenames:
    #         file=str(filenamess)+str(i)+str(filename[-4:])
    #         print(file)
    #         images.append(imageio.imread(file))
    #         i=i+1
    #     imageio.mimsave(name, images,duration=1)

def erpic(filepath='./pic/',zoo=[455,455]):
    #批量去白边框缩放指定大小
    for i in lsfile(filepath):
        print(i)
        #x=qubian(i,[455,455])moban
        x=qubian(i,zoo)
        x.save(i)  # 保存


def savepic(picfile,template,savefile=''):
    #批量合成文件夹图片 目标 模板 保存地址
    # savepic("./pic/","./t2.png","./save/")
    filenames=lsfile(picfile)
    t_i=0
    for i in range(len(filenames)):
        ocr_img = Image.open(filenames[i])
        # filename='./save/'+str(i)+'.jpg'
        filename=savefile+str(i)+'.jpg'
        merge(template,ocr_img,filename)
# savepic("./pic/","./t2.png","./save/")

# create_gif('./pic/','s.gif')
def update():
    #更新图片
    import requests
    import re
    s1=re.compile("(/ss.php\?action=img_merge.*?)'")
    s=requests.get("http://cuk.cn/ss.php")
    s2=s1.findall(s.content.decode(s.encoding))
    for i in s2:
        url='http://cuk.cn'+str(i)
        requests.get(url)
update()
# erpic('c://2/')
# create_gif('c://2/','pic4.gif')
# img_c = qubian(r"./2.jpg")
# img_c = qubian(r"./pic/17 微信号：cuk13209  沈.png")


# erpic()
# create_gif('./pic/','pic3.gif')

# lsfile('./pic/')
# #

# create_gif('C:/b/','1226.gif')
# x="ssssabcdefg"
# print(x[x.find("b"):])
# print(x[:-3])

