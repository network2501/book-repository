#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# r   String (converts any python object using repr()), The repr module provides
# a means for producing object representations with limits on the size of the
# resulting strings. This is used in the Python debugger and may be useful in
# other contexts as well. https://docs.python.org/2/library/repr.html
# print any python object using repr
formatter = "%r %r %r %r"

# print the variable formatter which is four repr strings to evaluate the
# intergers using the repr function
print formatter % (1, 2, 3, 4)
# print the variable formatter which is four repr strings to evaluate the
# four strings using the repr function
print formatter % ("one", "two", "three", "four")
# print the variable formatter whcih is four repr strings to evaluate the
# Booleans using repr
print formatter % (True, False, False, True)
# print the variable formatter which is four repr strings to print four %r for
# each variable listed. So print "%r %r %r %r" for each time formatter is
# listed in
print formatter % (formatter, formatter, formatter, formatter)
# print the variable formatter using the four strings which are on new lines but
# still act as one line thanks to ,
print formatter %( 
        "I had this thing,",
        "That you could type up right.",
        "But it didn't sing.",
        "So i said goodnight"
)
