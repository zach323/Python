print('Enter arrow base height: ')
arrow_base_height = int(input())

print('Enter arrow base width: ')
arrow_base_width = int(input())

print('Enter arrow head width: ')
arrow_head_width = int(input())

while arrow_head_width <= arrow_base_width:
    print('Enter arrow head width: ')
    arrow_head_width = int(input())

row = 1
col = 1
while row <= arrow_base_height:
    while col <= arrow_base_width:
        print('*', end='')
        col += 1
    print()
    row += 1
    col = 1

counter = arrow_head_width  # needed third variable to decrement on inner loop
row = 1
col = 1
while row <= arrow_head_width:
    while col <= counter:
        print('*', end='')
        col += 1
    print()
    col = 1
    counter -= 1
    row += 1