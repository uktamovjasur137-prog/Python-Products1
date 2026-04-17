from products import products
from pprint import pprint
result = {}

for product in products:
    category_name = product['category']['name']
    
    if category_name not in result:
        result[category_name] = []
    
    result[category_name].append(product)

pprint(result)