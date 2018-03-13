# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
#import sentiment_mod as sent
import sentiment_mod as sent
from tkinter import *
import os


urls=[]
rating=0
with open('flinks.txt','r') as f:
    for line in f:
        urls.append(line)
f.close()
f=open("a.txt","w")
f.close()
f=open("rating.txt","w")
f.close()

class RevspiderSpider(scrapy.Spider):
    name = 'revspider'
    allowed_domains = ['amazon.in']
    start_urls=urls
    #start_urls = ["https://www.amazon.in/SanDisk-Cruzer-Blade-Flash-Drive/product-reviews/B005FYNT3G/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber={}".format(i) for i in range(1,4)]

    def parse(self, response):
        author     = response.xpath('//a[contains(@data-hook,"review-author")]/text()').extract()
        title      = response.xpath('//a[contains(@data-hook,"review-title")]/text()').extract()
        rating     = response.xpath('//i[contains(@data-hook,"review-star-rating")]/span[contains(@class,"a-icon-alt")]/text()').extract()
        review_date= response.xpath('//span[contains(@data-hook,"review-date")]/text()').extract()
        review_body= response.xpath('//span[contains(@data-hook,"review-body")]/text()').extract()
        
        f=open("rating.txt","a")
        for i in rating:
        	f.write(i)
        	f.write("\n")
        f.close()
        f=open("a.txt","a")
        for i in review_body:
            f.write(i)
            f.write("\n")
        #f.write("fabulous fantastic great nice\n")
        f.close()
if __name__ == "__main__":	
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(RevspiderSpider)
    process.start()
#os.system("cd")
#os.system("python3 resama.py")
countpos=0
countneg=0
countrev=0
with open('a.txt','r') as f:
    for line in f:
        senti,conf=sent.sentiment(line)
        if(conf>70):
            if(senti=='pos'):
                countpos+=1
            elif(senti=='neg'):
                countneg+=1
            countrev+=1

print("posr : ",countpos)
print("negr : ",countneg)

rc=0
countrat=0
fs=0
with open('rating.txt','r') as f:
    for line in f:
    	rc+=int(line[0])
    	countrat+=1
    	if(line[0]=='5'):
    		fs+=1	
f.close()
print(fs)
print(rc)
print(countrat)
print(rc/countrat)
ans=(rc/countrat)+((countpos/countrev)*5)
print(ans)
if (ans>5):
    resrev="Good Product to buy"
    col="green"
elif(ans<5):
    resrev="Bad Product to buy"
    col="red"
else:
    resrev="Ok Product"
    col="orange"
print("hello6")
master = Tk()
master.geometry("350x350")
label=Label(master, text=resrev)
label.place(relx=0.35, rely=0.5)
master.configure(background=col)
mainloop()
      
