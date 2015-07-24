##########################################
#           Nikola Radmanovic            #
#      http://www.github.com/Radmanovic  #
#                2015                    #
##########################################

from Tkinter import *

root = Tk()
#Naziv
root.title("Prosek v0.0.1")
naslov = Label(root, text="Prosek v0.0.1")
gornjiOkvir = Frame(root)
gornjiOkvir.grid()
donjiOkvir = Frame(root)
donjiOkvir.grid(row=10, column=7)

#Izgled
dugme_1 = Button(gornjiOkvir, text="Prosek", fg="green")
dugme_2 = Button(gornjiOkvir, text="Sacuvaj", fg="blue")
dugme_3 = Button(donjiOkvir, text="Izadji", fg="red")


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
Predmet_3 = Label(root, text="II Strani Jezik")
#Prikazuje i pozicionira
dugme_1.grid()
dugme_2.grid()
dugme_3.grid()
naslov.grid()
#Labeli Grid
Label_1.grid(row=0)
Label_2.grid(row=1)
Label_3.grid(row=20, column=9)
Label_4.grid()
Label_5.grid()
Label_6.grid()
Label_7.grid()
#Predmeti Labeli Grid
Predmet_1.grid()
Predmet_2.grid()
Predmet_3.grid()
root.mainloop()
