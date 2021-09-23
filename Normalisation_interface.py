from tkinter import *
from tkinter import filedialog, ttk, messagebox
from bidi import algorithm
from arabic_reshaper import arabic_reshaper
import normalisation
import normal


def openFile():
    file = filedialog.askopenfilename(
        initialdir="home/fatima/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    returninterface.path.delete('0', END)
    returninterface.path.insert(END, file)


def normalize():
    selectpath = returninterface.path.get()
    tf = open(selectpath, 'r', encoding="utf-8")
    for data in tf:
        if (returninterface.varall.get() == 0) & (returninterface.varnonarabic.get() == 1) & (returninterface.vardiac.get() == 1) & (returninterface.varponct.get() == 1) & (
                returninterface.varnormlettre.get() == 1) & (returninterface.varstop.get() == 0):
            sent = normalisation.tokenisation(data)
            sent = arabic_reshaper.reshape(sent)
            sent = algorithm.get_display(sent)
            returninterface.displaynorm.insert(END, sent + "\n")


        elif (returninterface.varall.get() == 1) & (returninterface.varnonarabic.get() == 0) & (returninterface.vardiac.get() == 0) & (returninterface.varponct.get() == 0) & (
                returninterface.varnormlettre.get() == 0) & (returninterface.varstop.get() == 0):
            sent = normalisation.tokenstop(data)
            sent = arabic_reshaper.reshape(sent)
            sent = algorithm.get_display(sent)
            returninterface.displaynorm.insert(END, sent + "\n")

        elif (returninterface.varall.get() == 0) & (returninterface.varnonarabic.get() == 1) & (returninterface.vardiac.get() == 0) & (returninterface.varponct.get() == 0) & (
                returninterface.varnormlettre.get() == 0) & (returninterface.varstop.get() == 0):
            sent = normal.normaliser(data)
            sent = arabic_reshaper.reshape(sent)
            sent = algorithm.get_display(sent)
            returninterface.displaynorm.insert(END, sent + "\n")


        elif (returninterface.varall.get() == 0) & (returninterface.varnonarabic.get() == 1) & (returninterface.vardiac.get() == 0) & (returninterface.varponct.get() == 0) & (
                returninterface.varnormlettre.get() == 0) & (returninterface.varstop.get() == 0):
            sent = normalisation.remove_stopWord(data)
            sent = arabic_reshaper.reshape(sent)
            sent = algorithm.get_display(sent)
            returninterface.displaynorm.insert(END, sent + "\n")


        else:
            sent = normalisation.tokenstop(data)
            sent = arabic_reshaper.reshape(sent)
            sent = algorithm.get_display(sent)
            returninterface.displaynorm.insert(END, sent + "\n")


def savetext():
    filename = filedialog.asksaveasfilename(defaultextension='.txt')
    f = open(filename, 'w')
    d = returninterface.displaynorm.get('1.0', 'end')
    d = arabic_reshaper.reshape(d)
    d = algorithm.get_display(d)
    f.write(d)
    f.close()
    messagebox.showinfo('FYI', 'File Saved')


def delete():
    returninterface.displaynorm.delete('1.0', END)


def returninterface(normalization):
    '''normalization = Tk()
    normalization.title("Normalisation")
    normalization.geometry("600x600")
    # stemming['bg'] = "white"'''
    
    
    wrapper1 = LabelFrame(normalization, text="Normalization", width=630, height=680, bg="white",
                          font=("Times New Roman", "14", "bold"))
    wrapper1.place(x=300, y=20)
    
    lblselectfile = Label(wrapper1, text="Select text to be normalize", bg="white",
                          font=("Times New Roman", "11", "bold")).place(x=15, y=15)
    canva1 = Canvas(wrapper1, width=595, height=70, bg="white", border=1, relief=SUNKEN)
    canva1.place(x=15, y=35)
    
    openfirsttext = Button(canva1, text="Select", height=1, width=7, font=("Times New Roman", "12"),
                           command=openFile).place(x=50, y=20)
    returninterface.path = Entry(canva1, width=45)
    returninterface.path.place(x=150, y=22)
    
    lbloutput = Label(wrapper1, text="PreTreatments", bg="white", font=("Times New Roman", "11", "bold")).place(x=15, y=110)
    
    canva2 = Canvas(wrapper1, width=595, height=110, bg="white", border=1, relief=SUNKEN)
    canva2.place(x=15, y=130)
    
    returninterface.varall = IntVar()
    all = Checkbutton(canva2, text="ALL", variable=returninterface.varall, font=("Times New Roman", "10", "bold"), bg="white", onvalue=1,
                      offvalue=0)
    all.place(x=10, y=25)
    returninterface.varnonarabic = IntVar()
    nonarab = Checkbutton(canva2, text="Remove Non Arabic Word", variable=returninterface.varnonarabic,
                          font=("Times New Roman", "10", "bold"), bg="white", onvalue=1, offvalue=0)
    nonarab.place(x=10, y=70)
    returninterface.vardiac = IntVar()
    diacr = Checkbutton(canva2, text="Remove Diacritics", variable=returninterface.vardiac, font=("Times New Roman", "10", "bold"),
                        bg="white", onvalue=1, offvalue=0)
    diacr.place(x=200, y=25)
    returninterface.varnormlettre = IntVar()
    normlettre = Checkbutton(canva2, text="Normalise Lettres", variable=returninterface.varnormlettre,
                             font=("Times New Roman", "10", "bold"), bg="white", onvalue=1, offvalue=0)
    normlettre.place(x=200, y=70)
    returninterface.varstop = IntVar()
    delstop = Checkbutton(canva2, text="Remove Stop Words", variable=returninterface.varstop, font=("Times New Roman", "10", "bold"),
                          bg="white", onvalue=1, offvalue=0)
    delstop.place(x=350, y=25)
    returninterface.varponct = IntVar()
    delponct = Checkbutton(canva2, text="Remove Ponctuations & Symbols", variable=returninterface.varponct,
                           font=("Times New Roman", "10", "bold"), bg="white", onvalue=1, offvalue=0)
    delponct.place(x=350, y=70)
    
    normalizebtn = Button(wrapper1, text="Normalize", font=("Times New Roman", "12"), bg="#0da5c4",
                          command=normalize).place(x=270, y=250)
    
    lbloutput = Label(wrapper1, text="Output Text", bg="white", font=("Times New Roman", "11", "bold")).place(x=15, y=280)
    
    canva3 = Canvas(wrapper1, width=595, height=340, bg="white", border=1, relief=SUNKEN)
    canva3.place(x=15, y=300)
    
    returninterface.displaynorm = Text(canva3, width=71, height=17, wrap='none')
    returninterface.displaynorm.place(x=10, y=10)
    returninterface.displaynorm.tag_configure('tag-right', justify='right')
    savebtn = Button(canva3, text="Save", width=10, font=("Times New Roman", "12"), bg="#0da5c4", command=savetext).place(
        x=200, y=305)
    delbtn = Button(canva3, text="Delete", width=10, font=("Times New Roman", "12"), bg="#0da5c4", command=delete).place(
        x=330, y=305)
    

    
    return normalization
    #normalization.mainloop()
