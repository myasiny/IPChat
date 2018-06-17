import socket
from tkinter import *
from tkinter.filedialog import *

root = Tk()

class Client:
    def __init__(self, port_text, port_file):
        self.port_text = port_text
        self.port_file = port_file

    def on_add_emoji(self):
        self.box_user_1.insert(END, self.var_emoji.get())

    def on_send_file(self):
        file = askopenfilename(parent=root)
        path = os.path.expanduser(file)

        if path:
            if self.box_protocol.get() == "TCP":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.box_ip.get(), self.port_file))
                sock.sendall(path.split(".")[-1].encode("utf-16", "surrogatepass"))
                file = open(path, "rb")
                while 1:
                    chunk = file.read(1024)
                    if not chunk:
                        break
                    sock.sendall(chunk)
                file.close()
                sock.close()
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(path.split(".")[-1].encode("utf-16", "surrogatepass"), (self.box_ip.get(), self.port_file))
                file = open(path, "rb")
                while 1:
                    chunk = file.read(1024)
                    if not chunk:
                        break
                    sock.sendto(chunk, (self.box_ip.get(), self.port_file))
                file.close()
                sock.close()

    def on_send_text(self):
        if self.box_user_1.get("1.0", END).strip():
            if self.box_protocol.get() == "TCP":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.box_ip.get(), self.port_text))
                sock.sendall(self.box_user_1.get("1.0", END).encode("utf-16", "surrogatepass"))
                sock.close()

                self.box_user_1.delete("1.0", END)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(self.box_user_1.get("1.0", END).encode("utf-16", "surrogatepass"), (self.box_ip.get(), self.port_text))
                sock.close()

                self.box_user_1.delete("1.0", END)

    def gui(self):
        # self.img_bg = Label(root, image=PhotoImage(file="img\\bg.gif"))
        # self.img_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.top_menu = Menu(root)
        self.top_menu.add_command(label="Send File", command=self.on_send_file)
        self.top_menu.add_command(label="Quit", command=root.quit)
        root.config(menu=self.top_menu)

        self.txt_header = Label(root, text="I P C h a t", font=("Impact", 12), height=2, bg="dark green", fg="white")
        self.txt_header.pack(side=TOP, fill=BOTH)

        self.txt_user_2 = Label(root, text="Your Friend")
        self.txt_user_2.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.box_user_2 = Text(root, width=50, height=15, state=DISABLED, relief=FLAT, bg="light gray")
        self.box_user_2.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.divider_1 = Frame(height=2, bd=1, relief=SUNKEN)
        self.divider_1.pack(fill=X, pady=300)

        self.txt_user_1 = Label(root, text="You")
        self.txt_user_1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.box_user_1 = Text(root, width=50, height=15)
        self.box_user_1.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.divider_2 = Frame(height=2, bd=1, relief=SUNKEN)
        self.divider_2.pack(fill=X, pady=0)

        self.box_ip = Entry(root)
        self.box_ip.place(relx=0.25, rely=0.9, anchor=CENTER)
        self.box_ip.insert(0, "Destination IP")

        self.box_protocol = Spinbox(root, values=("TCP", "UDP"))
        self.box_protocol.place(relx=0.55, rely=0.9, anchor=CENTER)

        # Only U+0000 - U+FFFF range is allowed by Tcl
        # Emoji unicode table: https://apps.timwhitlock.info/emoji/tables/unicode
        # Emoji unicode to js: https://r12a.github.io/app-conversion/
        self.var_emoji = StringVar(root)
        self.var_emoji.set("\uD83D\uDE03")
        self.box_emoji = OptionMenu(root, self.var_emoji,
                                    "\uD83D\uDE03",
                                    "\uD83D\uDE09",
                                    "\uD83D\uDE0D")
        self.box_emoji.place(relx=0.775, rely=0.9, anchor=CENTER)

        self.btn_emoji = Button(root, text="+", width=2, command=self.on_add_emoji)
        self.btn_emoji.place(relx=0.875, rely=0.9, anchor=CENTER)

        self.btn_send = Button(root, text="SEND", width=50, command=self.on_send_text)
        self.btn_send.place(relx=0.5, rely=0.95, anchor=CENTER)

if __name__ == '__main__':
    Client(8887, 8888).gui()
    root.wm_title("IPChat")
    root.geometry("500x750+500+25")
    root.iconbitmap("img\\icon.ico")
    root.resizable(0, 0)
    root.mainloop()