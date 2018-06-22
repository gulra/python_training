#!/usr/bin/python

print '------------------------------------Integer to octal and hexadecimal convertion-------------------------------'
while (True):
        try:
                num = int(input ('\nEnter the integer value: \t\t'))
                break
        except:
                print 'Please enter the INTEGER value'

print '\nThe given integer number is \t\t',num
print 'The equivalent octal format is \t\t', oct(num)
print 'The equivalent hexadecimal value is \t', hex(num)
