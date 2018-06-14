#!/usr/bin/python

while(True):
	try:
		num = int(raw_input('Enter the number to checked: '))
		break
	except:
		print('Please enter the integer')
if (num % 2) is 0:
	print('The given number %d is an even number' % num)
else:
	print('The given number is an odd number')
