#!/usr/bin/python

print '------------------------------------Integer to octal and hexadecimal convertion-------------------------------'
while (True):
        try:
                num = int(input ('\nEnter the integer value: \t\t'))
                break
        except:
                print 'Please enter the INTEGER value'
num_int = int(num)

print '\nThe given integer number is \t\t',num
print 'The equivalent octal format is \t\t', oct(num_int)
print 'The equivalent hexadecimal value is \t', hex(num_int)
