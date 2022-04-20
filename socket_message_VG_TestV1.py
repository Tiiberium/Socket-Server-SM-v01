import socket, string
import time


HOST = "" # localhost
PORT = 4242
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
while 1:
    print ("Слушаю порт 4242")
    srv.listen(1)
    sock, addr = srv.accept()
    while 1:
        pal = sock.recv(1024)
        if not pal:
            break
        print ("Получено от %s:%s:" % addr, pal)
        lap = input().encode()
        print ("Отправлено %s:%s:" % addr, lap)
        sock.send(lap)
    sock.close()

