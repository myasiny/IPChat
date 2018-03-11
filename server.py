import socket, threading

class TCP(threading.Thread):
    def run(self):  # TODO: Receive file
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", 8888))
        sock.listen(2)

        while 1:
            conn, addr = sock.accept()
            data = conn.recv(1024).decode()
            if data:
                # conn.sendall(data.encode())
                pass
        conn.close()

class UDP(threading.Thread):
    def run(self):  # TODO: Receive file and text
        pass

if __name__ == "__main__":
    TCP().start()
    UDP().start()