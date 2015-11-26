##########################################
#           Nikola Radmanovic            #
#      http://www.github.com/radmanovic  #
#                2015                    #
##########################################

#Skole

skole = ["Gimnazije", "Strucne skole", "Umetnicke skole"]

#/Skole#

#Smerovi

skole[0] = ["Prirodno matematicki", "Drustveno-jezicki", "Opsti"]

skole[1] = ["Komercijalista", "Turisticki tehnicar", "Masinski tehnicar"]

#/Smerovi#

#Predmeti

#Gimnazije predmeti

#Prirodno matematicki smer
skole[0][0] = ["Matematika",
               "Srpski jezik",
               "Hemija",
               "Strani jezik",
               "Engleski"]

#Drustveno-jezicki smer
skole[0][1] = ["Matematika",
               "Srpski jezik",
               "Hemija",
               "Strani jezik",
               "Engleski",
               "Latinski jezik"]

#Opsti smer
skole[0][2] = ["Matematika",
               "Srpski jezik",
               "Hemija",
               "Strani jezik",
               "Engleski"]

#/Gimnazije predmeti#

#/Predmeti#

#Izborni predmeti
izborni = ["Verska nastava", "Gradjanska nastava"]
#/Izborni predmeti#

#Funkcije
skole[0][0][0] = input("Unesite ocenu iz matematike")
print(skole[0][0][0])

#/Funkcije#
# Repository location https://github.com/radmanovic/prosek #
