#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 2.54 * 74 # centimeters
weight = 0.45 * 180 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %f centimeters tall." % height
print "He's %f kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is stricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# study drill 1, used vim :%s/my_//g to remove all my_ prepends.
# study drill 2, used python math to edit height and weight variables
# study drill 3,  
#		Conversion  Meaning     Notes
#		d   Signed integer decimal.     
#		i   Signed integer decimal.     
#		o   Unsigned octal.     (1)
#		u   Unsigned decimal.   
#		x   Unsigned hexadecimal (lowercase).   (2)
#		X   Unsigned hexadecimal (uppercase).   (2)
#		e   Floating point exponential format (lowercase). 
#                   - Hes 1.879600e+02 centimeters tall.
#                   - He's 8.100000e+01 kilograms heavy.
#		E   Floating point exponential format (uppercase).  
#		f   Floating point decimal format. 
#                   - He's 187.960000 centimeters tall.
#                   - He's 81.000000 kilograms heavy.
#		F   Floating point decimal format.  
#		g   Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.   
#		G   Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.   
#		c   Single character (accepts integer or single character string).  
#		r   String (converts any python object using repr()).   (3)
#		s   String (converts any python object using str()).    (4)
#		%   No argument is converted, results in a "%" character in the result.
