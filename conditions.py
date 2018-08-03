#on cree une variable qui est egal a 5
boite = 5

#si la variable de boite est plus grand que 10
if boite > 10 :
    #on affiche "plus grand"
    print("plus grand")

    #sinon, si la variable de boite est plus eptit que 10
elif boite < 10 :
    #on affiche "plus petit" 
    print("plus petit")

    #sinon, en definitif, c'est que la variable est egale
else:
    print("egal")


#------------------
#exemple 2 on garde le reste de la division (le modulo) de 52/2 
#et on stoque le resultat dans la variable boite
boite = 52 % 2

#si le contenu de la variable boite est egal a zero
#ATTENTION, double = quand on compare 2 elements
if boite == 0 :
    print("c'est un chiffre pair ?")