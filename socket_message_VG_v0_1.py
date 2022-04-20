import socket
import time

sock = socket.socket()
sock.bind(('', 4242))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    timez = format(int(time.time()))
  #  MSG = input().encode()
    print ('Текущее время: ', timez);
    print ('Полученная информация: ', conn, addr);
    MSG = ('01KEEPALIVE \x04'.encode() + '01MESSAGE   Try Again \x04'.encode())
    if not data:
        break
    conn.send(MSG);
    print (MSG)
def entmsg():
    print ('введите сообщщение:')
conn.close()
