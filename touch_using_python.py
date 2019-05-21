#!/usr/bin/python

import sys

v=sys.argv
for i in v[1:]:
	f=open('/root/'+i,'w')
	f.close()
