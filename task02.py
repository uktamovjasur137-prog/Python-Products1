from products import products

result = []
for product in products:
    result.append(product['name'])

print(result)