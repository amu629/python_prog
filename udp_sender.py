#!/use/bin/python

#Sender's Code

import socket

#To call The Socket Object
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Specifying IP and Port of receiver
ip_port=("127.0.0.1",9090)

i=1
while i<12:
	msg=raw_input("Enter Your MESSAGE : ")
	s.sendto(msg,ip_port)
	i+=1
print "connection ended"

