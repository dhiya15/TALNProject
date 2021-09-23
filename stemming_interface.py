from tkinter import *
from tkinter import filedialog, ttk, messagebox
from bidi import algorithm
from arabic_reshaper import arabic_reshaper
import AllStemmer

def openFile():
    file = filedialog.askopenfilename(
        initialdir="home/fatima/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    returninterface.path.delete('0', END)
    returninterface.path.insert(END, file)


def savetext():
    filename = filedialog.asksaveasfilename(defaultextension='.txt')
    f = open(filename, 'w')
    d = returninterface.displaystemming.get('1.0', 'end')
    d = arabic_reshaper.reshape(d)
    d = algorithm.get_display(d)
    f.write(d)
    f.close()
    messagebox.showinfo('FYI', 'File Saved')

def delete():
    returninterface.displaystemming.delete('1.0', END)

def getstem():
    selectpath = returninterface.path.get()
    if (len(selectpath) == 0):
        messagebox.showerror("ERROR!", "Your Field is Empty, You must select file")
    else:
        tf = open(selectpath, 'r', encoding="utf-8")
        if (returninterface.var1.get() == 0) & (returninterface.var2.get() == 0) & (returninterface.var3.get() == 0):
                messagebox.showwarning("WARNING!", "You must select a Stemmer")

        elif (returninterface.var1.get() == 1) & (returninterface.var2.get() == 0) & (returninterface.var3.get() == 0):
            returninterface.displaystemming.delete("1.0",END)
            for data in tf:
                sent = AllStemmer.IsriStemmer(data)
                sent = arabic_reshaper.reshape(sent)
                sent = algorithm.get_display(sent)
                returninterface.displaystemming.insert(END, sent + "\n")

        elif (returninterface.var1.get() == 0) & (returninterface.var2.get() == 1) & (returninterface.var3.get() == 0):
            returninterface.displaystemming.delete("1.0",END)
            for data in tf:
                sent = AllStemmer.TashaLightStem(data)
                sent = arabic_reshaper.reshape(sent)
                sent = algorithm.get_display(sent)
                returninterface.displaystemming.insert(END, sent + "\n")

        elif (returninterface.var1.get() == 0) & (returninterface.var2.get() == 0) & (returninterface.var3.get() == 1):
            returninterface.displaystemming.delete("1.0",END)
            for data in tf:
                sent = AllStemmer.TashaRootStem(data)
                sent = arabic_reshaper.reshape(sent)
                sent = algorithm.get_display(sent)
                returninterface.displaystemming.insert(END, sent + "\n")

        else:
                messagebox.showerror("ERROR!", "You must select one Stemmer at last")


def returninterface(stemming):
    '''stemming = Tk()
    stemming.title("Similarity Measurments")
    stemming.geometry("600x600")
    stemming['bg'] = "white"'''
    
    wrapper1 = LabelFrame(stemming, text="Stemming", width=630, height=680, bg="white", font=("Times New Roman", "14", "bold"))
    wrapper1.place(x=300, y=20)
    
    canva1 = Canvas(wrapper1, width=595, height=70, bg="white")
    canva1.place(x=15, y=15)
    
    labopenfile = Label(canva1, text="Select text", bg="white", font=("Times New Roman", "12", "bold")).place(x=10, y=10)
    opentext = Button(canva1, text="Select", height=1, width=5, font=("Times New Roman", "10", "bold"), command=openFile).place(x=90, y=10)
    returninterface.path = Entry(canva1, width=40)
    returninterface.path.place(x=200, y=15)
    
    canva2 = Canvas(wrapper1, width=595, height=70, bg="white")
    canva2.place(x=15, y=100)
    
    returninterface.var1 = IntVar()
    R1 = Checkbutton(canva2, text="ISRI Stemmer", variable=returninterface.var1, bg="white", font=("Times New Roman", "13"))
    R1.place(x=10, y=27)
    returninterface.var2 = IntVar()
    R2 = Checkbutton(canva2, text="Tasha Light Stemmer", variable=returninterface.var2, bg="white", font=("Times New Roman", "13"))
    R2.place(x=180, y=27)
    returninterface.var3 = IntVar()
    R3 = Checkbutton(canva2, text="Tasha Root Stemmer", variable=returninterface.var3, bg="white", font=("Times New Roman", "13"))
    R3.place(x=400, y=27)
    
    stembtn = Button(wrapper1, text="Stemming", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1, width=10, command=getstem).place(x=270, y=177)
    
    returninterface.displaystemming = Text(wrapper1, width=74, height=20, wrap='none')
    returninterface.displaystemming.place(x=15, y=220)
    returninterface.displaystemming.tag_configure('tag-right', justify='right')
    
    canva3 = Canvas(wrapper1, width=600, height=60, bg="white")
    canva3.place(x=15, y=580)
    
    savestemsent = Button(canva3, text="Save", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1, width=10, command=savetext).place(x=130, y=10)
    deletezonesent = Button(canva3, text="Delete", bg="#0da5c4", command=delete, font=("Times New Roman", "12", "bold"), height=1, width=10).place(x=250, y=10)
    cancel = Button(canva3, text="Cancel", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1, width=10, command=stemming.quit).place(x=370, y=10)
    return stemming
    #stemming.mainloop()