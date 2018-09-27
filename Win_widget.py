#!/usr/bin/python3
import sys
import os
import tkinter
from tkinter import *

master = Tk()
  
master.title("Alsac")
master.geometry("200x250")
master.wm_iconbitmap('py.png')
  
  
def DMstest():
    os.system("hello.py")
    
def test2():
    os.system('hello1.py')
    
name = Label(master, text="DMS Test")
name.grid(row=0, sticky=W, padx=(40, 10), pady=(10, 10))
b = Button(master, text="RUN", command=DMstest)
b.grid(row=0, column=1, padx=10, pady=10)

        
name2 = Label(master, text="Test2")
name2.grid(row=1, sticky=W, padx=(40, 10), pady=(10, 10))
b2 = Button(master, text="RUN", command=test2)
b2.grid(row=1, column=1, padx=10, pady=10)


mainloop()
