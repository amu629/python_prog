#!/usr/bin/python

import commands,getpass

a=raw_input('Username ')
b=getpass.getpass('Password ')

print commands.getoutput('useradd '+a)
print commands.getoutput('(echo '+b+';echo '+b+') | passwd '+a)



