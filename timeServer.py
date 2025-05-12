from socket import *
import socket
import threading
import logging
from datetime import datetime

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        try:
            while True:
                data = self.connection.recv(1024)
                if not data:
                    break
                decoded_data = data.decode().strip()
                logging.warning(f"Request from {self.address}: {decoded_data}")

                if decoded_data.startswith("TIME"):
                    now = datetime.now()
                    waktu = now.strftime("%d %m %Y %H:%M:%S")
                    response = f"JAM {waktu}\r\n"
                    logging.warning(f"Sending response with -> {response}")
                    self.connection.sendall(response.encode())

                elif decoded_data == "QUIT":
                    logging.warning(f"Connection closed by client {self.address}")
                    break

                else:
                    response = "ERROR Invalid command\r\n"
                    self.connection.sendall(response.encode())

        except Exception as e:
            logging.error(f"Exception: {e}")
        finally:
            self.connection.close()

class Server(threading.Thread):
    def __init__(self, port=45000):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', self.port))
        self.my_socket.listen(5)
        logging.warning(f"Server listening on port {self.port}")

        while True:
            connection, client_address = self.my_socket.accept()
            logging.warning(f"Accepted connection from {client_address}")

            clt = ProcessTheClient(connection, client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
    svr = Server()
    svr.start()

if __name__ == "__main__":
    main()