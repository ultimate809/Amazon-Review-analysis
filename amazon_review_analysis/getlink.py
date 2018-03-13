# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import sentiment_mod as sent
from tkinter import *
import os

print("Enter the product link to see result : ")
first_url=input()


class getlink(scrapy.Spider):
    name = 'getlink'
    allowed_domains = ['amazon.in']
    #start_urls = ['https://www.amazon.in/gp/product/B006RHKER4/ref=s9u_cartx_gw_i2?ie=UTF8&pd_rd_i=B006RHKER4&pd_rd_r=f4351443-cbc3-11e7-8c37-3da6d9ea9702&pd_rd_w=cSFeV&pd_rd_wg=afVVT&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=Q0ABX3J4HKTHPBRKPSM6&pf_rd_t=36701&pf_rd_p=a66bc199-b270-44de-9fcc-5cf0a06a7727&pf_rd_i=desktop']
    start_urls=[first_url]

    def parse(self, response):
        link=response.xpath('//a[contains(@data-hook,"see-all-reviews-link")]/@href').extract()
        f=open("link.txt","w")
        f.write(link[0])
        f.close()
if __name__ == "__main__":	
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    print("1")
    process.crawl(getlink)
    process.start()

link="https://www.amazon.in"      
with open('link.txt','r') as f:
    for line in f:
        link+=line   	
f.close()
link+="&pageNumber="
links_all_rev=[]
for i in range(0,1000):
    links_all_rev.append("0")
for i in range(1,4):
    links_all_rev[i-1]=link+str(i)
f=open("flinks.txt","w")
for i in range(0,3):
    f.write(links_all_rev[i])
    f.write("\n")
f.close()




