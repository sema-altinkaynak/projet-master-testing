from src.calculator.Calculator import Calculator

import tkinter
from tkinter import *
from tkinter import ttk

#On MacOS, install the last version of Python 3.10 and use /usr/local/bin/python3.10 PlayGround.py

class UserInterface:
    def __init__(self, start) -> None:
        self.calculator = Calculator()
        root = Tk()
        frm = ttk.Frame(root)
        frm.grid()
        self.text = tkinter.StringVar()
        self.text.set("")
        ttk.Label(frm, textvariable=self.text).grid(column=0, row=0, columnspan = 5)
        ttk.Button(frm, text="1", command=self.press1).grid(column=0, row=1)
        ttk.Button(frm, text="2", command=self.press2).grid(column=1, row=1)
        ttk.Button(frm, text="3", command=self.press3).grid(column=2, row=1)
        ttk.Button(frm, text="4", command=self.press4).grid(column=0, row=2)
        ttk.Button(frm, text="5", command=self.press5).grid(column=1, row=2)
        ttk.Button(frm, text="6", command=self.press6).grid(column=2, row=2)
        ttk.Button(frm, text="7", command=self.press7).grid(column=0, row=3)
        ttk.Button(frm, text="8", command=self.press8).grid(column=1, row=3)
        ttk.Button(frm, text="9", command=self.press9).grid(column=2, row=3)
        ttk.Button(frm, text="0", command=self.press0).grid(column=0, row=4)
        ttk.Button(frm, text="C", command=self.pressClear).grid(column=3, row=1)
        ttk.Button(frm, text="+", command=self.pressAdd).grid(column=3, row=2)
        ttk.Button(frm, text="-", command=self.pressMinus).grid(column=3, row=3)
        ttk.Button(frm, text="x", command=self.pressMulti).grid(column=3, row=4)
        ttk.Button(frm, text="/", command=self.pressDivide).grid(column=4, row=2)
        ttk.Button(frm, text="(", command=self.pressAccOpen).grid(column=4, row=3)
        ttk.Button(frm, text=")", command=self.pressAccClose).grid(column=4, row=4)
        ttk.Button(frm, text="=", command=self.pressEqual).grid(column=2, row=4)
        if(start == True):
            root.mainloop()

    def press1(self):
        self.text.set(self.text.get() + "1")

    def press2(self):
        self.text.set(self.text.get() + "2")

    def press3(self):
        self.text.set(self.text.get() + "3")

    def press4(self):
        self.text.set(self.text.get() + "4")

    def press5(self):
        self.text.set(self.text.get() + "5")

    def press6(self):
        self.text.set(self.text.get() + "6")
    
    def press7(self):
        self.text.set(self.text.get() + "7")

    def press8(self):
        self.text.set(self.text.get() + "8")
    
    def press9(self):
        self.text.set(self.text.get() + "9")

    def press0(self):
        self.text.set(self.text.get() + "0")

    def pressClear(self):
        self.text.set("")

    def pressAdd(self):
        self.text.set(self.text.get() + " + ")

    def pressMinus(self):
        self.text.set(self.text.get() + " - ")

    def pressMulti(self):
        self.text.set(self.text.get() + " * ")

    def pressDivide(self):
        self.text.set(self.text.get() + " / ")

    def pressAccOpen(self):
        self.text.set(self.text.get() + " ( ")

    def pressAccClose(self):
        self.text.set(self.text.get() + " ) ")

    def pressEqual(self):
        self.text.set(self.calculator.calculate(self.text.get()))