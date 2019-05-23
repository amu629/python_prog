#!/usr/bin/python

import commands

#Before using this , we need to have sshpass package installed .
users_choice=input('Press 1 if you want to install the sshpass package else press 0 ')
if users_choice==1:
	commands.getoutput('yum install sshpass -y')

#Providing a GUI environment on your OS .
ip=raw_input('Enter the ip address ')
password=raw_input('Enter the password ')
software=raw_input('Enter the software you want to use ')
print commands.getoutput('sshpass -p '+password+' ssh -o StrictHostKeyChecking=no -X '+ip+' '+software)  
