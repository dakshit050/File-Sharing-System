import socket
import time
import os
import sys
from tqdm.auto import tqdm

#host="localhost"
port=(int(1234))
def ServerExit():
    print("Client is no longer exist")
    s.close() 
    sys.exit()


def ServerList():
    print("In sender,list function")
    F=os.listdir(path="C:/Users/Dakshit/Desktop/file/server")
    Lists=[]
    for file in F:
        Lists.append(file)
    Liststr=str(Lists)
    ListsEn=Liststr.encode('utf-8')
    s.sendto(ListsEn,clientAddr)
    print("List send From sender")

def ServerGet(g):
    print("Sending Acknowledgment of command.")
    exist=str(os.path.isfile(g))
    existen=exist.encode('utf-8')
    s.sendto(existen,clientAddr)
    if os.path.isfile(g):
        c = 0
        sizeS = os.stat(g)
        sizeSS = sizeS.st_size
        print("File size in bytes:" + str(sizeSS))
        NumS = int(sizeSS / 4096)+1
        tillSS = str(NumS)
        tillSSS = tillSS.encode('utf8')
        s.sendto(tillSSS, clientAddr)
        check = int(NumS)
        f = open(g, "rb")
        while check != 0:
            data = f.read(4096)
            s.sendto(data, clientAddr)
            c += 1
            check -= 1
            print("Packet number:" + str(c))
        f.close()
        print("File send successfully")
    else:
        print("Error: File does not exist in Server directory.")
def ServerPut(g):
    exist,clientaAddr=s.recvfrom(51200)
    isexist=exist.decode('utf-8')
    if isexist=='True':
        c=0
        size,clientAddr=s.recvfrom(4096)
        sizes=size.decode('utf-8')
        count=int(sizes)
        f=open(g,'wb')
        while count!=0:
            data,dataAddr=s.recvfrom(4096)
            datas=f.write(data)
            c+=1
            print("Received packet number:"+str(c))
            count-=1
        f.close()
        print("Received Successfully")
    else:
        print("File Does not Exist")
def ServerDelete(g):
    print("Sending Acknowledgment of command.")
    exist=str(os.path.isfile(g))
    existen=exist.encode('utf-8')
    s.sendto(existen,clientAddr)
    if os.path.isfile(g):
        os.remove(g)
        print("File deteled Successfully")
    else:
        print("Error:File does not Exist")
    
    
    
    
    
        
try:
    hostname = socket.gethostname()    
    host = socket.gethostbyname(hostname)
    print("Share Address with your friend To connect:"+host)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Sender socket initialized")
    s.bind((host, port))
except socket.error:
    print("Failed to create socket")
    sys.exit()
while True:
    try:
        data,clientAddr=s.recvfrom(4096)
            
    except ConnectionResetError:
        print("Error. Port numbers not matching. Exiting. Next time enter same port numbers.")
        sys.exit()
    text=data.decode('utf-8')
    t2=text.split()
    if t2[0] == "get":
        os.system('cls')
        ServerGet(t2[1])           
    elif t2[0] == "list":
        os.system('cls')
        ServerList()
    elif t2[0]=='put':
        os.system('cls')
        ServerPut(t2[1])
    elif t2[0]=='delete':
        os.system('clr')
        ServerDelete(t2[1])
    elif t2[0] == "exit":
        os.system('cls')
        ServerExit()

print("Program will end now. ")
quit()
