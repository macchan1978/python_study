


import tkinter as tk


class PackApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('ウィジェットの一列配置')
        self.master.geometry('240x240')

        label1 = tk.Label(self, text='label1', bg='red')
        label1.pack(padx=5, pady=5)

        label2 = tk.Label(self, text="label2",bg='green')
        label2.pack(padx=5, pady=5)

        label3 = tk.Label(self, text="label3",bg='blue')
        label3.pack(padx=5, pady=5)