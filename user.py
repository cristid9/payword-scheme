import socket
import threading
import time
import sys

from User import User


host = socket.gethostname()
port = 2401
VANZATOR_PORT = 2402
BUFFER_SIZE = 512
ERROR = "cont_invalid"


def client_server_thread():
    """
    This thread handles the communication between the user and the bank.
    """
    id_user = input("Insert user id: ")
    password = input("Insert user password: ")

    u = User(id_user, password)  # modify later, timestamp invalid

    tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClientB.connect((host, port))
    tcpClientB.send(
        (u.id + "-" + str(u.password) + "-" + str(u.signing_key)).encode())

    bank_validation_message = tcpClientB.recv(BUFFER_SIZE)
    if bank_validation_message == ERROR:
        print(ERROR)
        tcpClientB.close()
        sys.exit(-1)
    else:
        certificate = bank_validation_message
        print(certificate.decode())


    # while MESSAGE != 'stop':
    #     tcpClientB.send(MESSAGE.encode())
    #     data = tcpClientB.recv(BUFFER_SIZE)
    #     print("User a primit:", data)
    #     MESSAGE = input("Mesaj user:")

    tcpClientB.close()


def client_vanzator_thread():
    """
    Handles the communication between the user and the vanzator.
    """
    vanzator_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    vanzator_client.connect((host, VANZATOR_PORT))
    vanzator_client.send("yaso vanzatorule".encode())

    MESSAGE = "nustop"

    # while MESSAGE != 'stop':
    vanzator_client.send("ana".encode())
    data = vanzator_client.recv(BUFFER_SIZE)
    print("[Client vanzator thread] User a primit:", data)
    # time.sleep(5)

    vanzator_client.close()


if __name__ == "__main__":
    t1 = threading.Thread(target=client_server_thread)
    t2 = threading.Thread(target=client_vanzator_thread)

    t1.start()
    t2.start()
