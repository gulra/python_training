#!/usr/bin/python
while (True):
	try:
		fir_digit = int(raw_input('Enter the first digit : \t'))
		sec_digit = int(raw_input('Enter the second digit : \t'))
		break
	except:
		print('\t\tPlease enter the integer value')

add = fir_digit + sec_digit
diff = fir_digit - sec_digit
multiply = fir_digit * sec_digit
div = fir_digit / sec_digit

print '\nThe addition value is \t\t', add
print 'The difference value is \t', diff
print 'The multiplied value is \t', multiply
print 'The divident value is \t\t', div
