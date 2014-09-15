#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import os
from Tkinter import *
import tkMessageBox

def callback():
    result = os.system('python PortingChecker')
    tkMessageBox.showinfo('Porting Checker','Checking successful!')
    quit()

width_scale = 1
height_scale = 0.5

rt = Tk()
rt.resizable(False,False)
rt.title("Porting Checker") 

rt.update() # update window ,must do
curWidth = rt.winfo_reqwidth() # get current width
curHeight = rt.winfo_height() # get current height
scnWidth,scnHeight = rt.maxsize() # get screen width and height

win_width = curWidth * width_scale
win_height = curHeight * height_scale
# now generate configuration information
tmpcnf = '%dx%d+%d+%d'%(win_width, win_height, (scnWidth-curWidth)/2, (scnHeight-curHeight)/2)
rt.geometry(tmpcnf)

info = Label(rt, text='hi tanya')
info.pack(fill=Y,expand=1)

run = Button(rt, text='start checking...', anchor = 'center', width = 15, height = 1, command=callback)
run.pack()

rt.mainloop()



