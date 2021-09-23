import sqlite3
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from tkcalendar import Calendar, DateEntry






def search():
    srch = returninterface.s.get()
    query1 = "SELECT idcorp, name, domain, date_creation FROM corpus WHERE idcorp LIKE '%" + srch + "%' OR name LIKE '%" + srch + "%' OR domain LIKE '%" + srch + "%' OR date_creation LIKE '%" + srch + "%'"
    returninterface.cursor.execute(query1)
    rows = returninterface.cursor.fetchall()
    update(rows)


def clear():
    query2 = "SELECT idcorp, name, domain, date_creation FROM corpus"
    returninterface.cursor.execute(query2)
    rows = returninterface.cursor.fetchall()
    update(rows)

def add_new_corpus():
    #c_id = id.get()
    c_name = returninterface.name.get()
    c_domain = returninterface.domaine.get()
    c_date = returninterface.date.get()

    queryadd = "INSERT INTO corpus(name, domain, date_creation) VALUES (?, ?, ?)"
    returninterface.cursor.execute(queryadd, (c_name, c_domain, c_date))
    returninterface.db.commit()
    clear()

def update_corpus():
    c_id = returninterface.id.get()
    c_name = returninterface.name.get()
    c_domain = returninterface.domaine.get()
    c_date = returninterface.date.get()

    if messagebox.askyesno("Confirm please!", "Are you sure you want to update this corpus?"):
        query_up = "UPDATE corpus SET name=?, domain=?, date_creation=? WHERE idcorp=?"
        returninterface.cursor.execute(query_up, (c_name, c_domain, c_date, c_id))
        returninterface.db.commit()
        clear()
    else:
        return True

def delete_corpus():
    c_id = returninterface.id.get()
    if messagebox.askyesno("Confirm Delete?", "Are you sure you want delete this corpus?"):
        querydlt = "DELETE FROM corpus WHERE idcorp= " + str(c_id)
        returninterface.cursor.execute(querydlt)
        returninterface.db.commit()
        clear()
    else:
        return True

def reset():
    #entid.delete(0, END)
    returninterface.entname.delete(0, END)
    returninterface.entdomain.delete(0, END)
    returninterface.entdate.delete(0, END)

def update(rows):
    print(rows)
    returninterface.tree.delete(*returninterface.tree.get_children())
    for row in rows:
       returninterface.tree.insert('', 'end', '#{}'.format(row['idcorp']), text=row['idcorp'])
       returninterface.tree.set('#{}'.format(row['idcorp']), '#1', row['idcorp'])
       returninterface.tree.set('#{}'.format(row['idcorp']), '#2', row['name'])
       returninterface.tree.set('#{}'.format(row['idcorp']), '#3', row['domain'])
       returninterface.tree.set('#{}'.format(row['idcorp']), '#4', row['date_creation'])


def getrow(event):
    rowid = returninterface.tree.identify_row(event.y)
    item = returninterface.tree.item(returninterface.tree.focus())
    returninterface.id.set(item['values'][0])
    returninterface.name.set(item['values'][1])
    returninterface.domaine.set(item['values'][2])
    returninterface.nb_f.set(item['values'][3])
    returninterface.date.set(item['values'][4])

def returninterface(corpus):
    '''corpus = Tk()
    corpus.title("Scraping web")
    corpus.geometry("600x600")
    # corpus['bg'] = "white"'''
    
    returninterface.s = StringVar()
    returninterface.id = IntVar()
    returninterface.name = StringVar()
    returninterface.domaine = StringVar()
    returninterface.nb_f = IntVar()
    returninterface.date = StringVar()
    
    
    
    wrapper1 = LabelFrame(corpus, text="Corpus Informations", width=600, height=680, bg="white",
                          font=("Times New Roman", "16", "bold"))
    wrapper1.place(x=20, y=10)
    
    canva1 = Canvas(wrapper1, width=565, height=300, bg="white")
    canva1.place(x=15, y=15)
    
    """labid = Label(canva1, text="Corpus ID: ", bg="white", font=("Times New Roman", "13")).place(x=10, y=10)
    entid = Entry(canva1, textvariable=id, width=40)
    entid.place(x=150, y=10)"""
    
    labname = Label(canva1, text="Corpus Name: ", bg="white", font=("Times New Roman", "13")).place(x=10, y=60)
    entname = Entry(canva1, textvariable=returninterface.name, width=40)
    entname.place(x=150, y=60)
    
    labdomain = Label(canva1, text="Corpus Domain: ", bg="white", font=("Times New Roman", "13")).place(x=10, y=120)
    entdomain = Entry(canva1, textvariable=returninterface.domaine, width=40)
    entdomain.place(x=150, y=120)
    
    labdate = Label(canva1, text="Creation Date: ", bg="white", font=("Times New Roman", "13")).place(x=10, y=180)
    entdate = DateEntry(wrapper1, textvariable=returninterface.date, width=39, selectmode="day", firstweekday="sunday", locale="en_US", date_pattern='y/mm/dd')
    entdate.place(x=165, y=195)
    
    add_btn = Button(canva1, text="ADD", command=add_new_corpus, width=10, bg="#a4d4f9", font=("Times New Roman", "11")).place(x=10, y=250)
    up_btn = Button(canva1, text="EDIT", command=update_corpus, width=10, bg="#a4d4f9", font=("Times New Roman", "11")).place(x=150, y=250)
    dlt_btn = Button(canva1, text="REMOVE", command=delete_corpus, width=10, bg="#a4d4f9", font=("Times New Roman", "11")).place(x=300, y=250)
    reset_btn = Button(canva1, text="RESET", command=reset, width=10, bg="#a4d4f9", font=("Times New Roman", "11")).place(x=440, y=250)
    
    # ------------------------------------------------------------------------------------------------------------------------
    
    canva2 = Canvas(wrapper1, width=565, height=200, bg="white")
    canva2.place(x=15, y=400)
    
    lablel1 = Label(canva2, text="Search corpus in Data Base", bg="white", fg="gray", font=("Times New Roman", "12"))
    lablel1.place(x=10, y=5)
    
    lablel2 = Label(canva2, text="Search", bg="white", font=("Times New Roman", "14", "bold"))
    lablel2.place(x=25, y=40)
    srchentry = Entry(canva2, textvariable=returninterface.s, width=40)
    srchentry.place(x=100, y=40)
    
    btn = Button(canva2, text="Search", command=search, width=10, bg="#a4d4f9", font=("Times New Roman", "11"))
    btn.place(x=150, y=100)
    
    btnretour = Button(canva2, text="Reset", command=clear, width=10, bg="#a4d4f9", font=("Times New Roman", "11"))
    btnretour.place(x=270, y=100)
    
    # ---------------------------Details-----------------------------
    wrapper2 = LabelFrame(corpus, text="Corpus Details", width=700, height=680, bg="white",
                          font=("Times New Roman", "16", "bold"))
    wrapper2.place(x=650, y=10)
    
    returninterface.tree = ttk.Treeview(wrapper2, columns=(0, 1, 2, 3, 4), show="headings", height="30")
    
    returninterface.tree.heading("0", text="ID")
    returninterface.tree.heading("1", text="Name")
    returninterface.tree.heading("2", text="Domain")
    returninterface.tree.heading("3", text="Creation Date")
    returninterface.tree.heading("4", text="File Name")
    returninterface.tree.bind('<Double 1>', getrow)
    
    returninterface.tree.column("0", width=100, minwidth=150, stretch=NO)
    returninterface.tree.column("1", width=150, minwidth=150, stretch=NO)
    returninterface.tree.column("2", width=120, minwidth=150, stretch=NO)
    returninterface.tree.column("3", width=150, minwidth=150, stretch=NO)
    returninterface.tree.column("4", width=150, minwidth=150, stretch=NO)
    
    returninterface.tree.place(x=10, y=10)
    ttk.Style().configure(".", background="white", foreground="#3ba6f9", font=("Times New Roman", "11"))
    
    #returninterface.db = sqlite3.connect("corpus_DB.db")
    
    returninterface.db = sqlite3.connect("C:\\Users\\Dhiya\\Downloads\\Compressed\\NewTestProject_15_09_2021_22_30\\NewTestProject\\corpus_DB.db")
    returninterface.db.row_factory = sqlite3.Row
    returninterface.cursor = returninterface.db.cursor()
    
    query1 = "SELECT idcorp, name, domain, date_creation, idtxt from corpus join text on corpus.idcorp=text.idcorptxt"
    returninterface.cursor.execute(query1)
    rows = returninterface.cursor.fetchall()
    update(rows)
    
    return corpus
    
    #corpus.mainloop()
