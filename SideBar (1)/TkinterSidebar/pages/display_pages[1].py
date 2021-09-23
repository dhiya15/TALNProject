from tkinter import ttk, filedialog
import arabic_reshaper

from ..pages.page import *

"""
defualt widget color:

#201F1E
"""

def normalize():
    print("Hello, world")

def_bg = "white"
def_fg = "black"

"""class Dashboard(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Dashboard", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)"""

"""class Category(Page):
    def __init__(self, parent):
        
        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Category", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)"""

class CorpusPage(Page):

    def __init__(self, parent):
        def openFile():
            tf = filedialog.askopenfilename(
                initialdir="home/fatima/",
                title="Open Text file",
                filetypes=(("Text Files", "*.txt"),)
            )
            pathh.insert(END, tf)
            tf = open(tf)  # or tf = open(tf, 'r')
            data = tf.read()
            txtarab = arabic_reshaper.reshape(data)
            txtarea.insert(END, txtarab)
            tf.close()
        # init page/ delete old page
        Page.__init__(self, parent)

        #create corpus from search

        Button(self, text="Open File", bg="green", command=openFile).place(x=150, y=100)

        pathh = Entry(self, width=67)
        pathh.place(x=250, y=103)

        txtarea = Text(self, width=80, height=20)
        txtarea.place(x=150, y=150)


class NormalizePage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)

        button = ttk.Button(self, text='Normalize a text')
        button.config(command=normalize)
        button.pack()
        button.place(x=100, y=150)

        t = Label(self, text="Normalization of texts", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class StemmingPage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Stemming", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class SimilarityPage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Similarity measurements", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)


class CardDesignPage(Page):
    def __init__(self, parent):
        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Chart", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class AnalyticsPage(Page):
    def __init__(self, parent):
        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Analytic Corpora", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class AboutPage(Page):
    def __init__(self, parent):
        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="About", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)