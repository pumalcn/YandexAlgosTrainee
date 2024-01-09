
import sys
result = {}

for line in sys.stdin.read():
    name, product, count = line.split()
    result.setdefault(name, {})
    result[name][product] = result[name].get(product, 0) + int(count)

for name in sorted(result.keys()):
    print(f'{name}:')
    data = result[name]
    for product in sorted(data.keys()):
        print(f'{product} {data[product]}')



#
# import sys
# from collections import defaultdict
#
#
# def sales(sales_data):
#     customers = defaultdict(lambda: defaultdict(int))
#     for customer, item, quantity in sales_data:
#         customers[customer][item] += quantity
#     return customers
#
#
#
#
#
#
# sales_data = []
# for line in sys.stdin:
#     sales_item = line.split()
#     sales_data.append((sales_item[0], sales_item[1], int(sales_item[2])))
# results = sales(sales_data)
# for customer in sorted(results.keys()):
#     print(f'{customer}:')
#     customer_data = results[customer]
#     for item in sorted(customer_data.keys()):
#         print(f'{item} {customer_data[item]}')
#
#
