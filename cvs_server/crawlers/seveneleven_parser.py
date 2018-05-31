import requests
from bs4 import BeautifulSoup
from product_classify import classifyProducts
#to import upper folder `cvs_server`
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvs_server.settings")
import django
django.setup()

from cvs_rest.models import Product

productList = []

def pbCrawler():
    url = 'http://www.7-eleven.co.kr/product/listMoreAjax.asp'
    pageNo = 0
    listCnt = 1
    while listCnt != 0:
        req = requests.post(url, data={'intPageSize': 10, 'intCurrPage': pageNo, 'pTab': 5})
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        htmlList = soup.select('.pic_product > .pic_product')
        for element in htmlList:
            name = element.find(class_='name').get_text()
            category = classifyProducts(name)
            productList.append({
                'large_category': category['large_category'], 
                'small_category': category['small_category'], 
                'name': name, 
                'price': int(element.find(class_='price').get_text().replace('\n','').replace(',','')), 
                'img': 'http://www.7-eleven.co.kr' + element.find('img')['src']
            })
        pageNo = pageNo + 1
        listCnt = int(soup.find(id='listCnt')['value'])

def lunchboxCrawler():
    url = 'http://www.7-eleven.co.kr/product/dosirakNewMoreAjax.asp'
    pageNo = 1
    listCnt = 1
    while True:
        req = requests.post(url, data={'intPageSize': 10 * pageNo})
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        listCnt = int(soup.find(id='listCnt')['value'])
        if listCnt != 10 * pageNo:
            break
        pageNo = pageNo + 1
    req = requests.post(url, data={'intPageSize': listCnt})
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    htmlList = soup.select('.pic_product')
    for element in htmlList:
        name = element.find(class_='name').get_text()
        category = classifyProducts(name)
        productList.append({
            'large_category': category['large_category'], 
            'small_category': category['small_category'], 
            'name': name, 
            'price': int(element.select('.price > span')[0].get_text().replace('\n','').replace(',','')), 
            'img': 'http://www.7-eleven.co.kr' + element.find('img')['src']
        }) 
pbCrawler()
lunchboxCrawler()
# print(productList)

# code for registering product to DB
if __name__ == '__main__':
    product_data_dict = productList
    for p in product_data_dict:
        Product(
            name=p['name'], 
            price=p['price'], 
            image=p['img'], 
            manufacturer='SE',
            large_category=p['large_category'],
            small_category=p['small_category'],
            PB=True,
        ).save()   
