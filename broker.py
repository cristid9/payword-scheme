import socket

if __name__ == "__main__":
    host = socket.gethostname()
    port = 2401
    BUFFER_SIZE = 512
    MESSAGE = input("Mesaj broker:")




    tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClientA.connect((host, port))

    while MESSAGE != 'stop':
        tcpClientA.send(MESSAGE.encode())
        data = tcpClientA.recv(BUFFER_SIZE)
        print("Broker a primit:", data)
        MESSAGE = input("Mesaj broker:")

    tcpClientA.close()
