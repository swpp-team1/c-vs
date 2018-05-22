import requests
import json
#to import upper folder `cvs_server`
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvs_server.settings")
import django
django.setup()

from cvs_rest.models import Product
from product_classify import classifyProducts

#productSrvFoodCK description
#FreshFoodKey - fresh food
#DifferentServiceKey - different product


#searchProduct description
#in Fresh Food Key
#productLunch - search dosirak
#productRice - search gimbab & jumukbab
#productBurger - search burger
#productSnack - search fastfood , in Korean, gan pyeon sik
#in Different Service Key
#productDrink - search coffee & drink
#productMilk - search milk product
#productCookie - search snack
#productRamen - search ramen & processed food
#productGoods - search living items

def getPBProducts():
    product_list = []
    #setting url
    pageNum = 1
    pageSize = 16
    searchSrvFoodCK_list = ['FreshFoodKey', 'DifferentServiceKey']
    searchSort = 'searchALLSort'
    searchProduct = 'productALL'
    for searchSrvFoodCK in searchSrvFoodCK_list:
        url = "http://gs25.gsretail.com/products/youus-freshfoodDetail-search?pageNum={}&pageSize={}&searchSrvFoodCK={}&searchSort={}&searchProduct={}".format(pageNum, pageSize, searchSrvFoodCK, searchSort, searchProduct)
        # send request
        req = requests.get(url)
        header = req.headers
        status = req.status_code
        is_ok = req.ok
        if (is_ok == False) :
            print(status)
            return
        #get json data    
        json_raw = req.text
        json_data = json.loads(json_raw)
        json_data = json.loads(json_data)
        #total of products
        total_count = json_data['SubPageListPagination']['totalNumberOfResults']
        #total of pages
        total_page = json_data['SubPageListPagination']['numberOfPages']
        #append items to product_list
        for page in range(1,total_page): 
            url = "http://gs25.gsretail.com/products/youus-freshfoodDetail-search?pageNum={}&pageSize={}&searchSrvFoodCK={}&searchSort={}&searchProduct={}".format(page, pageSize, searchSrvFoodCK, searchSort, searchProduct)
            req = requests.get(url)
            is_ok = req.ok
            if (is_ok == False) :
                print(req.text)
                return    
            json_raw = req.text
            json_data = json.loads(json_raw)
            json_data = json.loads(json_data) 
            products = json_data["SubPageListData"]
            for product in products:
                name = product['goodsNm']
                category = classifyProducts(name)
                product_list.append({
                    'large_category': category['large_category'],
                    'small_category': category['small_category'], 
                    'name':product['goodsNm'],
                    'img':product['attFileNm'],
                    'price':product['price'],
                    'manufacturer': 'GS',
                })
                
    return product_list

print(getPBProducts())

'''
# code for registering product to DB
if __name__ == '__main__':
    product_data_dict = getPBProducts()
    for p in product_data_dict:
        Product(name=p['name'], price=p['price'], image=p['img'], manufacturer=p['manufacturer']).save()   
'''
