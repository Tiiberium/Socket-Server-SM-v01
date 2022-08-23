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
    MSG = ('01KEEPALIVE \x04'.encode() + '01READTICKET00001210 \x04'.encode());
    MSG2 = ('01MESSAGE   WAIT MATHA FAKA \x04'.encode() + '01RESPONSE  1200220bioПРЭВЭД МЭДВЭД \x04'.encode())
    if not data:
        break
    conn.send(MSG);
    conn.send(MSG2);
    print (MSG);
    print (MSG2)
conn.close()
