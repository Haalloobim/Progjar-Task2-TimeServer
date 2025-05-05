import sys
import socket
import logging
import threading
import time


def kirim_data(nama="kosong"):
    logging.warning(f"[THREAD-{nama}] Starting client thread")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 45000)  # Update port to 45000
    logging.warning(f"[THREAD-{nama}] Connecting to {server_address}")
    sock.connect(server_address)

    try:
        # Send TIME request
        message = "TIME\r\n"
        logging.warning(f"[THREAD-{nama}] Sending: {message.strip()}")
        sock.sendall(message.encode())

        # Receive response
        data = sock.recv(1024)
        logging.warning(f"[THREAD-{nama}] Received: {data.decode().strip()}")

        # Optional: Send QUIT to close the connection gracefully
        quit_message = "QUIT\r\n"
        logging.warning(f"[THREAD-{nama}] Sending: {quit_message.strip()}")
        sock.sendall(quit_message.encode())

    finally:
        logging.warning(f"[THREAD-{nama}] Closing socket")
        sock.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
    threads = []
    for i in range(3):  # Create 3 concurrent clients
        t = threading.Thread(target=kirim_data, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()