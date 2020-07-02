import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input = tk.Entry(self)
        self.input.pack(side="top",ipadx=20, padx=30, ipady=5, pady=30,fill='x' )

        self.location = tk.Button(self)
        self.location["text"] = "Get by location"
        self.location["command"] = self.get_location
        self.location.pack(side="left",ipadx=20, padx=30)

        self.hastag = tk.Button(self)
        self.hastag["text"] = "Get by #hastag"
        self.hastag["command"] = self.get_hastag
        self.hastag.pack(side="left",ipadx=20, padx=30 )

        self.text = tk.Text(self)
        self.text.pack(ipadx=20, padx=30, fill='x')

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def get_location(self):
        print(self.input.get())

    def get_hastag(self):
        print(self.input.get())

root = tk.Tk()
app = Application(master=root)

app.master.title("Twitter search App")
app.master.minsize(400,400)
app.master.maxsize(1000, 1920)

app.mainloop()