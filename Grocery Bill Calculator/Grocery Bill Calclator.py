import numpy as np

items = ["water","ptato","soap","lemon","suger"]
price = np.array([50,60,110,60,180])

"""Total Bill"""
Total_bill = np.sum(price)
print(f"Total Bill of Things Bought: {Total_bill}")

"""Expensive Thing"""
expensive_thing = np.argmax(price)
print(f"{items[expensive_thing]} is most expensive with price of {price[expensive_thing]}")

"""Avg of Things Price"""
avg_price = np.average(price)
print(avg_price)