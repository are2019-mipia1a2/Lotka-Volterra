import numpy as np
import matplotlib.pyplot as plt  
import random
Ligne = 16
Colonne = 16
plaine =('oifdnzoenfze',2/5)
montagne=('ppp',1/8)
foret=('ppp',1/3)
environnement=montagne
List_number_species=[16,16,16]
#Terrain nature uniquement début:
def basea (ligne, colonne) :
    base=[]
    basetemp=[]
    for _ in range(colonne//4):
        for _ in range(ligne//4):
            basetemp.append(1)
        base.append(basetemp)
        basetemp=[]
    base=np.reshape(np.asarray(base),(ligne//4, colonne//4))
    return base
base=basea(Ligne,Colonne)

def terrain_base(environnement, ligne, colonne) :
    """crée la matrice terrain base"""
    A=[]
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    tempA=[]
    for x in range(ligne//4) :
        for y in range (colonne//4) :
            if x != y :
                a.append(0)
                c.append(0)
                d.append(0)
                b.append(0)
                e.append(0)
                f.append(0)
                g.append(0)
                h.append(0)
            else : 
                a.append(randomi(environnement))
                b.append(randomi(environnement))
                c.append(randomi(environnement))
                d.append(randomi(environnement))
                
    
    a=(np.reshape(np.asarray(a),(ligne//4,colonne//4))).dot(base)
    if random.random()<0.5 :
        a=np.transpose(a)
    b=(np.reshape(np.asarray(b),(ligne//4,colonne//4))).dot(base)
    if random.random()<0.5 :
        b=np.transpose(b)
    c=(np.reshape(np.asarray(c),(ligne//4,colonne//4))).dot(base)
    if random.random()<0.5 :
        c=np.transpose(c)
    d=(np.reshape(np.asarray(d),(ligne//4,colonne//4))).dot(base)
    if random.random()<0.5 :
        d=np.transpose(d)
    tempA=np.concatenate((a,b),axis=1)
    tempB=np.concatenate((c,d),axis=1)
    A=np.concatenate((tempA,tempB),axis=0)
    return A

def randomi(environnement) :
    _, a=environnement
    if a<random.random() :
        return 1
    else : 
        return 0
    
def terrain_final(environnement,ligne,colonne) :
    return np.concatenate((np.concatenate((terrain_base(environnement, ligne, colonne),terrain_base(environnement, ligne, colonne)),axis=1),np.concatenate((terrain_base(environnement, ligne, colonne),terrain_base(environnement, ligne, colonne)),axis=1)),axis=0)
#Terrain nature uniquement fin
    
#Terrain animal uniquement :
def create_empty_land(n):   #matrice avec que des 0
    L= []
    for i in range(n):
        L1 = []
        for i in range(n):
            L1.append(0)
        L.append(L1)
    return L

def create_occupied_land(n, m, signature):  #ajoute à une matrice m, n éléments de valeur signature
    Empty_matrix = m
    k = len(m)
    for i in range(n):
        a = random.randint(0, k-1)
        b = random.randint(0, k-1)
        while Empty_matrix[a][b] != 0:
            a = random.randint(0, k-1)
            b = random.randint(0, k-1)
        Empty_matrix[a][b] = signature
    return Empty_matrix

def create_occupied_land_ecosystem(List_number_species, List_of_signatures, m):     #crée la matrice animale avec : list_number_species est le nombre d'animaux voulu par espece 
    """len(List_of_species == len(List_of_signature)"""                             #List_of_signatures : le valeur de l'espece dans la matrice
                                                                                    #m : la dimension du terrain
    General_ecosystem_matrix = create_empty_land(m)
    for i in range(len(List_number_species)):
       General_ecosystem_matrix = create_occupied_land(List_number_species[i], General_ecosystem_matrix, List_of_signatures[i])
       print(General_ecosystem_matrix)
    General_ecosystem_matrix = np.reshape(np.asarray(General_ecosystem_matrix), (m, m))
    return General_ecosystem_matrix

#Terrain animal uniquement fin

#Terrain : create_occupied_land_ecosystem
def creatdict_esp2(terrain):    #dictionnaire de l'espece 2 uniquement
    desp2=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==2 :
                desp2[str(i)+'-'+str(j)]=[1,80]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp2

def creatdict_esp3(terrain):    #dictionnaire de l'espece 3 uniquement
    desp3=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==2 :
                desp3[str(i)+'-'+str(j)]=[1,80]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp3

def creatdict_esp4(terrain):    #dictionnaire de l'espece 3 uniquement
    desp4=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==2 :
                desp4[str(i)+'-'+str(j)]=[1,80]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp4

def creatdict_plant(terrain):    #dictionnaire des plantes uniquement, Terrain : terrain_final
    dplant=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==1 :
                dplant[str(i)+'-'+str(j)]=100
    return dplant

def Merge_matrix(M1, M2):
    L = []
    L_1 = []
    for i in range(len(M1)):
        L_1 = []
        for j in range(len(M1[i])):
            L_temp = []
            L_temp.append(M1[i][j])
            L_temp.append(M2[i][j])
            L_1.append(L_temp)
        L.append(L_1)
    L = np.reshape(np.asarray(L), (len(M1), len(M2), 2))
    return L

def affichage(matrice) :
    """permet d'afficher le terrain uniquement"""
    img=[]
    for j in matrice :
       temp=[]
       for k in j :
           i=0
           for e in k:
               if e>i:
                   i=e  
           if i==0:
                temp.append((51,153,0))  #vert
           elif i==1:
                temp.append((255, 255, 0))  #jaune
           elif i==2:
                temp.append((204,153,51))  #marron
           elif i==3:
                temp.append((128,0,128)) #violet
           elif i==4:
                temp.append((192, 192, 192))    #gris
       img.append(temp)      
    plt.imshow(img)
    plt.show()
    return 

Terrain_plante=terrain_final(environnement,Ligne,Colonne)
Terrain_especes= create_occupied_land_ecosystem(List_number_species, [2,3,4], Ligne)
dict_plante=creatdict_plant(Terrain_plante)
dict_esp2=creatdict_esp2(Terrain_especes)
dict_esp3=creatdict_esp3(Terrain_especes)
dict_esp4=creatdict_esp4(Terrain_especes)
Terrain_final=Merge_matrix(Terrain_plante, Terrain_especes)