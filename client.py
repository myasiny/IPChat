from tkinter import *
from tkinter.filedialog import *

root = Tk()

class Client:
    def __init__(self):
        pass

    def on_send_file(self):
        file = askopenfilename(parent=root)
        path = os.path.expanduser(file)
        pass
        # TODO: Send file

    def on_send_text(self):
        pass
        # TODO: Send text

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
        box_user_2 = Text(root, width=50, height=15, state=DISABLED, relief=FLAT, bg="light gray")
        box_user_2.place(relx=0.5, rely=0.3, anchor=CENTER)

        divider_1 = Frame(height=2, bd=1, relief=SUNKEN)
        divider_1.pack(fill=X, pady=300)

        txt_user_1 = Label(root, text="You")
        txt_user_1.place(relx=0.5, rely=0.5, anchor=CENTER)
        box_user_1 = Text(root, width=50, height=15)
        box_user_1.place(relx=0.5, rely=0.7, anchor=CENTER)

        divider_2 = Frame(height=2, bd=1, relief=SUNKEN)
        divider_2.pack(fill=X, pady=0)
        box_ip = Entry(root)
        box_ip.place(relx=0.25, rely=0.9, anchor=CENTER)
        box_ip.insert(0, "Destination IP")

        box_protocol = Spinbox(root, values=("TCP", "UDP"))
        box_protocol.place(relx=0.55, rely=0.9, anchor=CENTER)

        var_emoji = StringVar(root)
        var_emoji.set("Emoji")
        box_emoji = OptionMenu(root, var_emoji, "\u2764")
        box_emoji.place(relx=0.8, rely=0.9, anchor=CENTER)

        btn_send = Button(root, text="SEND", width=50, command=self.on_send_text)
        btn_send.place(relx=0.5, rely=0.95, anchor=CENTER)

if __name__ == '__main__':
    Client().gui()
    root.wm_title("IPChat")
    root.geometry("500x750+500+25")
    root.iconbitmap("img\\icon.ico")
    root.resizable(0, 0)
    root.mainloop()