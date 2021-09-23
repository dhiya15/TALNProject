from tkinter import *
from tkinter import filedialog, ttk, messagebox
from bidi import algorithm
from bidi.algorithm import get_display

import WriteInFIle
import normalisation
from AllSimMesures import *
import arabic_reshaper
from awesometkinter.bidirender import add_bidi_support, render_text

def openFIle1():
    file1 = filedialog.askopenfilename(
        initialdir="home/fatima/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    returninterface.path1.delete('0', END)
    returninterface.path1.insert(END, file1)

def openFile2():
    file2 = filedialog.askopenfilename(
        initialdir="home/fatima/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    returninterface.path2.delete('0', END)
    returninterface.path2.insert(END, file2)

def getsimfiles():
    selectpath1 = returninterface.path1.get()
    selectpath2 = returninterface.path2.get()
    if (len(selectpath1)==0) or (len(selectpath2)==0):
        messagebox.showinfo("ERROR!", "Your Field is Empty, You must select file")
    else:
        text1 = open(selectpath1, 'r', encoding="utf-8")
        f = text1.read()
        fichier1 = f.split("\n")
        text2 = open(selectpath2, 'r', encoding="utf-8")
        k = text2.read()
        fichier2 = k.split("\n")

        if (returninterface.all.get() == 0) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (e.get() == 0) & (returninterface.ja.get() == 0) & (returninterface.e.get() == 0) & (
                returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 0):
            messagebox.showinfo('WARNING!', 'You must check similarity measurements')

        ##------------All measurmentes----------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 0):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1)-1):
                for jj in range(len(fichier2)-1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)
                    ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)
                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  "+sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  "+sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  "+str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  "+str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  "+str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  "+str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  "+str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  "+str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  "+str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.3-0.7):  "+str(ponderation1) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.2-0.8):  "+str(ponderation2) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  "+str(harmonicAvg) + "\n")

#----------------------------------------Only syntactic-------------------------------------------------------------------------------------------

        elif (returninterface.all.get() == 0) & (returninterface.j.get() == 1) & (returninterface.d.get() == 1) & (returninterface.l.get() == 1) & (returninterface.e.get() == 1) & (returninterface.ja.get() == 1) & (
                returninterface.e.get() == 1) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 0):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")

#-------------------only semantic-----------------------------------------------------------------------------------------------------------

        elif (returninterface.all.get() == 0) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 1) & (returninterface.tf.get() == 1) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 0):

                returninterface.display.delete("1.0", END)
                for i in range(len(fichier1) - 1):
                        for jj in range(len(fichier2) - 1):
                            sentence1 = fichier1[i]
                            sentence2 = fichier2[jj]
                            sentence1 = arabic_reshaper.reshape(sentence1)
                            sentence2 = arabic_reshaper.reshape(sentence2)
                            sentence1 = algorithm.get_display(sentence1)
                            sentence2 = algorithm.get_display(sentence2)

                            sent1 = normalisation.tokenisation(sentence1)
                            sent2 = normalisation.tokenisation(sentence2)
                            sent1 = arabic_reshaper.reshape(sent1)
                            sent2 = arabic_reshaper.reshape(sent2)
                            sent1 = algorithm.get_display(sent1)
                            sent2 = algorithm.get_display(sent2)
                            cosWE, Tfminmax = getScore(sent1, sent2)

                            returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                            returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                            returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                            returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")

#-----------------------------------------------witth ponderation 0.3-0.7-----------------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 1) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 0):
            display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")

        #-----------------------with ponderation 0.2-0.8--------------------------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 1) & (
                returninterface.harm.get() == 0):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")
#------------------------------------------------------with harmonic-----------------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 1):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

            #------------------------------------- ponderation 0.3-0.7 with harmonic-----------------------
        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 1) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 1):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)
                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

#-------------------------------------ponderation 0.2-0.8 with harmonic--------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 1) & (
                returninterface.harm.get() == 1):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)
                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

        else:
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):

                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)
                    ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)
                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

###############################################################################################################################################
###############################################################################################################################################

def getsimilaritysent():
    if (returninterface.textareasent1.get("1.0", END) == ' ') or (returninterface.textareasent2.get("1.0", END) == ' '):
        messagebox.showinfo("ERROR!", "Your Field is Empty, You must Enter a sentence")

    else:
        returninterface.display.delete("1.0", END)
        sentence1 = returninterface.textareasent1.get("1.0", END)
        sentence2 = returninterface.textareasent2.get("1.0", END)

        sentence1 = arabic_reshaper.reshape(sentence1)
        sentence2 = arabic_reshaper.reshape(sentence2)
        sentence1 = algorithm.get_display(sentence1)
        sentence2 = algorithm.get_display(sentence2)

        sent1 = normaliser(sentence1)
        sent2 = normaliser(sentence2)
        sent1 = normalisation.tokenisation(sent1)
        sent2 = normalisation.tokenisation(sent2)
        sent1 = arabic_reshaper.reshape(sent1)
        sent2 = arabic_reshaper.reshape(sent2)
        sent1 = algorithm.get_display(sent1)
        sent2 = algorithm.get_display(sent2)

        if (returninterface.all.get() == 0) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (returninterface.e.get() == 0) & (
                returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 0):
            messagebox.showinfo('WARNING!', 'You must check similarity measurements')

#------------------------------------------all---------------------------------------------------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (returninterface.e.get() == 0) & (
                returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 0):
            returninterface.display.delete("1.0", END)
            simjaccard = jaccard(sent1, sent2)
            simdice = dice(sent1, sent2)
            simeuclid = euclidien(sent1, sent2)
            simjaro = jaro(sent1, sent2)
            simlevensh = levenshtein(sent1, sent2)

            cosWE, Tfminmax = getScore(sent1, sent2)

            arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
            arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

            ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)
            ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)
            harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

            returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
            returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
            returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
            returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
            returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
            returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
            returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
            returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
            returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
            returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")
            returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")
            returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

        # ----------------------------------------Only syntactic-------------------------------------------------------------------------------------------

        elif (returninterface.all.get() == 0) & (returninterface.j.get() == 1) & (returninterface.d.get() == 1) & (returninterface.l.get() == 1) & (returninterface.e.get() == 1) & (returninterface.ja.get() == 1) & (
                returninterface.e.get() == 1) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 0):
                    returninterface.display.delete("1.0", END)
                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")

        # -------------------only semantic-----------------------------------------------------------------------------------------------------------

        elif (returninterface.all.get() == 0) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 1) & (returninterface.tf.get() == 1) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 0):
                    returninterface.display.delete("1.0", END)
                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)
                    cosWE, Tfminmax = getScore(sent1, sent2)

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")

        # -----------------------------------------------witth ponderation 0.3-0.7-----------------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 1) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 0):
                    returninterface.display.delete("1.0", END)
                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")

        # -----------------------with ponderation 0.2-0.8--------------------------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 1) & (
                returninterface.harm.get() == 0):
                    returninterface.display.delete("1.0", END)
                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")

        # ------------------------------------------------------with harmonic-----------------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 1):
                    returninterface.display.delete("1.0", END)
                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

            # ------------------------------------- ponderation 0.3-0.7 with harmonic-----------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 1) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 1):
                    returninterface.display.delete("1.0", END)
                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)
                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

        # -------------------------------------ponderation 0.2-0.8 with harmonic--------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 1) & (
                returninterface.harm.get() == 1):
                    returninterface.display.delete("1.0", END)
                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)
                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                    returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                    returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                    returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                    returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                    returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                    returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                    returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                    returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                    returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")
                    returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

        else:
                returninterface.display.delete("1.0", END)
                simjaccard = jaccard(sent1, sent2)
                simdice = dice(sent1, sent2)
                simeuclid = euclidien(sent1, sent2)
                simjaro = jaro(sent1, sent2)
                simlevensh = levenshtein(sent1, sent2)

                cosWE, Tfminmax = getScore(sent1, sent2)

                arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)
                ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)
                harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                returninterface.display.insert(END, "Jaccard Similarity:  " + str(simjaccard) + "\n")
                returninterface.display.insert(END, "Dice Similarity:  " + str(simdice) + "\n")
                returninterface.display.insert(END, "Euclidean Similarity:  " + str(simeuclid) + "\n")
                returninterface.display.insert(END, "Jaro Similarity:  " + str(simjaro) + "\n")
                returninterface.display.insert(END, "Levenshtein Similarity:  " + str(simlevensh) + "\n")
                returninterface.display.insert(END, "Cos WE Similarity:  " + str(cosWE) + "\n")
                returninterface.display.insert(END, "Tf-MIN-MAX Similarity:  " + str(Tfminmax) + "\n")
                returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")
                returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")
                returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

############################################## ---------------- nettoyer text box ------------------- ##################################################################

def deletetxt():
    returninterface.display.delete("1.0", END)

########################################### save result to file ############################################################################################

def savetext():
    filename = filedialog.asksaveasfilename(defaultextension='.txt')
    f = open(filename, 'a')
    data = returninterface.display.get('1.0', 'end')
    data = arabic_reshaper.reshape(data)
    data = algorithm.get_display(data)
    f.write(data)
    f.close()
    messagebox.showinfo('FYI', 'File Saved')

################################# --- GET THE MOST SIMILAR --- #############################################################



def mostsimilar():
    selectpath1 = returninterface.path1.get()
    selectpath2 = returninterface.path2.get()
    if (len(selectpath1) == 0) or (len(selectpath2) == 0):
        messagebox.showinfo("ERROR!", "Your Field is Empty, You must select file")
    else:
        text1 = open(selectpath1, 'r', encoding="utf-8")
        f = text1.read()
        fichier1 = f.split("\n")
        text2 = open(selectpath2, 'r', encoding="utf-8")
        k = text2.read()
        fichier2 = k.split("\n")
        if (returninterface.all.get() == 0) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (returninterface.e.get() == 0) & (
                returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 0):
            messagebox.showinfo('WARNING!', 'You must check similarity measurements')

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (
                 returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 0):
            messagebox.showinfo('WARNING!', 'You must check ponderation 0.3-0.7 or ponderation 0.2-0.8 or harmonic avg measurements at once')

        elif (returninterface.all.get() == 0) & (returninterface.j.get() == 1) & (returninterface.d.get() == 1) & (returninterface.l.get() == 1) & (returninterface.e.get() == 1) & (returninterface.ja.get() == 1) & (
                    returninterface.e.get() == 1) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (
                         returninterface.harm.get() == 0):
            messagebox.showinfo('WARNING!', 'You must check semantic with ponderation 0.3-0.7 or ponderation 0.2-0.8 or harmonic avg measurements at once')

        elif (returninterface.all.get() == 0) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 1) & (returninterface.tf.get() == 1) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (
                returninterface.harm.get() == 0):
            messagebox.showinfo('WARNING!', 'You must check syntactic with ponderation 0.3-0.7 or ponderation 0.2-0.8 or harmonic avg measurements at once')

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                    returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 1) & (returninterface.pond2.get() == 0) & (
                    returninterface.harm.get() == 1):
            messagebox.showinfo('WARNING!', 'You must check ponderation 0.3-0.7 or harmonic avg measurements at once')

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                    returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 1) & (
                    returninterface.harm.get() == 1):
            messagebox.showinfo('WARNING!', 'You must check ponderation 0.2-0.8 or harmonic avg measurements at once')

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                    returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 1) & (returninterface.pond2.get() == 1) & (
                         returninterface.harm.get() == 0):
            messagebox.showinfo('WARNING!', 'You must check semantic with ponderation 0.3-0.7 or ponderation 0.2-0.8 at once')

#----------------------#### ----------- with harmonic ------------------###------------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 0) & (returninterface.harm.get() == 1):

            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])
                    harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])

                    if harmonicAvg >= 0.80 and harmonicAvg <= 1:
                        returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                        returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                        returninterface.display.insert(END, "Harmonic AVG:  " + str(harmonicAvg) + "\n")

                    elif 0.50 <= harmonicAvg < 0.80:
                        WriteInFIle.writeInFile("lowharmsim.txt", sentence1, 1)
                        WriteInFIle.writeInFile("lowharmsim.txt", sentence2, 1)
                        WriteInFIle.writeInFile("lowharmsim.txt", str(harmonicAvg), 1)
                        WriteInFIle.writeInFile("lowharmsim.txt", '\n', 1)

                    else:
                        WriteInFIle.writeInFile("poorharmsim.txt", sentence1, 1)
                        WriteInFIle.writeInFile("poorharmsim.txt", sentence2, 1)
                        WriteInFIle.writeInFile("poorharmsim.txt", str(harmonicAvg), 1)
                        WriteInFIle.writeInFile("poorharmsim.txt", '\n', 1)

#--------------------###---------------with ponderation 0.3-0.7--------------####--------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 1) & (returninterface.pond2.get() == 0) & (
                     returninterface.harm.get() == 0):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)

                    if ponderation1 >= 0.80 and ponderation1 <= 1:
                        returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                        returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                        returninterface.display.insert(END, "Ponderation (0.3-0.7):  " + str(ponderation1) + "\n")
                        returninterface.display.insert(END, "\n")


                    elif 0.50 <= ponderation1 < 0.80:
                        WriteInFIle.writeInFile("lowpond1sim.txt", sentence1, 1)
                        WriteInFIle.writeInFile("lowpond1sim.txt", sentence2, 1)
                        WriteInFIle.writeInFile("lowpond1sim.txt", str(ponderation1), 1)
                        WriteInFIle.writeInFile("lowpond1sim.txt", '\n', 1)

                    else:
                        WriteInFIle.writeInFile("poorpond1sim.txt", sentence1, 1)
                        WriteInFIle.writeInFile("poorpond1sim.txt", sentence2, 1)
                        WriteInFIle.writeInFile("poorpond1sim.txt", str(ponderation1), 1)
                        WriteInFIle.writeInFile("poorpond1sim.txt", '\n', 1)

# --------------------###---------------with ponderation 0.2-0.8--------------####--------------------------------------------

        elif (returninterface.all.get() == 1) & (returninterface.j.get() == 0) & (returninterface.d.get() == 0) & (returninterface.l.get() == 0) & (returninterface.e.get() == 0) & (returninterface.ja.get() == 0) & (
                returninterface.e.get() == 0) & (returninterface.cos.get() == 0) & (returninterface.tf.get() == 0) & (returninterface.pond1.get() == 0) & (returninterface.pond2.get() == 1) & (
                returninterface.harm.get() == 0):
            returninterface.display.delete("1.0", END)
            for i in range(len(fichier1) - 1):
                for jj in range(len(fichier2) - 1):
                    sentence1 = fichier1[i]
                    sentence2 = fichier2[jj]
                    sentence1 = arabic_reshaper.reshape(sentence1)
                    sentence2 = arabic_reshaper.reshape(sentence2)
                    sentence1 = algorithm.get_display(sentence1)
                    sentence2 = algorithm.get_display(sentence2)

                    sent1 = normalisation.tokenisation(sentence1)
                    sent2 = normalisation.tokenisation(sentence2)
                    sent1 = arabic_reshaper.reshape(sent1)
                    sent2 = arabic_reshaper.reshape(sent2)
                    sent1 = algorithm.get_display(sent1)
                    sent2 = algorithm.get_display(sent2)

                    simjaccard = jaccard(sent1, sent2)
                    simdice = dice(sent1, sent2)
                    simeuclid = euclidien(sent1, sent2)
                    simjaro = jaro(sent1, sent2)
                    simlevensh = levenshtein(sent1, sent2)

                    cosWE, Tfminmax = getScore(sent1, sent2)

                    arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])
                    arithmMoysemantic = statistics.mean([cosWE.item((0, 0)), Tfminmax.item((0, 0))])

                    ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)

                    if ponderation2 >= 0.80 and ponderation2 <= 1:
                        returninterface.display.insert(END, "First sentence:  " + sentence1 + "\n")
                        returninterface.display.insert(END, "second sentence:  " + sentence2 + "\n")
                        returninterface.display.insert(END, "Ponderation (0.2-0.8):  " + str(ponderation2) + "\n")
                        returninterface.display.insert(END, "\n")


                    elif 0.50 <= ponderation2 < 0.80:
                        WriteInFIle.writeInFile("lowpond2sim.txt", sentence1, 1)
                        WriteInFIle.writeInFile("lowpond2sim.txt", sentence2, 1)
                        WriteInFIle.writeInFile("lowpond2sim.txt", str(ponderation2), 1)
                        WriteInFIle.writeInFile("lowpond2sim.txt", '\n', 1)

                    else:
                        WriteInFIle.writeInFile("poorpond2sim.txt", sentence1, 1)
                        WriteInFIle.writeInFile("poorpond2sim.txt", sentence2, 1)
                        WriteInFIle.writeInFile("poorpond2sim.txt", str(ponderation2), 1)
                        WriteInFIle.writeInFile("poorpond2sim.txt", '\n', 1)

###############################################################################################################################
##########################################---INTERFACE---######################################################################
def returninterface(similarity):
    '''similarity = Tk()
    similarity.title("Similarity Measurments")
    similarity.geometry("600x600")
    similarity['bg'] = "white"'''
    #similarity.geometry("1200x1000")
    wrapper1 = LabelFrame(similarity, text="Similarity", width=630, height=680, bg="white",
                          font=("Times New Roman", "14", "bold"))
    wrapper1.place(x=20, y=20)
    
    canva2 = Canvas(wrapper1, width=575, height=200, bg="white")
    canva2.place(x=15, y=15)
    
    canva1 = Canvas(wrapper1, width=575, height=170, bg="white")
    canva1.place(x=15, y=240)
    
    labeltext = Label(canva1, text="Get similarity between two texts", bg="white", font=("Times New Roman", "10")).place(
        x=5, y=5)
    
    labopenfile = Label(canva1, text="first text", bg="white", font=("Times New Roman", "12", "bold")).place(x=10, y=40)
    openfirsttext = Button(canva1, text="Select", height=1, width=5, font=("Times New Roman", "10", "bold"),
                           command=openFIle1).place(x=100, y=40)
    returninterface.path1 = Entry(canva1, width=35)
    returninterface.path1.place(x=200, y=40)
    
    labopenfile = Label(canva1, text="second text", bg="white", font=("Times New Roman", "12", "bold")).place(x=10, y=100)
    opensecondtext = Button(canva1, text="Select", height=1, width=5, font=("Times New Roman", "10", "bold"),
                            command=openFile2)
    opensecondtext.place(x=100, y=97)
    returninterface.path2 = Entry(canva1, width=35)
    returninterface.path2.place(x=200, y=100)
    
    # -----------------------------------------------------------------------------------------------------
    
    
    # labeltext = Label(canva2, text="Similarity measurements", bg="white", font=("Times New Roman", "10")).place(x=5, y=5)
    
    labelsyntaxe = Label(canva2, text="Syntactic Similarity", bg="white", font=("Times New Roman", "13", "bold")).place(x=5,
                                                                                                                        y=5)

    returninterface.j = IntVar()
    jcrd = Checkbutton(canva2, text="Jaccard", bg="white", font=("Times New Roman", "10"), variable=returninterface.j, onvalue=1,
                       offvalue=0)
    jcrd.place(x=5, y=30)
    
    returninterface.d = IntVar()
    di = Checkbutton(canva2, text="Dice", bg="white", font=("Times New Roman", "10"), variable=returninterface.d, onvalue=1, offvalue=0)
    di.place(x=80, y=30)
    
    returninterface.l = IntVar()
    levensh = Checkbutton(canva2, text="Levenshtein", bg="white", font=("Times New Roman", "10"), variable=returninterface.l, onvalue=1,
                          offvalue=0)
    levensh.place(x=5, y=60)
    
    returninterface.ja = IntVar()
    jar = Checkbutton(canva2, text="Jaro", bg="white", font=("Times New Roman", "10"), variable=returninterface.ja, onvalue=1, offvalue=0)
    jar.place(x=110, y=60)
    
    returninterface.e = IntVar()
    euclid = Checkbutton(canva2, text="Euclidean Distance", bg="white", font=("Times New Roman", "10"), variable=returninterface.e,
                         onvalue=1, offvalue=0)
    euclid.place(x=5, y=90)
    
    labelsemantic = Label(canva2, text="Semantic Similarity", bg="white", font=("Times New Roman", "13", "bold")).place(
        x=250, y=5)
    
    returninterface.cos = IntVar()
    coswe = Checkbutton(canva2, text='Cosine WE', variable=returninterface.cos, onvalue=1, offvalue=0, bg="white",
                        font=("Times New Roman", "10"))
    coswe.place(x=250, y=40)
    
    returninterface.tf = IntVar()
    tfwe = Checkbutton(canva2, text="TF-MIN-MAX", variable=returninterface.tf, onvalue=1, offvalue=0, bg="white",
                       font=("Times New Roman", "10"))
    tfwe.place(x=250, y=70)
    
    labelpond = Label(canva2, text="Ponderation: ", bg="white", font=("Times New Roman", "11", "bold")).place(x=20, y=120)
    
    returninterface.pond1 = IntVar()
    pon1 = Checkbutton(canva2, text="0.3-0.7", variable=returninterface.pond1, onvalue=1, offvalue=0, bg="white",
                       font=("Times New Roman", "10"))
    pon1.place(x=20, y=145)
    
    returninterface.pond2 = IntVar()
    pon2 = Checkbutton(canva2, text="0.2-0.8", variable=returninterface.pond2, onvalue=1, offvalue=0, bg="white",
                       font=("Times New Roman", "10"))
    pon2.place(x=20, y=170)
    
    labelharm = Label(canva2, text="Harmonic AVG: ", bg="white", font=("Times New Roman", "11", "bold")).place(x=250, y=120)
    
    returninterface.harm = IntVar()
    harmavg = Checkbutton(canva2, text="Harmonic AVG", variable=returninterface.harm, onvalue=1, offvalue=0, bg="white",
                          font=("Times New Roman", "11", "bold"))
    harmavg.place(x=250, y=150)
    
    returninterface.all = IntVar()
    allsim = Checkbutton(canva2, text="ALL", bg="white", font=("Times New Roman", "10"), variable=returninterface.all, onvalue=1,
                       offvalue=0)
    allsim.place(x=420, y=60)
    
    simbtn = Button(canva1, text="Get Similarity", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1, width=10, command=getsimfiles)
    simbtn.place(x=200, y=130)
    
    mostsimbtn = Button(canva1, text="Most Similar", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1, width=10, command=mostsimilar)
    mostsimbtn.place(x=330, y=130)
    
    
    canva3 = Canvas(wrapper1, width=575, height=200, bg="white")
    canva3.place(x=15, y=430)
    
    labeltext = Label(canva3, text="Get similarity between two sentences", bg="white",
                      font=("Times New Roman", "10")).place(x=5, y=5)
    
    firstsent = Label(canva3, text="First sentence", bg="white", font=("Times New Roman", "10", "bold")).place(x=5, y=50)
    returninterface.textareasent1 = Text(canva3, width=40, height=3, wrap='none')
    returninterface.textareasent1.place(x=100, y=35)
    returninterface.textareasent1.tag_configure('tag-right', justify='right')
    
    add_bidi_support(returninterface.textareasent1)
    
    secondsent = Label(canva3, text="Second sentence", bg="white", font=("Times New Roman", "10", "bold")).place(x=5, y=150)
    returninterface.textareasent2 = Text(canva3, width=40, height=3, wrap='none')
    returninterface.textareasent2.place(x=100, y=130)
    returninterface.textareasent2.tag_configure('tag-right', justify='right')
    add_bidi_support(returninterface.textareasent2)
    
    Button(canva3, text="Get Similarity", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1, width=10, command=getsimilaritysent).place(x=450, y=100)
    
    wrapper2 = LabelFrame(similarity, text="Result", width=630, height=680, bg="white",
                          font=("Times New Roman", "14", "bold"))
    wrapper2.place(x=680, y=20)
    
    returninterface.display = Text(wrapper2, width=74, height=33, wrap='none')
    returninterface.display.place(x=15, y=15)
    returninterface.display.tag_configure('tag-right', justify='right')
    
    canva4 = Canvas(wrapper2, width=600, height=60, bg="white")
    canva4.place(x=15, y=590)
    
    savesimilaritysent = Button(canva4, text="Save", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1,
                                width=10, command=savetext).place(x=130, y=15)
    deletezonesent = Button(canva4, text="Delete", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1,
                            width=10, command=deletetxt).place(x=250, y=15)
    cancel = Button(canva4, text="Cancel", bg="#0da5c4", font=("Times New Roman", "12", "bold"), height=1, width=10,
                    command=similarity.quit).place(x=370, y=15)
    #similarity.mainloop()
    return similarity

#returninterface()