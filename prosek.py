##########################################
#           Nikola Radmanovic            #
#      http://www.github.com/Radmanovic  #
#                2015                    #
##########################################

from Tkinter import *

root = Tk()
#Naziv
root.title("Prosek v0.0.1")
gornjiOkvir = Frame(root)
gornjiOkvir.pack()
donjiOkvir = Frame(root)
donjiOkvir.pack(side=BOTTOM)

#Izgled
dugme1 = Button(gornjiOkvir, text="Prosek", fg="green")
dugme2 = Button(gornjiOkvir, text="Sacuvaj", fg="blue")
dugme3 = Button(donjiOkvir, text="Izadji", fg="red")

#Prikazuje i pozicionira
dugme1.pack(side="left")
dugme2.pack(side="left")
dugme3.pack(side="bottom")

root.mainloop()