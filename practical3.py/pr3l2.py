print("Inventory Shop Item Operations")
print("Enter item numbers separated by spaces:")
line = input().strip()
if not line:
    print("No items entered.")
    raise SystemExit

items = []
for token in line.split():
    if token.isdigit():
        items.append(int(token))
    else:
        print(f"Ignored invalid item: {token}")

if len(items) == 0:
    print("No valid item numbers found.")
    raise SystemExit

# a) total number
print("a) Total number of items:", len(items))
# b) last item
print("b) Last item number:", items[-1])
# c) sorted list
sorted_items = sorted(items)
print("c) Items in sorted order:", sorted_items)
# d) contains 515?
print("d) Contains 515:", "Yes" if 515 in items else "No")
# e) add 121 and 321 and print sorted list
items.append(121)
items.append(321)
items = sorted(items)
print("e) Updated sorted list after adding 121 and 321:", items)
