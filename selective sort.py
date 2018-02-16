list = [5, 44, 2, 15, 1, 20, 83, 0, 100, -1, 23, 77, 2004, 8877]
pos = 0
k = 0
for num in range(len(list)):
    min = list[num] #set new mininum after every loop execution
    print('New starting point is {}'.format(min))
    for i in range(num + 1, len(list)): #compare current minimum to all numbers in list, and start at index after minimum
        if list[i] < min: #if list[i] is less than the current minimum, set min = list[i]
            min = list[i]
            tmp = list[num] #holds old minimum
            list[num] = list[i] #place new minimum in place of old minimum
            list[i] = tmp #set current pos in inner loop to old minimum
            print(list)

#loop looks like this visually:
# square bracket indicates current minimum
# |[[5]|, 44, 2, 15, 1, 20, 83, 0]
# |[[2]|, 44, 5, 15, 1, 20, 83, 0]
#...|[[0]|, 44, 2, 15, 1, 20, 83, 1]
#[[0], |44|, 2, 15, 1, 20, 83, 0]
