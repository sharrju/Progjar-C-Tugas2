import sys
import socket
import logging



def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.18.0.4', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = "TIME\r\n".encode()
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message)
        # Look for the response
        data = sock.recv(32)
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    kirim_data()