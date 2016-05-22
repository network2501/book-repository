#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


from sys import argv

script, user_name, code_name = argv
prompt = '%'

print "Hi, %s, I'm the %s script," % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "%s kind of computer do you have?" % code_name
computer = raw_input(prompt)

print "%r happens when you get happy?" % code_name
happy = raw_input(prompt)

print """
Alright, so you have said %s about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
You must be really %r.
""" % (likes, lives, computer, happy)

