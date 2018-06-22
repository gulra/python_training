#!/usr/bin/python

print '-------------------------------------------------------Case convertion---------------------------------------------------------'

given_string = str(raw_input ('\nEnter a string : \t'))

count = given_string.isalpha();

if count is True:
	print '\nThe given string is case converted as follows\n\n', given_string.swapcase()
else:
	print '\nPlease Enter a string value'
