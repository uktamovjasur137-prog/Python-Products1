from products import products

for product in products:
    reviews = product['reviews']
    
    if len(reviews) == 0:
        print(product['id'], 0)
    else:
        total = 0
        
        for review in reviews:
            total += review['rating']
        
        avg = total / len(reviews)
        print(product['id'], avg)