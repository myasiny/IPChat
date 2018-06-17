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
            data = conn.recv(1024).decode("utf-16")
            if data:
                # conn.sendall(data.encode())
                print("{sender} (TCP) sent a message:\n{msg}".format(sender=addr[0], msg=data))
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
                print("{sender} (UDP) sent a message:\n{msg}".format(sender=addr[0], msg=data.decode("utf-16")))
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
            data = conn.recv(1024).decode("utf-16")
            if data:
                file = open("recv/from_%s.%s" % (addr[0].replace(".", "-"), data), "wb")
                while 1:
                    try:
                        file.write(conn.recv(1024))
                    except:
                        break
                print("{sender} (TCP) sent a file: ...{msg}".format(sender=addr[0], msg=data))
                file.close()

class UDP_File(threading.Thread):
    def run(self):
        self.file()

    @staticmethod
    def file():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 8888))
        sock.settimeout(2)

        while 1:
            try:
                data, addr = sock.recvfrom(1024)
                if data:
                    file = open("recv/from_%s.%s" % (addr[0].replace(".", "-"), data.decode("utf-16")), "wb")
                    while 1:
                        try:
                            chunk, addr = sock.recvfrom(1024)
                            file.write(chunk)
                        except:
                            break
                    print("{sender} (UDP) sent a file: ...{msg}".format(sender=addr[0], msg=data.decode("utf-16")))
                    file.close()
            except:
                pass

if __name__ == "__main__":
    server = [TCP_Text(), TCP_File(), UDP_Text(), UDP_File()]
    for thread in server:
        thread.start()