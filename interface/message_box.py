from customtkinter import *

class Message(CTkFrame):
        def __init__(self, master, message):
            super().__init__(master)
            txt = CTkLabel(self, text=message, font=("Helvetica", 12))
            txt.pack(pady=10, ipadx=40, ipady=20)
             


class MessageBox():
    def __init__(self, parent, title, message, high=250, width=150):

        self.root = CTkToplevel(parent)
        self.root.geometry(f"{width}x{high}")
        self.root.resizable(False, False)
        self.root.title(title)
        self.message_frame = Message(self.root, message)
        self.message_frame.pack(pady=20)
        self.btn = CTkButton(self.root, text="OK", command=self.root.destroy)
        self.btn.pack(pady=10)
        self.focus()

    def focus(self):
        self.root.grab_set()