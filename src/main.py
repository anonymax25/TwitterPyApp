import tkinter as tk
from tkinter import LEFT, ttk, HORIZONTAL, BOTTOM, X
from src.user import getTweetsByUser
from src.address import getTweetsByAddress


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.find_address = tk.Button(self)
        self.find_user = tk.Button(self)
        self.label = tk.Label(self, text="Find by address or by userID :")
        self.input = tk.Entry(self)
        self.progressbar = ttk.Progressbar(orient=HORIZONTAL, length=250, mode='determinate')
        self.error = tk.Label(self, text="")
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label.pack(side=LEFT, padx=5, pady=10)
        self.input.pack(side=LEFT, padx=5, pady=10, expand=True)

        self.find_user["text"] = "Find tweets by user"
        self.find_user["command"] = self.get_by_user
        self.find_user.pack(side=LEFT, padx=5, pady=10)

        self.find_address["text"] = "Find tweets by Address"
        self.find_address["command"] = self.get_by_address
        self.find_address.pack(side=LEFT, padx=5, pady=10)
        self.error.pack(fill=X)
        self.progressbar.pack(side=BOTTOM, pady=10)

    def get_by_user(self):
        if not self.input.get().strip():
            self.error['text'] = "Input can't be empty !"
        else:
            self.progressbar.start()
            getTweetsByUser("@" + self.input.get())

    def get_by_address(self):
        if not self.input.get().strip():
            self.error['text'] = "Input can't be empty !"
        else:
            getTweetsByAddress(self.input.get(), 10)


root = tk.Tk()
app = Application(master=root)

app.master.title("Twitter search App")
app.master.minsize(400, 150)

app.mainloop()
