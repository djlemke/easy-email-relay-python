from tkinter import *
from tkinter import ttk

class GUI(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self)
        self.title("Easy Email Relay")

        self.main_frame = ttk.Frame(self, padding="4 4 4 4")
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.commands_frame = ttk.Frame(self.main_frame, padding="4 4 4 4")
        self.commands_frame.grid(column=0, row=0, sticky=(N, W, E))

        self.start_button = ttk.Button(self.commands_frame, text="Start")
        self.start_button.grid(column=0, row=0, sticky=W)
        self.stop_button = ttk.Button(self.commands_frame, text="Stop")
        self.stop_button.grid(column=1, row=0, sticky=W)
        self.options_button = ttk.Button(self.commands_frame, text="Options", command=self.show_options)
        self.options_button.grid(column=2, row=0, sticky=W)
        self.log_text = Text(self.main_frame, width=80, height=24)
        self.log_text.grid(column=0,row=1,sticky=(N, W, E, S))

        for child in self.main_frame.winfo_children():
            child.grid_configure(padx=4, pady=4)
    
    def start(self):
        self.mainloop()
    
    def rebind_button(self, button, cmd):
        if button == "start":
            self.start_button.configure(command=cmd)
        elif button == "stop":
            self.stop_button.configure(command=cmd)
        elif button == "options":
            self.options_button.configure(command=cmd)
    
    def show_options(self):
        pass