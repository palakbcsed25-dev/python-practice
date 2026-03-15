# Program: tuple operations on sold item prices
values_input = input('Enter prices of sold items separated by spaces: ').strip()
if not values_input:
    print('No prices entered. Exiting.')
    raise SystemExit

try:
    prices = tuple(float(x) for x in values_input.split())
except ValueError:
    print('Invalid input: please enter numbers separated by spaces.')
    raise SystemExit

# a) total number of items sold
print('Total items sold:', len(prices))

# b) cheapest item price
print('Cheapest item price:', min(prices))

# c) costliest item price
print('Costliest item price:', max(prices))

# d) price list in ascending order
print('Ascending price list:', tuple(sorted(prices)))

# e) count of costliest items sold
costliest = max(prices)
print('Number of costliest items sold:', prices.count(costliest))
