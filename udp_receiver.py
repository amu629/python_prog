#!/usr/bin/python

# Receiver's Code
import socket

# To call the socket Object
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Specifying IP and Port of receiver
ip_port=("127.0.0.1",9090) #receiver's ip & port

#Opening Connection
s.bind(ip_port)

Buffer_Size=100

i=1
while i<12:
	rec_data=s.recvfrom(Buffer_Size)
	print rec_data
	i+=1
print 'connection closed'
s.close()
