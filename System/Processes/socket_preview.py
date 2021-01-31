from socket import socket, AF_INET, SOCK_STREAM # portable socket api

port = 50008
host = 'localhost'

def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('',port))
    sock.listen(5)  # allow up to 5 pending clients
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024) # read bytes data from this client
        reply = 'server got: [%s]' % data   # connis a new connect socket
        conn.send(reply.encode())       # send bytes reply back to client

def client(name):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect((host,port))   # connect to a socket port
    sock.send(name.encode())    
    reply = sock.recv(1024)    
    sock.close()
    print('client got: [%s]' % reply)

if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True
    sthread.start()
    for i in range(5):
        Thread(target=client,args=('client%s' % i,)).start()
    
