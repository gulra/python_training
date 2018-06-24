#!/usr/bin/python

inp = str(raw_input ('Enter the list value seperated by space (eg: python training) : '))

inp_li = inp.split();
print 'The given list is\n', inp_li

inp_li.sort()
print '\nThe given list in sorted format is\n', inp_li

inp_li.reverse();
print '\nThe given list in reverse sorted format is\n',inp_li
