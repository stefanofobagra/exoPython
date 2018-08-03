#depuis la bibliotheque random, on importe la fonction "randrange" 
#qui permet de recuperer un chiffre aleatoire
from random import randrange
chiffre = randrange(100)

#on cree une variable boolean trouver qui vaut FAUX
trouver = False

#tant que trouver est egal a FAUX, on continue la boucle
while trouver == False :
    a = int(input("Entrez un chiffre : "))
    if a < chiffre:
        print("le chiffre est plus grand")
    elif a > chiffre:
        print("le chiffre est plus petit")
    else:
        print("Bravo !")
        #si on a trouve, il faut penser a changer la valeur de notre "Flag" trouver qui passe a VRAI
        trouver = True