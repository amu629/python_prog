#!/usr/bin/python

import commands

d_name=raw_input('enter the name of the drive ')
d_size=raw_input('enter the size of the drive ')

#Creating an LV with the name and size provided by the user 
commands.getoutput('lvcreate --name '+d_name+' --size '+d_size+' vg')

#Formating the raw drive and Creating a directory (same as that of LV name) where the user wants to mount the drive 
commands.getoutput('mkfs.xfs /dev/vg/'+d_name+';mkdir /mnt/'+d_name)

#Mounting the LV to the directory
commands.getoutput('mount /dev/vg/'+d_name+' /mnt/'+d_name)

#IF user wants to create the LV permanently
y=input('Press 1 if you want to create permanent LV ')
msg='/dev/vg/'+d_name+'		/mnt/'+d_name+'		xfs	defaults	0	0\n'
if(y==1):
	f=open('/etc/fstab','a')
	f.write(msg)
	f.close()


 
