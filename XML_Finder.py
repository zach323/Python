fhand = open('C:\\Users\\zrebstock\\Documents\\python_linear_search.txt')

import time
str  = input('Enter string you would like to locate: ') #string to be located in file
start = time.time()
delta_time = 0

def find(str):
	time.sleep(0.01)
	found_str ='' #initialize placeholder for found string
	next_index = 0 #index for comparison checking
	line_count = 1
	
	for line in fhand: #each line in file
		line_count = line_count +1
		for letter in line: #each letter in line
			if letter == str[next_index]: #compare current letter index to beginning index of string you want to find
				
				found_str += letter #if a match, concatenate to string placeholder
					
			
				#print(found_str) #print for visualization of inline search per iteration
				next_index = next_index + 1
				

			
				if found_str == str: #if complete match is found, break out of loop.
					
					print('Result is: ', found_str, ' on line %s '%(line_count))
					print (line)
					return found_str #return string to function caller
					break
			else:
				#if a match was found but the next_index match was False, reset the indexes and try again.
				next_index=0 # reset indext back to zero
			
				found_str = '' #reset string back to empty
				
		if found_str == str:
			print(line)
		
if str != "":	
	result = find(str)
	delta_time = time.time() - start

	print(result)
	print('Seconds elapsed: ', delta_time)	
	
else:
	print('sorry, empty string')

			
		
		


