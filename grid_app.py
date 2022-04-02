


import tkinter as tk


class GridApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)

        self.master.title('grid of widgets')
        self.master.geometry('240x240')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        label1=tk.Label(self,text='label1', bg='red', height=100)
        label1.grid(row=0,column=0,columnspan=2,sticky='news',padx=5,pady=5)
        
        label2=tk.Label(self,text='label2', bg='green')
        label2.grid(row=1,column=0,sticky='news',padx=5,pady=5)

        label3=tk.Label(self,text='label3', bg='blue')
        label3.grid(row=1,column=1,sticky='news',padx=5,pady=5)