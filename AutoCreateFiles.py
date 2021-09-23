from tkinter import *
from tkinter import filedialog, ttk
import arabic_reshaper
import bidi.algorithm


def openFile():
    tf = filedialog.askopenfilename(
        initialdir="home/fatima/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    pathh.insert(END, tf)
    tf = open(tf, encoding="utf-8")  # or tf = open(tf, 'r')
    data = tf.read()

    data = arabic_reshaper.reshape(data)
    data = bidi.algorithm.get_display(data)

    txtarea.insert(END, data)
    tf.close()


ws = Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws['bg'] = 'white'

Button(ws, text="Open File", bg="green", command=openFile).place(x=150, y=100)

pathh = Entry(ws, width=67)
pathh.place(x=250, y=103)

horz_scrol = Scrollbar(ws, orient='horizontal')
horz_scrol.pack(side=BOTTOM, fill=X)

txtarea = Text(ws, width=80, height=20, wrap='none', xscrollcommand=horz_scrol.set)
txtarea.place(x=150, y=150)
txtarea.tag_configure('tag-right', justify='right')
horz_scrol.config(command=txtarea.xview)

ws.mainloop()
