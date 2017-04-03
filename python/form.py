import tkinter as Tkinter
class App(Tkinter.Tk):
    def __init__(self,parent):
        #Form
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.grid()
        #Entry
        self.entryvar = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryvar)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        #Button
        self.button = Tkinter.Button(self,text=u'Cick Me',command=self.OnButtonClick)
        self.button.grid(column=1,row=0)
        #Label
        self.labelvar = Tkinter.StringVar()
        self.label = Tkinter.Label(self,anchor='w',fg='black',bg='white',textvariable=self.labelvar)
        self.label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelvar.set("Hello!")
        #Config
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
    def OnButtonClick(self):
        self.labelvar.set(self.entryvar.get()+" (you clicked the button!)")
    def OnPressEnter(self,event):
        self.labelvar.set(self.entryvar.get()+" (You pressed enter!)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = App(None)
    app.title('Test App')
    app.mainloop()
