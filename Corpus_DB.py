import sqlite3

def corpusData():
    con = sqlite3.connect("corpus_DB.db")
    #cur = con.cursor()
    con.execute("""CREATE TABLE IF NOT EXISTS corpus(idcorp INTEGER PRIMARY KEY AUTOINCREMENT, name text, domain text, date_creation text)""")
    con.execute("""CREATE TABLE IF NOT EXISTS text(idtxt INTEGER PRIMARY KEY AUTOINCREMENT, idcorptxt INTEGER, FOREIGN KEY(idcorptxt) REFERENCES corpus(idcorp))""")
    con.commit()
    con.close()


if __name__ == '__main__':
    corpusData()
