import json

with open('/home/julia/Downloads/manager_sales.json') as file:
    data = json.load(file)

best_manager = max(data, key=lambda x: sum(car['price'] for car in x['cars']))

first_name = best_manager['manager']['first_name']
last_name = best_manager['manager']['last_name']
total_sales = sum(car['price'] for car in best_manager['cars'])

print(f"Best manager: {first_name} {last_name}")
print(f"Total sales: {total_sales}")
