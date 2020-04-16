import socket
import time
import os
import sys
from tqdm.auto import tqdm
host = input("Enter Address to Connect\n")
try:
    port = int(1234)
except ValueError:
    print("Error. Exiting. Please enter a valid port number.")
    sys.exit()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Receiver socket initialized")
    s.setblocking(0)
    s.settimeout(15)
except socket.error:
    print("Failed to create socket")
    sys.exit()
while True:
    command = input("\nPlease enter a command: \n1. put filename\n2. get file_name\n3. list\n4. delete file_name\n5. exit\n ")
    CommClient = command.encode('utf-8')
    try:
        s.sendto(CommClient, (host, port))
    except ConnectionResetError:
        print("Error. Port numbers are not matching. Exiting. Next time please enter same port numbers.")
        sys.exit()
    CL = command.split()
    if CL[0]=='list':
        os.system('cls')            
        print('Checking for acknowledgement\n')
        clientDatal,clientAddrl=s.recvfrom(4096)
        text=clientDatal.decode('utf-8')
        print(text)
    elif CL[0]=='get':
        os.system('cls')
        exist,clientaAddr=s.recvfrom(51200)
        isexist=exist.decode('utf-8')
        if isexist=='True':
            f = open(CL[1], "wb")
            d = 0
            Count, countaddress = s.recvfrom(4096)
            point = Count.decode('utf8')
            pointer = int(point)
            print("Receiving packets will start now if file exists.")
            while pointer != 0:
                data, clientbAddr = s.recvfrom(4096)
                datas=f.write(data)
                d += 1
                print("Received packet number:" + str(d))
                pointer -= 1
            f.close()
            print("File received successfully")
        else:
            print("Error:File does not exist in server diractory")
    elif CL[0]=='put':
        os.system('cls')
        path="C:/Users/Dakshit/Desktop/file/client"
        exist=str(os.path.isfile(CL[1]))
        existen=exist.encode('utf-8')
        s.sendto(existen,(host,port))
        if os.path.isfile(CL[1]):
            c=0
            size=os.stat(CL[1])
            sizeS=size.st_size
            num=int(sizeS/4096)+1
            nums=str(num)
            numen=nums.encode('utf-8')
            s.sendto(numen,(host, port))
            f=open(CL[1],'rb')
            while num !=0:
                data=f.read(4096)
                s.sendto(data,(host,port))
                c+=1
                num-=1
                print("packet number:"+str(c))
            f.close()
            print("File Send Successfully")
    elif CL[0]=='delete':
        os.system('cls')
        exist,clientaAddr=s.recvfrom(51200)
        isexist=exist.decode('utf-8')
        if isexist=='True':
            print("File deleted Succsessfully")
        else:
            print("File does not Exist")
            
        
        
    elif CL[0]=='exit':
        os.system('cls')
        print("Programm Ends Here")
        sys.exit()

else:
    print("Error. Exiting. Please enter a valid process\n.")
    sys.exit()
    
    
        
    
        
