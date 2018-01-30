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
while row <= arrow_head_width: #outer loop for lines
    while col <= counter: #inner loop for columns. Prints widest part first, then decrements
        print('*', end='')
        col += 1 #print up to counter times
    print() #start new line
    col = 1 #set col back to 1 to let inner loop start as TRUE
    counter -= 1 #decrement counter for each new line, so that an angle is drawn
    row += 1 #print new line until arrow_head_width is met