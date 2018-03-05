import socket
from threading import Thread
from Bank import Bank

# The bank
TCP_IP = '0.0.0.0'
TCP_PORT = 2401
BUFFER_SIZE = 512
BANK_ID = 'BRD_SUPER_COPOU'
ERROR = 'cont_invalid'

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.conn = conn
        self.port = port

    def run(self):
        # while True:
        #     data = self.conn.recv(512)
        #     print("Server a primit:", data)
        #     MESSAGE = str(ip)
        #     if MESSAGE == 'stop':
        #         break
        #     self.conn.send(MESSAGE.encode())
        data = self.conn.recv(512)
        print(data)
        user_id, password, signing_key = data.decode().split('-')
        # check user existence in database
        self.bank = Bank(BANK_ID)
        if user_id[0].lower() == 'u':
            if self.bank.query_user(user_id, password) != -1:
                certificate = self.bank.genererate_digital_signature(user_id, password, signing_key)
                print(str(certificate))
                self.conn.send(str(certificate).encode())
            else:
                self.conn.send(ERROR.encode())


if __name__ == "__main__":

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServer.bind((TCP_IP, TCP_PORT))
    threads = []

    while True:
        tcpServer.listen(5)
        (conn, (ip, port)) = tcpServer.accept()
        newthread = ClientThread(ip, port, conn)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()
