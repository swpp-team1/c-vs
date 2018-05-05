import requests
from bs4 import BeautifulSoup

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
        productList.extend(list(map(
            lambda x: {'name': x.find(class_='name').get_text(), 'price': int(x.find(class_='price').get_text().replace('\n','').replace(',','')), 'url': 'http://www.7-eleven.co.kr' + x.find('img')['src']}, 
            htmlList)))
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
    productList.extend(list(map(
        lambda x: {'name': x.find(class_='name').get_text(), 'price': int(x.select('.price > span')[0].get_text().replace('\n','').replace(',','')), 'url': 'http://www.7-eleven.co.kr' + x.find('img')['src']}, 
        htmlList)))
pbCrawler()
lunchboxCrawler()
print(productList)