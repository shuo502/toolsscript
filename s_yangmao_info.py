#coding=utf-8
import  requests,re
#def
link_all=[]
link_title=[]
A_url=""
A_title=""
A_content=""

url="https://yangmao.info/pingce/2/"

def s_link(url):
    #def page
    re_pageN=re.compile('">(\d+)</a></li><li class="next-page',re.S)
    re_link_all=re.compile('<a href="(.*?)" title=".*?">(.*?)</a></h2>',re.S)
    temp_a=requests.get(url).content.decode()
    print(re_pageN.findall(temp_a))
    return re_link_all.findall(temp_a)

def s_Art(url):
    temp_a = requests.get(url).content.decode()
    re_content=re.compile('article-content">(.*?)</article',re.S)
    return re_content.findall(temp_a)
    pass

#link 入库 文章入库
from peewee import *
from peewee import MySQLDatabase
from peewee import Model
import datetime

db = MySQLDatabase("sdb", host="199.188.101.35", port=3306, user="root", passwd="pops123456")
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Papaurl(BaseModel):
    title = CharField(unique=True)
    url=CharField(unique=True)
    created_date=DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=False)

class Tweet(BaseModel):
    title = ForeignKeyField(Papaurl, related_name='tweets')
    content = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

