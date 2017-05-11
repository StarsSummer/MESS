#coding=utf-8
import urllib
import urllib2
import re
import os
import socket

socket.setdefaulttimeout(3)

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'"objURL":"(.*?)"'
    imgre = re.compile(reg)
    print imgre
    imglist = re.findall(imgre,html)
    print len(imglist)
    return imglist

def download(urls,path,pages):
    index=1+pages
    for url in urls:
        print "Downloading:"+url
        try:
            res=urllib2.Request(url)
            if str(res.status_Code)[0]=="4":
		print "Failed!!!"
                continue
	
        except Exception as e:
            print index," Downloaded!!! "
        filename=os.path.join(path,str(index)+".jpg")
	try:
            urllib.urlretrieve(url,filename)
	except Exception as e:
	    print "timeout"
	    index+=1
	    continue
        index+=1
        if index>20+pages:
            break

word= "北京烤鸭"
Savepath="/home/zsummer/Desktop/code/RoastDuck"

for pages in ["0","20","40","60","80"]:
	html = getHtml("https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+word+"&pn="+pages)
	download(getImg(html),Savepath,int(pages))



