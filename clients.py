import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = "10.95.231.111"
port = 9999

s.connect((host,port))

msg = s.recv(1024)

s.close()

print(msg.decode('ascii'))