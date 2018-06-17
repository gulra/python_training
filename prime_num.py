#!/usr/bin/python

print'\n--------------------------------------Prime Number-----------------------------------------'

while (True):
	try:
		start_num = input('Enter the starting range number : ')
		end_num = input('Enter the ending range number : ')
		break
	except:
		print 'Please enter a valid intger number'

print('\nThe Prime number(s) inbetween the range are/is \n')

for num in range(start_num,end_num):
	for multi_1 in range(2,num):
		if num% multi_1 == 0:
			multi_2 = (num / multi_1)
			break
	else:
		print num	
