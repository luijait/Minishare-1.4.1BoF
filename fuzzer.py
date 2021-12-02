import socket
import sys
from time import sleep
try:
    host = sys.argv[1]
    puerto = sys.argv[2]
except:
    print ("[*]USO {} <Direccion IP> <Puerto> ").format(sys.argv[0])
    sys.exit()
   
        
if __name__ == "__main__":
    bytes_fuzz = input("Introduce el numero de bytes con los que quieres empezar a fuzzear: ")
    max_buff = input("Introduce el numero de bytes en los que quieres que se pare el fuzzing: ")
    iteracion = input("Introduce el numero de bytes que quieres que se sume al buffer por iteracion: ")
    while bytes_fuzz < max_buff:
        try:
            buffer = "GET " + bytes_fuzz * 'A' + " HTTP/1.1\r\n\r\n"
            bytes_fuzz = bytes_fuzz + iteracion
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,int(puerto)))
            print "Fuzzeando con %s bytes: "  % bytes_fuzz
            s.send(buffer)
            s.close()
            sleep(3)
        except:
            print "El programa ha craseado con %s bytes" % bytes_fuzz
            sys.exit()    