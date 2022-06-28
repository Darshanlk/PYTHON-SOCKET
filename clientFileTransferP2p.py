import socket;

c = socket.socket()

c.connect(("localhost",2200))
name = input("enter your name")
c.send(bytes(name,'utf-8'))

i=0
while True:
    i+=1
    data_Type =c.recv(1024).decode()

    if data_Type == "file":
        f =open(f"TransferFile{i}.txt","w")
        datas = c.recv(5000).decode()
        f.write(datas)
        f.close()
        print("Stuff reciving")
        break
print("Done")


        
    

