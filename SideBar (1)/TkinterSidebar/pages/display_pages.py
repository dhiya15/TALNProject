from tkinter import ttk, filedialog
import arabic_reshaper

from ..pages.page import *

from tkinter import *
from tkinter import filedialog, ttk, messagebox
from bidi import algorithm
from bidi.algorithm import get_display

import sys  
sys.path.append('C:\\Users\\Dhiya\\Downloads\\Compressed\\NewTestProject_15_09_2021_22_30\\NewTestProject')  

import Similarity_interface as si
import corpus_interface as ci
import stemming_interface as sti
import Normalisation_interface as ni
import scraping_interface as spi



import arabic_reshaper
from awesometkinter.bidirender import add_bidi_support, render_text



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
        '''def openFile():
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
            tf.close()'''
        # init page/ delete old page
        Page.__init__(self, parent)
        main_frame = Frame(self, bg="white", width=1500, height=1000)
        main_frame.place(x=200, y=0)
        
        ci.returninterface(main_frame)


        #create corpus from search

        '''Button(self, text="Open File", bg="green", command=openFile).place(x=150, y=100)

        pathh = Entry(self, width=67)
        pathh.place(x=250, y=103)

        txtarea = Text(self, width=80, height=20)
        txtarea.place(x=150, y=150)'''
        #ci.returninterface(self)


class NormalizePage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)

        '''button = ttk.Button(self, text='Normalize a text')
        button.config(command=normalize)
        button.pack()
        button.place(x=100, y=150)

        t = Label(self, text="Normalization of texts", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)'''
        
        main_frame = Frame(self, bg="white", width=1500, height=1000)
        main_frame.place(x=-80, y=0)
        
        ni.returninterface(main_frame)

class StemmingPage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)

        main_frame = Frame(self, bg="white", width=1500, height=1000)
        main_frame.place(x=-80, y=0)
        
        sti.returninterface(main_frame)

class SimilarityPage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)
        
        main_frame = Frame(self, bg="white", width=1800, height=1000)
        main_frame.place(x=200, y=0)

        si.returninterface(main_frame)
        

class ScrapPage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)
        
        main_frame = Frame(self, bg="white", width=1800, height=1000)
        main_frame.place(x=200, y=0)

        spi.returninterface(main_frame)



class AboutPage(Page):
    def __init__(self, parent):
        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="About", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)