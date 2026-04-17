from products import products

for product in products:
    max_price = 0
    
    for variant in product['variants']:
        if variant['price'] > max_price:
            max_price = variant['price']
    
    print(product['name'], max_price)