#!/usr/bin/python2

import commands

d_name= raw_input('enter the drive you want to detach: ')

#unmounting the drive
commands.getoutput('umount /mnt/'+d_name)

#deleting the directory under /mnt
commands.getoutput('rmdir /mnt/'+d_name)

#removing the lv associated
commands.getoutput('lvremove -f /dev/vg/'+d_name)

#updating entry offstab file
f=open('/etc/fstab','r+')
lines=f.readlines();
f.close()

f=open('/etc/fstab','w')
for line in lines:
	word = line.split()
	if len(word)==0:
		f.write('\n')
		continue
	if word[0] != '/dev/vg/'+d_name:
		f.write(line)
f.close()
