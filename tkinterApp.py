import tkinter as tk
import mainUser
from tkinter import X, LEFT, RIGHT


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.quit = tk.Button(self, text="Close", fg="red", command=self.master.destroy)
        self.find_user = tk.Button(self)
        self.input_address = tk.Entry(self)
        self.label_address = tk.Label(self, text="Find by address")
        self.input_user = tk.Entry(self)
        self.label_user = tk.Label(self, text="Find with user @")
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_user.pack(side=LEFT, padx=5, pady=5)
        self.input_user.pack(fill=X, padx=5, expand=True)

        self.label_address.pack(side=LEFT, padx=5, pady=5)
        self.input_address.pack(fill=X, padx=5, expand=True)

        self.find_user["text"] = "Find User tweets"
        self.find_user["command"] = self.get_user
        self.find_user.pack(side="left", ipadx=20, padx=30)

        self.hastag = tk.Button(self)
        self.hastag["text"] = "Get by #hastag"
        self.hastag["command"] = self.get_hastag
        self.hastag.pack(side="left", ipadx=20, padx=30)

        self.quit.pack(side=RIGHT, padx=5, pady=5)

        # okButton.pack(side=RIGHT)

    def get_user(self):
        mainUser.getUserInfo("@" + self.input_user.get())

    def get_hastag(self):
        print(self.input.get())


root = tk.Tk()
app = Application(master=root)

app.master.title("Twitter search App")
app.master.minsize(400, 400)
app.master.maxsize(1000, 1920)

app.mainloop()
