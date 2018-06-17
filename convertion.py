#!/usr/bin/python

print 'Convertion of a integer value into different type of data types'

while (True):
	try:
		num=int(raw_input('\nEnter the number \t\t\t: '))
		break
	except:
		print '\nPlease Enter the intger number'


print 'The given number in integer\t\t:',int(num)
print 'The given number in float\t\t:',float(num)
print 'The given number in octal\t\t:',oct(num)
print 'The given number in hex\t\t\t:',hex(num)
print 'The given number in string format\t:', str(num)

