import sys
import socket
HOST = '127.0.0.1'
PORT = 10102
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	data1 = s.recv(1024)
	ques = (sys.argv[1]+' - '+sys.argv[2]).encode('utf-8')
	s.sendall(ques)
	data = s.recv(1024)
	fin = str(data)
	print(fin)
	s.close()