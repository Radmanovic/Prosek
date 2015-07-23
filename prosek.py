##########################################
#           Nikola Radmanovic            #
#      http://www.github.com/Radmanovic  #
#                2015                    #
##########################################

from Tkinter import *

root = Tk()
#Naziv
root.title("Prosek v0.0.1")
naslov = Label(root, text="Prosek v0.0.1", bg="grey", fg="white")
gornjiOkvir = Frame(root)
gornjiOkvir.pack()
donjiOkvir = Frame(root)
donjiOkvir.pack(side=BOTTOM)

#Izgled
dugme1 = Button(gornjiOkvir, text="Prosek", fg="green")
dugme2 = Button(gornjiOkvir, text="Sacuvaj", fg="blue")
dugme3 = Button(donjiOkvir, text="Izadji", fg="red")


#Labeli
Label_1 = Label(root, text="Ime i Prezime")
Label_2 = Label(root, text="Razredni Staresina")
Label_3 = Label(root, text="Skolska Godina")
Label_4 = Label(root, text="Ime Skole")
Label_5 = Label(root, text="Mesto")
Label_6 = Label(root, text="Opstina")
Label_7 = Label(root, text="Zemlja")
#Predmet Labeli
Predmet_1 = Label(root, text="Maternji jezik")
Predmet_2 = Label(root, text="I Strani Jezik")
#Prikazuje i pozicionira
dugme1.pack(side="left")
dugme2.pack(side="left")
dugme3.pack(side="bottom")
naslov.pack(side="bottom")
#Labeli Pack
Label_1.pack()
Label_2.pack()
Label_3.pack()
Label_4.pack()
Label_5.pack()
Label_6.pack()
Label_7.pack()
#Predmeti Labeli Pack
Predmet_1.pack()
Predmet_2.pack()
root.mainloop()
