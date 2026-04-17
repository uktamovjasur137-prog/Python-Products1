from products import products

ratings = []

for p in products:              
    for r in p.get('reviews', []):  
        ratings.append(r['rating'])

print(ratings)