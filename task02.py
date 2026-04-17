from products import products

result = map(lambda x: x['name'], products)
print(list(result))