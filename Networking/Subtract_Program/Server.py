import socket
HOST = '127.0.0.1'
PORT = 10102
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	s.settimeout(10)
	conn,addr = s.accept()
	with conn:
		print('Connected by: ',addr)
		conn.sendall(b'Enter the subtraction in the form of A - B\n')
		rec = conn.recv(1024)
		data = rec.split()
		op1 =int(data[0])
		op2 = int(data[2])
		ans = str(op1 - op2)
		print("The answer is "+ans)
		fn_ans = ('Subtraction is '+ans).encode('utf-8')
		conn.sendall(fn_ans)
		s.close()