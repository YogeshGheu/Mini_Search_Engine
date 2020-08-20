import re
from time import time

stock_list = ["python is cool", "python is good", "python is not python snake"]
search_in = input("Enter Your Query String: ")
search_in = search_in.lower()
item_no = 0
cache_dict = {}
init_time = time()

for item in stock_list:
    list_temp1 = [] #stores the search items quantity in the current list element
    pattern = re.compile(f"{search_in}")
    match = re.findall(pattern, item)
    for qty in match:
        list_temp1.append(qty)
        if qty == search_in:
            cache_dict[stock_list[item_no]] = len(list_temp1)
    item_no += 1
swapped_dict = dict([(value, key) for key, value in cache_dict.items()])
after_time = time()
print(f"Results Found: {len(swapped_dict)} (in {str(after_time - init_time)[0:5]} Seconds): \n")

if len(swapped_dict) == 0:
    print("Sorry! No Results Found.")
else:
    serialize = 0
    for i in reversed(sorted(swapped_dict)):
        serialize += 1
        print(f"{serialize}. {swapped_dict[i]} ")