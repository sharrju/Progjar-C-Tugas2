from socket import *
import socket
import threading
import logging
import time
import sys


class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(32)
            if data:
                logging.warning(f"Server is receiving {data} from {self.address}")
                # melakukan perubahan input dari socket yang berbentuk bytes menjadi string
                # untuk melakukan klasifikasi CRLF (karakter 13 dan 10)
                if data.startswith(b'TIME') and data.endswith(b'\r\n'):
                    current_time = time.strftime("%H:%M:%S")
                    response = f"JAM {current_time}\r\n"
                    logging.warning(f"Server is sending {response} to {self.address}")
                    self.connection.sendall(response.encode('utf-8'))
                else:
                    response = "Request is rejected by the server."
                    self.connection.sendall(response.encode('utf-8'))
                    
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0',45000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")
                     
            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)
	

def main():
	svr = Server()
	svr.start()

if __name__=="__main__":
	main()