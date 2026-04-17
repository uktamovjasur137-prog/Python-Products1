from products import products

result = filter(lambda x: x['variants']['in_stock'] == 0, products)
print(list(result))