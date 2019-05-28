#!/use/bin/python

#Sender's Code

import socket

#To call The Socket Object
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Specifying receivers receiving port
ip_port=("127.0.0.1",9090)

#Specifying senders receiving port
ip_ports=("127.0.0.1",9000)
s.bind(ip_ports)
buffer_size=100

i=1
while i<12:
	msg=raw_input("Enter Your MESSAGE : ")
	s.sendto(msg,ip_port)
	rec_data=s.recvfrom(buffer_size)
	print rec_data[0]
	i+=1
print "connection ended"
s.close()
