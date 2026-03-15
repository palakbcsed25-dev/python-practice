# Program: tuple operations with user-entered integers
values_input = input('Enter integers separated by spaces: ').strip()
if not values_input:
    print('No integers entered. Exiting.')
    raise SystemExit

try:
    ints = [int(x) for x in values_input.split()]
except ValueError:
    print('Invalid input: please enter only integers separated by spaces.')
    raise SystemExit

values = tuple(ints)

# a) Total number of items
print('Total items:', len(values))

# b) Last item
print('Last item:', values[-1])

# c) Tuple elements in reverse order
print('Reversed tuple:', values[::-1])

# d) Contains integer 5?
print('Yes' if 5 in values else 'No')

# e) Remove first and last, sort remaining
if len(values) <= 2:
    print('Not enough items to remove first and last and sort remaining.')
else:
    middle = list(values[1:-1])
    middle.sort()
    print('Remaining sorted after removing first and last:', tuple(middle))
