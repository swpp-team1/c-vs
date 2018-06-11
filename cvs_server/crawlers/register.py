import sys
import os
import ast
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvs_server.settings")
import django
django.setup()

from cvs_rest.models import Product
from django.core.exceptions import ObjectDoesNotExist


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('register.py <file> <manufacturer>')
        sys.exit()
    if sys.argv[2] not in ('SE', 'CU', 'GS'):
        print('manufacturer have tp be CU SE GS')
        sys.exit()
    print('Register START')
    f = open(sys.argv[1], 'r')
    product_data_dict = f.read()
    product_data_dict = ast.literal_eval(product_data_dict)
    for p in product_data_dict:
        try:
            Product.objects.get(name=p['name'])
        except ObjectDoesNotExist:
            print('\t{} is registed in DB'.format(p['name']))
            Product(
                name=p['name'], 
                price=p['price'], 
                image=p['img'], 
                manufacturer=sys.argv[2],
                large_category=p['large_category'],
                small_category=p['small_category'],
                PB=True,
            ).save()
    f.close()
