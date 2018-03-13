import socket
from tkinter import *
from tkinter.filedialog import *

root = Tk()

class Client:
    def __init__(self, port_text, port_file):
        self.port_text = port_text
        self.port_file = port_file

    def on_send_file(self):  # TODO: Send file over UDP
        file = askopenfilename(parent=root)
        path = os.path.expanduser(file)

        if self.box_protocol.get() == "TCP":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.box_ip.get(), self.port_file))
            sock.sendall(path.split(".")[-1].encode())
            file = open(path, "rb")
            while 1:
                chunk = file.read(1024)
                if not chunk:
                    break
                sock.sendall(chunk)
            file.close()
            sock.close()
        else:
            pass

    def on_send_text(self):
        if self.box_protocol.get() == "TCP":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.box_ip.get(), self.port_text))
            sock.sendall(self.box_user_1.get("1.0", END).encode())
            sock.close()

            self.box_user_1.delete("1.0", END)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(self.box_user_1.get("1.0", END).encode(), (self.box_ip.get(), self.port_text))
            sock.close()

            self.box_user_1.delete("1.0", END)

    def gui(self):
        # img_bg = Label(root, image=PhotoImage(file="img\\bg.gif"))
        # img_bg.place(x=0, y=0, relwidth=1, relheight=1)

        top_menu = Menu(root)
        top_menu.add_command(label="Send File", command=self.on_send_file)
        top_menu.add_command(label="Quit", command=root.quit)
        root.config(menu=top_menu)

        txt_header = Label(root, text="I P C h a t", font=("Impact", 12), height=2, bg="dark green", fg="white")
        txt_header.pack(side=TOP, fill=BOTH)

        txt_user_2 = Label(root, text="Your Friend")
        txt_user_2.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.box_user_2 = Text(root, width=50, height=15, state=DISABLED, relief=FLAT, bg="light gray")
        self.box_user_2.place(relx=0.5, rely=0.3, anchor=CENTER)

        divider_1 = Frame(height=2, bd=1, relief=SUNKEN)
        divider_1.pack(fill=X, pady=300)

        txt_user_1 = Label(root, text="You")
        txt_user_1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.box_user_1 = Text(root, width=50, height=15)
        self.box_user_1.place(relx=0.5, rely=0.7, anchor=CENTER)

        divider_2 = Frame(height=2, bd=1, relief=SUNKEN)
        divider_2.pack(fill=X, pady=0)

        self.box_ip = Entry(root)
        self.box_ip.place(relx=0.25, rely=0.9, anchor=CENTER)
        self.box_ip.insert(0, "Destination IP")

        self.box_protocol = Spinbox(root, values=("TCP", "UDP"))
        self.box_protocol.place(relx=0.55, rely=0.9, anchor=CENTER)

        var_emoji = StringVar(root)
        var_emoji.set("Emoji")
        box_emoji = OptionMenu(root, var_emoji, "\u2764")  # TODO: Emojis
        box_emoji.place(relx=0.8, rely=0.9, anchor=CENTER)

        btn_send = Button(root, text="SEND", width=50, command=self.on_send_text)
        btn_send.place(relx=0.5, rely=0.95, anchor=CENTER)

if __name__ == '__main__':
    Client(8887, 8888).gui()
    root.wm_title("IPChat")
    root.geometry("500x750+500+25")
    root.iconbitmap("img\\icon.ico")
    root.resizable(0, 0)
    root.mainloop()