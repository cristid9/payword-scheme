import socket
import threading

host = socket.gethostname()
VANZATOR_PORT = 2402
bank_port = 2401
BUFFER_SIZE = 512
TCP_IP = '0.0.0.0'


def server_client():
    """
    Handles the communication between the vanzator and the bank (central server).
    """
    MESSAGE = input("Mesaj vanzator:")

    tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClientA.connect((host, bank_port))

    while MESSAGE != 'stop':
        tcpClientA.send(MESSAGE.encode())
        data = tcpClientA.recv(BUFFER_SIZE)
        print("Vanzator a primit:", data)
        MESSAGE = input("Mesaj vanzator:")

    tcpClientA.close()


def user_v_server():
    """
    Opens a TCP server on vanzator's side. The vanzator will act as a server for the user.
    """

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServer.bind((TCP_IP, VANZATOR_PORT))

    tcpServer.listen(1)
    (conn, (ip, port)) = tcpServer.accept()

    while True:
        data = conn.recv(512)
        print("Server vanzator a primit:", data)
        MESSAGE = str(ip)
        if MESSAGE == 'stop':
            break
        conn.send(MESSAGE.encode())


if __name__ == "__main__":
    t1 = threading.Thread(target=server_client)
    t2 = threading.Thread(target=user_v_server)
    t1.start()
    t2.start()

