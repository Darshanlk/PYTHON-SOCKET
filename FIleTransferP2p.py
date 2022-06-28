import socket
import time

s = socket.socket()

s.bind(("192.168.120.130",9000))

s.listen(3)
print("waiting for connection ...")
time.sleep(2)
print("...")
time.sleep(2)


def choice(client_name):
    ask = input(f"anything serve to {client_name}.[Y/n]")
    if ask == "Y":
        stuff, stuff_type = input(
            f"Enter Stuff Path with Name:."), input(f"Enter Stuff Type:.")
        f = open(stuff, 'r')
        datas = f.read(5000)
        f.close()
        return [datas, stuff_type]
    else:
        print("ok !not sending any stuff")
        return [None, None]


data = []
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print(f"server connected to with client {name} at {addr}")

    data = choice(name)
    _type = data[1]
    _data = data[0]
    c.send(bytes(_type, "utf-8"))
    c.send(bytes(_data, "utf-8"))

    recive_Stuff = c.recv(1024).decode()
    print(recive_Stuff)
    c.close()
