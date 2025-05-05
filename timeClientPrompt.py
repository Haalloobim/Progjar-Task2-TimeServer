import sys
import socket
import logging
import threading

def kirim_data(command, nama="Client"):
    logging.warning(f"[{nama}] Starting client")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 45000)
    logging.warning(f"[{nama}] Connecting to {server_address}")
    sock.connect(server_address)

    try:
        # Send initial command
        message = f"{command}\r\n"
        logging.warning(f"[{nama}] Sending: {command}")
        sock.sendall(message.encode())

        # Receive response from server
        data = sock.recv(1024)
        logging.warning(f"[{nama}] Received: {data.decode().strip()}")

        # If the initial command wasn't QUIT, ask whether to send QUIT next
        if command.upper() != "QUIT":
            quit_message = "QUIT\r\n"
            logging.warning(f"[{nama}] Sending: QUIT")
            sock.sendall(quit_message.encode())

            # Receive the response to QUIT
            data = sock.recv(1024)
            logging.warning(f"[{nama}] Received after QUIT: {data.decode().strip()}")

    finally:
        logging.warning(f"[{nama}] Closing socket")
        sock.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

    threads = []

    for i in range(3):
        cmd = input(f"Enter command for client {i} (TIME, QUIT, or anything else): ").strip().upper()
        if not cmd:
            continue

        t = threading.Thread(target=kirim_data, args=(cmd, f"Client-{i}"))
        threads.append(t)

    for thr in threads:
        thr.start()

    for thr in threads:
        thr.join()  # Optional: Wait for all threads to complete before exiting
