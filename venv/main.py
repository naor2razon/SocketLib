import socket
import sys

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket sucsses")
except socket.error as err:
    print(f"Socket failed with error:{err}")

port = 80

try:
    host_ip=socket.gethostbyname('www.github.com')
except socket.gaierror:
    print("error resolving the host")
    sys.exit()

s.connect((host_ip,port))
print(f"socket sucsees to connect github with port:{port}")

#ip = socket.gethostbyname('www.github.com')
#print(ip)
