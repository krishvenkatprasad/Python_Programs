# This program takes two IP address as command line arguments.
# The program finds the Host name for the first IP address and for the second IP address it will check whether we get positive or negative result when we ping the IP address

import socket
import os
import sys
ip1 = sys.argv[1]
ip2 = sys.argv[2]
try:
	ais = socket.gethostbyaddr(ip1)
	pin = os.system('ping -c 1 '+ip2)
except:
	print('Exception Raised')
if pin==0:
	status = 'UP'
else:
	status = 'DOWN'
print("--------------------------------------")
print("IP Address = "+ip1)
print("Hostname = "+ais[0])
print("--------------------------------------")
print("IP Address = "+ip2)
print("Status = "+status)
print("--------------------------------------")