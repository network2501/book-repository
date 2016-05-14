#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# new variable, has to start with a alpha not a numeral. This variable is a string with a interger decimal variable.
x = "There are %d types of people." % 10
# the variable binary is the string binary
binary = "binary"
# the variable can't have a space so _ is used. the double quotes are used to allow the use of a ' in the word don't
do_not = "don't"
# %s is a string variable and () are used to define the start finish of multiple variables at the end of a string
## string inside of a string
y = "Those who know %s and those who %s." % (binary, do_not)

# print the variable x
print x
# print the variable y
print y

# print the string and refer to variable x which is listed above which uses a %d variable. For exmaple %r   String (converts any python object using repr()
## STRING inside a string
print "I said: %r." % x
# print the string with a object %s (string) which is referencing a variable ywhcih is a string with multiple object strings
## String inside a string
print "I also said: '%s'." % y

# False is a boolean, hilarious is now a boolean
hilarious = False
# a new varilable with a repr value referencing hilarious i think it must make it a string instead of a boolean
joke_evaluation = "Isn't that joke so funny?! %r"

# as mentioned above this prints the above values and convers them intro strings
##STRING inside a string as the boolean is now evaluated as a string
print joke_evaluation % hilarious 

# a variable that's not beginging with a or a word
w = "This is the left side of..."
# another string variable
e = "a string with a right side."

#this is the concatanation of two strings
print w + e
