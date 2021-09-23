# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:07:24 2021

@author: Dhiya
"""


import tkinter as tk
from awesometkinter.bidirender import add_bidi_support, render_text

root = tk.Tk()

text = 'السلام عليكم'

# text display incorrectly on linux without bidi support
dummyvar = tk.StringVar()
dummyvar.set(text)
tk.Label(root, textvariable=dummyvar, font='any 20').pack()

# uncomment below to set a rendered text to first label
# dummyvar.set(render_text(text))

entry = tk.Entry(root, font='any 20', justify='right')
entry.pack()

lbl = tk.Label(root, font='any 20')
lbl.pack()

# adding bidi support for widgets
add_bidi_support(lbl)
add_bidi_support(entry)

# now there is a new set() and get() methods to set and get text on a widget
entry.set(text)
lbl.set('هذا كتاب adventure شيق')

root.mainloop()