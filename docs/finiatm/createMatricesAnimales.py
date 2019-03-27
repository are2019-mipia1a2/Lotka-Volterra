#Terrain : create_occupied_land_ecosystem
def creatdesp2(terrain):    #dictionnaire de l'espece 2 uniquement
    desp2=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==2 :
                desp2[str(i)+'-'+str(j)]=[1,80]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp2

def creatdesp3(terrain):    #dictionnaire de l'espece 3 uniquement
    desp3=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==2 :
                desp3[str(i)+'-'+str(j)]=[1,80]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp3

def creatdesp4(terrain):    #dictionnaire de l'espece 3 uniquement
    desp4=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==2 :
                desp4[str(i)+'-'+str(j)]=[1,80]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp4