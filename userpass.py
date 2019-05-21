#!/usr/bin/python

import commands

a=raw_input('Username ')
b=raw_input('Password ')

print commands.getoutput('adduser '+a)
print commands.getoutput('(echo '+b+';echo '+b+') | passwd '+a)


