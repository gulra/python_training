#!/usr/bin/python

length_str = str(raw_input('Enter the String: '))

part_str = str(raw_input('Enter the sub string to be searched: '))

count = length_str.find(part_str)

if count is -1:
	print 'The given substring is not present'
else:
	print 'The given substring is present in the main string'
