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

dict1={"ab":3,"aa":4}
dict2={"ab":3,"aa":4}
dict3={"ab":3,"aa":4}

def deplacement1(i,j,per, cible, Terrain):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            dict1[str(i+1)+"-"+str(j)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i+1,j].append(2)
        else :
            dict1[str(i-1)+"-"+str(j)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i-1,j].append(2)
    if k[1]==j :
        if k[0]>i :
            dict1[str(i)+"-"+str(j+1)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i,j+1].append(2)
        else :
            dict1[str(i)+"-"+str(j-1)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i,j-1].append(2)
    if k[0]<i :
        if k[i]<j :
            dict1[str(i-1)+"-"+str(j-1)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i-1,j-1].append(2)
        else : 
            dict1[str(i-1)+"-"+str(j+1)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i-1,j+1].append(2)
    else :
        if k[i]>j :
            dict1[str(i+1)+"-"+str(j+1)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i+1,j+1].append(2)
        else :
            dict1[str(i+1)+"-"+str(j-1)]=dict1.pop[str(i),str(j)]
            Terrain[i,j].remove(2)
            Terrain[i+1,j-1].append(2)

def deplacement2(i,j,per, cible, Terrain):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            dict2[str(i+1)+"-"+str(j)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i+1,j].append(3)
        else :
            dict2[str(i-1)+"-"+str(j)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i-1,j].append(3)
    if k[1]==j :
        if k[0]>i :
            dict2[str(i)+"-"+str(j+1)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i,j+1].append(3)
        else :
            dict2[str(i)+"-"+str(j-1)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i,j-1].append(3)
    if k[0]<i :
        if k[i]<j :
            dict2[str(i-1)+"-"+str(j-1)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i-1,j-1].append(3)
        else : 
            dict2[str(i-1)+"-"+str(j+1)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i-1,j+1].append(3)
    else :
        if k[i]>j :
            dict2[str(i+1)+"-"+str(j+1)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i+1,j+1].append(3)
        else :
            dict2[str(i+1)+"-"+str(j-1)]=dict2.pop[str(i),str(j)]
            Terrain[i,j].remove(3)
            Terrain[i+1,j-1].append(3)
            

def deplacement3(i,j,per, cible, Terrain):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            dict3[str(i+1)+"-"+str(j)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i+1,j].append(4)
        else :
            dict3[str(i-1)+"-"+str(j)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i-1,j].append(4)
    if k[1]==j :
        if k[0]>i :
            dict3[str(i)+"-"+str(j+1)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i,j+1].append(4)
        else :
            dict3[str(i)+"-"+str(j-1)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i,j-1].append(4)
    if k[0]<i :
        if k[i]<j :
            dict3[str(i-1)+"-"+str(j-1)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i-1,j-1].append(4)
        else : 
            dict3[str(i-1)+"-"+str(j+1)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i-1,j+1].append(4)
    else :
        if k[i]>j :
            dict3[str(i+1)+"-"+str(j+1)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i+1,j+1].append(4)
        else :
            dict3[str(i+1)+"-"+str(j-1)]=dict3.pop[str(i),str(j)]
            Terrain[i,j].remove(4)
            Terrain[i+1,j-1].append(4)
            
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

def predation(d_pred,d_cible,cible,i,j,pos_cible_i,pos_cible_j,terrain):
    d_pred[str(i)+"-"+str(j)][1]+=20
    del d_cible[str(pos_cible_i)+"-"+str(pos_cible_j)]
    terrain[pos_cible_i,pos_cible_j].remove(cible)
    return
def predation_plant(d_pred,i,j,pos_cible_i,pos_cible_j):
    d_pred[str(i)+"-"+str(j)][1]+=20
    dict_plante[pos_cible_i,pos_cible_j]+=-20
    return

def reproduction(espece,d_pred,i,j,pos_cible_i,pos_cible_j,terrain) :
    if i==pos_cible_i :
        if terrain[i+1,j]==[0] :
            d_pred[str(i+1)+"-"+str(j)]=[1,80]
            terrain[i+1,j].append(espece)
        elif terrain[i+1,pos_cible_j]==[0] :
            d_pred[str(i+1)+"-"+str(pos_cible_j)]=[1,80]
            terrain[i+1,pos_cible_j].append(espece)
        elif terrain[i-1,j]==[0] :
            d_pred[str(i-1)+"-"+str(j)]=[1,80]
            terrain[i-1,j].append(espece)
        elif terrain[i-1,pos_cible_j]==[0] :
            d_pred[str(i-1)+"-"+str(pos_cible_j)]=[1,80]
            terrain[i-1,pos_cible_j].append(espece)
    if j==pos_cible_j :
        if terrain[i,j+1]==[0] :
            d_pred[str(i)+"-"+str(j+1)]=[1,80]
            terrain[i,j+1].append(espece)
        elif terrain[pos_cible_i,j+1]==[0] :
            terrain[pos_cible_i,j+1].append(espece)
            d_pred[str(pos_cible_i)+"-"+str(j+1)]=[1,80]
        elif terrain[i,j-1]==[0] :
            d_pred[str(i)+"-"+str(j-1)]=[1,80]
            terrain[i,j-1].append(espece)
        elif terrain[pos_cible_i,j-1]==[0] :
            d_pred[str(pos_cible_i)+"-"+str(j-1)]=[1,80]
            terrain[pos_cible_i,j-1].append(espece)
    if i==pos_cible_i+1 :
        if j==pos_cible_j+1 :
            if terrain[i+1,j]==[0] :
                d_pred[str(i+1)+"-"+str(j)]=[1,80]
                terrain[i+1,j].append(espece)
            elif terrain[i,j+1]==[0] :
                d_pred[str(i)+"-"+str(j+1)]=[1,80]
                terrain[i,j+1].append(espece)
    if i==pos_cible_i-1 :
        if j==pos_cible_j+1 :
            if terrain[i-1,j]==[0] :
                d_pred[str(i-1)+"-"+str(j)]=[1,80]
                [i-1,j].append(espece)
            elif terrain[i,j+1]==[0] :
                d_pred[str(i)+"-"+str(j+1)]=[1,80]
                terrain[i,j+1].append(espece)
    return

def decompo_coords(a) :
    temp1=""
    res=[]
    for k in a :
        if k!="-" :
            temp1+=str(k)
            print(k)
        if k=="-" :
            res.append(int(temp1))
            temp1=""
            print(k)
    res.append(int(temp1))
    return res

def final(n) :
    for _ in range(n):
        for e2 in dict_esp2 :
            if e2[0]>=8 :
                del(dict_esp2(e2))
                Terrain_final[decompo_coords(e2)[0],decompo_coords(e2)[1]].remove(2)
            elif e2[1]<=20 :
                if math.sqrt((perimetre_vision(1,decompo_coords(e2)[0],decompo_coords(e2)[1],1,Terrain_final)[0]-decompo_coords(e2)[0])**2+(perimetre_vision(1,decompo_coords(e2)[0],decompo_coords(e2)[1],1,Terrain_final)[1]-decompo_coords(e2)[1])**2)<=math.sqrt(2) :
                    predation_plant(dict_esp2,decompo_coords(e2)[0],decompo_coords(e2)[1],perimetre_vision(1,decompo_coords(e2)[0],perimetre_vision(1,decompo_coords(e2)[1])))
                else :
                    deplacement1(decompo_coords(e2)[0],decompo_coords(e2)[1],6, 1, Terrain_final)
            elif e2[0]>=2 :
                if math.sqrt((perimetre_vision(1,decompo_coords(e2)[0],decompo_coords(e2)[1],2,Terrain_final)[0]-decompo_coords(e2)[0])**2+(perimetre_vision(1,decompo_coords(e2)[0],decompo_coords(e2)[1],2,Terrain_final)[1]-decompo_coords(e2)[1])**2)<=math.sqrt(2) :
                    reproduction(2,dict_esp2,decompo_coords(e2)[0],decompo_coords(e2)[1],perimetre_vision(1,decompo_coords(e2)[0],perimetre_vision(1,decompo_coords(e2)[1],Terrain_final)))
                else :
                    deplacement1(decompo_coords(e2)[0],decompo_coords(e2)[1],6, 1, Terrain_final)
            e2[0]+=1
                
                
                
                