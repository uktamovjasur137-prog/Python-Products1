from products import products
from pprint import pprint

result = filter(lambda x: x['is_active'] == True, products)
pprint(list(result))
