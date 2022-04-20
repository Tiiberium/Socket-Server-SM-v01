import socket
from _thread import start_new_thread
import time

def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print ('Отключение в: ', timez);
            print('Bye')
            break
        c.send(data)
    c.close()
 
host = ""
port = 4242
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
while True:
    sock, addr = s.accept()
    timez = format(int(time.time()))
    MSG = ('01KEEPALIVE'.encode());
    MSG2 = ('02MESSAGE TEST SHOW'.encode())
    sock.send(MSG);
    sock.send(MSG2);
    print ('Отправлено: ', MSG);
    print ('Текущее время: ', timez);
    print('Connected to :', addr[0], ':', addr[1])
    print ('Полученная информация: ', sock, addr);
    start_new_thread(threaded, (sock,))
