from tkinter import *
from tkinter import filedialog, ttk, messagebox
import scrapautonew
import scrapurl
import arabic_reshaper
import bidi.algorithm
from bidi import algorithm

# ----------------functions---------------

def openFIle():
    file = filedialog.askopenfilename(
        initialdir="home/fatima/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    path.delete('0', END)
    path.insert(END, file)


def openDirectory():
    directory = filedialog.askdirectory()
    path1.delete('0', END)
    path1.insert(END, directory)


def getresult():
    # return the result of scraping(urls + texts)
    domaine = entrydomaine.get()
    inputdir = path1.get()
    stop = entrypage.get()
    query = entrysearch.get()
    apply = scrapautonew.ScrapWeb(query, stop, domaine, inputdir)
    apply = arabic_reshaper.reshape(apply)
    apply = bidi.algorithm.get_display(apply)
    textarea.insert(END, apply)


def SaveOneUrlToFile():
    # open selected folder, create txt files for each url
    filename = filedialog.asksaveasfilename(defaultextension='.txt')
    file = open(filename, 'a')
    saveurl = entryurl.get()
    data = textarea.get('1.0', 'end')
    data = arabic_reshaper.reshape(data)
    data = algorithm.get_display(data)
    file.write(saveurl+'\n'+'\n')
    file.write(data)
    file.close()
    messagebox.showinfo('Successful', 'File Saved')


def deleteText():
    # if the user doesn't satisfied with results, can delete it.
    textareasent.delete("1.0", END)


def getUrl():
    # scrap specific url
    url = entryurl.get()
    data = scrapurl.scrapurl(url)
    data = arabic_reshaper.reshape(data)
    data = bidi.algorithm.get_display(data)
    textarea.delete("1.0", END)
    textarea.insert(END, data)


def savetokens():
    filename = filedialog.asksaveasfilename(defaultextension='.txt')
    file = open(filename, 'a')
    data = textareasent.get('1.0', 'end')
    data = arabic_reshaper.reshape(data)
    data = algorithm.get_display(data)
    file.write(data)
    file.close()
    messagebox.showinfo('Successful', 'File Saved')


# -----------------interface widgets--------------------------------------------------------
scrap = Tk()
scrap.title("Scraping web")
scrap.geometry("600x600")
scrap['bg'] = "white"

# --------------------------insert domaine and nb page---------------------------------------
entrydomaine = StringVar()
entrysearch = StringVar()
entrypage = IntVar()
entryurl = StringVar()
src = StringVar()

# -----------------informations----------------------------------------------------------------
wrapper1 = LabelFrame(scrap, text="New Scrap", width=760, height=315, bg="white")
wrapper1.place(x=20, y=10)

scraplab = Label(wrapper1, text="Scrap set of URLs ", bg="white", font=("Times New Roman", 12, "bold")).place(x=10,
                                                                                                              y=10)

canva1 = Canvas(wrapper1, width=400, height=185, bg="white", border=1, relief=SUNKEN)
canva1.place(x=10, y=30)

labelDom = Label(canva1, text="Domain Name", bg="white").place(x=10, y=20)
domaine = Entry(canva1, textvariable=entrydomaine, width=30).place(x=130, y=20)

sourcelab = Label(canva1, text="Choose Source", bg="white").place(x=10, y=63)
source = ttk.Combobox(canva1, width=29, textvariable=src, values=('Google Search', 'Wikipedia')).place(x=130, y=63)

labelsearch = Label(canva1, text="Search Query", bg="white").place(x=10, y=105)
search = Entry(canva1, textvariable=entrysearch, width=30).place(x=130, y=105)

nbPage = Label(canva1, text="Number of pages\nto be returned", bg="white").place(x=10, y=140)
nbPage = Entry(canva1, textvariable=entrypage, width=10).place(x=130, y=140)

btnsearch = Button(canva1, text="Search", bg="#0da5c4", height=1, width=10, command=getresult).place(x=270, y=140)

#############################################################################################################################

persourllab = Label(wrapper1, text="Custom URL ", bg="white", font=("Times New Roman", 12, "bold")).place(x=420, y=0)

canva2 = Canvas(wrapper1, width=320, height=186, bg="white", border=1, relief=SUNKEN)
canva2.place(x=420, y=30)

labelurl = Label(canva2, text="Enter a specific URL", bg="white").place(x=10, y=20)
url = Entry(canva2, textvariable=entryurl, width=35)
url.place(x=10, y=50)
geturl = Button(canva2, text="Get Url", bg="#0da5c4", height=1, width=5, command=getUrl).place(x=100, y=100)

# -----------------------------------------------------------------------------------------------------------------------------

openfile = Button(wrapper1, text="Open File", height=1, width=10, command=openDirectory).place(x=10, y=240)
path1 = Entry(wrapper1, width=40)
path1.place(x=130, y=240)
labopenfile = Label(wrapper1, text="  Select Path To Save Results", bg="white", fg="gray").place(x=130, y=265)

########################################################################################################################################

# -----------------------display results of scraping------------------------------------------------
wrapper2 = LabelFrame(scrap, text="Search Result", width=760, height=370, bg="white")
wrapper2.place(x=20, y=330)

textarea = Text(wrapper2, width=60, height=19, wrap='none')
# , xscrollcommand=horz_scrol.set)
textarea.place(x=10, y=0)
textarea.tag_configure('tag-right', justify='right')
# horz_scrol.config(command=textarea.xview)

count = Text(wrapper2, width=21, height=10, wrap='none')
count.place(x=510, y=0)
count.tag_configure('tag-left', justify='left')
count.insert(END, "\nURLs: \n\nArticles: \n\nSource: ")

savebtn = Button(wrapper2, text="Save", bg="#0da5c4", height=1, width=10, command=SaveOneUrlToFile).place(x=550, y=220)
cancelbtn = Button(wrapper2, text="Cancel", bg="#0da5c4", height=1, width=10, command=deleteText).place(x=550, y=270)

# -------------------tokenize text to senteces-------------------------------------------------

wrapper3 = LabelFrame(scrap, text="Tokenization", width=550, height=680, bg="white")
wrapper3.place(x=800, y=20)

canva = Canvas(wrapper3, width=520, height=100, bg="white")
canva.place(x=10, y=10)

opentextfile = Button(canva, text="Open File", height=1, width=10, command=openFIle).place(x=30, y=25)
path = Entry(canva, width=35)
path.place(x=160, y=25)
labopenfile = Label(canva, text="  Select Path To get text", bg="white", fg="gray").place(x=200, y=50)

labopenfile = Label(wrapper3, text="Output Text", bg="white", fg="gray").place(x=15, y=130)

textareasent = Text(wrapper3, width=64, height=26, wrap='none')
textareasent.place(x=15, y=150)
textareasent.tag_configure('tag-right', justify='right')

savesent = Button(wrapper3, text="Save", bg="#0da5c4", height=1, width=10, command=savetokens).place(x=100, y=610)
delsent = Button(wrapper3, text="Delete", bg="#0da5c4", height=1, width=10, command=deleteText).place(x=230, y=610)
cancelsent = Button(wrapper3, text="Cancel", bg="#0da5c4", height=1, width=10, command=scrap.quit).place(x=360, y=610)

scrap.mainloop()
#return scrap
