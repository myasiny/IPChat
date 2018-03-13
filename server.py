import socket, threading

class TCP_Text(threading.Thread):
    def run(self):
        self.text()

    @staticmethod
    def text():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", 8887))
        sock.listen(2)

        while 1:
            conn, addr = sock.accept()
            data = conn.recv(1024).decode()
            if data:
                # conn.sendall(data.encode())
                pass

class UDP_Text(threading.Thread):
    def run(self):
        self.text()

    @staticmethod
    def text():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 8887))

        while 1:
            data, addr = sock.recvfrom(1024)
            if data:
                # sock.sendto(data, addr)
                pass

class TCP_File(threading.Thread):
    def run(self):
        self.file()

    @staticmethod
    def file():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", 8888))
        sock.listen(2)

        while 1:
            conn, addr = sock.accept()
            data = conn.recv(1024).decode()
            if data:
                file = open("recv/from_%s.%s" % (addr[0].replace(".", "-"), data), "wb")
                while 1:
                    try:
                        file.write(conn.recv(1024))
                    except:
                        break
                file.close()

class UDP_File(threading.Thread):
    def run(self):  # TODO: Receive file
        self.file()

    @staticmethod
    def file():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 8888))

        while 1:
            try:
                data, addr = sock.recvfrom(1024)
                if data:
                    file = open("recv/from_%s.%s" % (addr[0].replace(".", "-"), data.decode("utf-8")), "wb")
                    while 1:
                        try:
                            sock.settimeout(2)
                            chunk, addr = sock.recvfrom(1024)
                            file.write(chunk)
                        except:
                            break
                    file.close()
            except:
                pass

if __name__ == "__main__":
    TCP_Text().start()
    UDP_Text().start()
    TCP_File().start()
    UDP_File().start()