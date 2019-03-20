import math
Ligne=16
Colonne=16
def perimetre_vision(per,i,j, cible,Terrain) : #s'applique sur un animal de position (i,j) qui cherche une proie de valeur cible
    temp=[]
    npsh =0
    npsd =0
    npsg =0
    npsb =0
    if i-per<0 :
        npsg=abs(i-per)      #npsg : ne pas sortir à gauche
    if i+per>len(Terrain[0]) :
        npsd = i+per-len(Terrain[0])     #npsd : ne pas sortir à droite
    if j-per<0 :
        npsh=abs(j-per)                 #npsh : ne pas sortir en haut
    if j+per>len(Terrain) :
        npsb = j+per-len(Terrain)      #npsb : ne pas sortir en bas
    for ligne in range(i-per+npsg,i+per-npsd-1):
        for colonne in range(j-per+npsh, j+per-npsb+1):
            #print("ligne :",ligne,"colonne :",colonne,"valeur :",Terrain[ligne,colonne])
            if Terrain[ligne,colonne]==cible :
                if len(temp)==0 :
                    temp=[ligne, colonne]
                if math.sqrt((i-ligne)**2+(j-colonne)**2)<math.sqrt((i-temp[0])**2+(j-temp[1])**2) :
                    temp=[ligne, colonne]
    return temp

#len b[]=nb de colonne et len b=nb de ligne