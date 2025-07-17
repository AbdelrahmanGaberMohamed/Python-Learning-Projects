prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0


# Write your code below
# Fuction returns list of affordable items, number unaffordable items, and total budget needed to buy all items

for index, item_price in enumerate(prices):
    if item_price <= budget_per_item:
        affordable_items.append(items[index])
        total_needed += item_price
cant_afford = len(items) - len(affordable_items)


print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
