import pandas as pd
import os
import time,datetime
import pyodbc
import requests
import threading
from lxml import etree
import re
import pandas as pd
from tqdm import tqdm
from fake_useragent import UserAgent
def get_html(url):
    response = requests.get(url, headers = {'User-Agent': UserAgent().random, 'Accept-Language': 'zh-CN,zh;q=0.9'})        
    return response 

df = pd.DataFrame()
quyu = ['jiangan','jianghan','qiaokou','dongxihu','wuchang','qingshan',
        'hongshan','hanyang','donghugaoxin','jiangxia','caidian','huangbei','xinzhou','tunkoukaifaqu','hannan','xinzhou','tunkoukaifaqu','hannan']
for c in quyu:
    print(c)
    for i in tqdm(range(1,101)):
        response = get_html(f'https://wh.lianjia.com/ershoufang/{c}/pg{i}/')
        selector = etree.HTML(response.content)
#         jianjie = selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/text()')
#         xiaoqu = selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[1]/text()')
    #     quyu = [etree.HTML(get_html(i).content).xpath('/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a[1]/text()')[0] for i in url]
#         data = selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[3]/div/text()')
#         huxing = [i.split(" | ")[0]  for i in data]
#         mianji = [i.split(" | ")[1]  for i in data]
        guanzhu = [i.split('/')[0] for i in selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[4]/text()')]
#         fabusj = [i.split('/')[1].strip() for i in selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[4]/text()')]
        fangjia = [float(i) for i in selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()')]
        danjia = selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()')
#         chengqu = selector.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()')
        d = pd.DataFrame({"房价": fangjia, "单价/平":danjia, '关注人数': guanzhu})
        df = pd.concat([df, d], ignore_index=True)