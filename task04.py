from products import products

result = {}

for product in products:
    result[product['name']] = len(product.get('variants', []))

print(result)