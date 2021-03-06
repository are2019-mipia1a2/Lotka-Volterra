import numpy as np
import matplotlib.pyplot as plt  
import random
import math
Ligne = 16
Colonne = 16
plaine =('oifdnzoenfze',2/5)
montagne=('ppp',1/8)
foret=('ppp',1/3)
environnement=montagne
List_number_species=[7,7,7]
age_max_esp2=8
age_max_esp3=10
age_max_esp4=12
per_2 =20
per_3=40
per_4=60
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
    General_ecosystem_matrix = np.reshape(np.asarray(General_ecosystem_matrix), (m, m))
    return General_ecosystem_matrix

#Terrain animal uniquement fin

#Terrain : create_occupied_land_ecosystem
def creatdict_esp2(Terrain):    #dictionnaire de l'espece 2 uniquement
    desp2=dict()
    for i in range(len(Terrain)) :
        for j in range(len(Terrain[i])) :
            if Terrain[i][j]==2 :
                desp2[i,j]=[1,80]
    return desp2
def creatdict_esp3(Terrain):    #dictionnaire de l'espece 3 uniquement
    desp3=dict()
    for i in range(len(Terrain)) :
        for j in range(len(Terrain[i])) :
            if Terrain[i][j]==3 :
                desp3[i,j]=[1,80]       #1er elmt : âge 2eme elmt : jauge de faim
    return desp3

def creatdict_esp4(terrain):    #dictionnaire de l'espece 3 uniquement
    desp4=dict()
    for i in range(len(terrain)) :
        for j in range(len(terrain[i])) :
            if terrain[i][j]==4 :
                desp4[i,j]=[1,80]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp4

def creatdict_plant(terrain):    #dictionnaire des plantes uniquement, Terrain : terrain_final
    dplant=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==1 :
                dplant[i,j]=100
    return dplant

def Merge_matrix(M1, M2):
    L = []
    L_1 = []
    for i in range(len(M1)):
        L_1 = []
        for j in range(len(M1[i])):
            L_temp = []
            if M2[i][j] != 0:
                L_temp.append(M2[i][j])
            L_temp.append(M1[i][j])
            L_1.append(L_temp)
        L.append(L_1)
    L = np.reshape(np.asarray(L), (len(M1), len(M2)))
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

def deplacement(i,j,per, cible, Terrain,dict_esp,esp):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]>i :
        if k[1]>j :
            dict_esp[i+1,j+1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+1,j+1].append(esp)
        elif k[1]<j :
            dict_esp[i+1,j-1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+1,j-1].append(esp)
        else :
            dict_esp[i+1,j]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+1,j].append(esp)
            
    elif k[0]<i :
        if k[1]>j :
            dict_esp[i-1,j+1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j+1].append(esp)
        elif k[1]<j :
            dict_esp[i-1,j-1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j-1].append(esp)
        else :
            dict_esp[i-1,j]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j].append(esp)
    elif k[0]==i :
        if k[1]<j :
            dict_esp[i,j-1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i,j-1].append(esp)
        else : 
            dict_esp[i,j+1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i,j+1].append(esp)
            
def deplacement2(i,j,per, cible, Terrain,dict_esp,esp):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            dict_esp[i+1,j]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+1,j].append(esp)
        else :
            dict_esp[i-1,j]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j].append(esp)
    elif k[1]==j :
        if k[0]>i :
            dict_esp[i,j+1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i,j+1].append(esp)
        else :
            dict_esp[i,j-1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i,j-1].append(esp)
    elif k[0]<i :
        if k[1]<j :
            dict_esp[i-1,j-1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j-1].append(esp)
        else : 
            dict_esp[i-1,j+1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j+1].append(esp)
    else : #k[0]>i
        if k[1]>j :
            dict_esp[i+1,j+1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+1,j+1].append(esp)
        else :
            dict_esp[i+1,j-1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+1,j-1].append(esp)

def perimetre_vision(per,i,j, cible,Terrain) : #s'applique sur un animal de position (i,j) qui cherche une proie de valeur cible
    temp=[]
    npsh =0
    npsd =0
    npsg =0
    npsb =0
    if i-per<0 :
        npsg=per-i      #npsg : ne pas sortir à gauche
    if i+per>len(Terrain[0]) :
        npsd = i+per-len(Terrain[0])     #npsd : ne pas sortir à droite
    if j-per<0 :
        npsh=per-j                 #npsh : ne pas sortir en haut
    if j+per>len(Terrain) :
        npsb = j+per-len(Terrain)      #npsb : ne pas sortir en bas
    for ligne in range(i-per+npsg,i+per-npsd):
        for colonne in range(j-per+npsh, j+per-npsb):
            #print("ligne :",ligne,"colonne :",colonne,"valeur :",Terrain[ligne,colonne])
            if cible in Terrain[ligne][colonne] :
                if len(temp)==0 :
                    temp=[ligne, colonne]
                if math.sqrt((i-ligne)**2+(j-colonne)**2)<math.sqrt((i-temp[0])**2+(j-temp[1])**2) :
                    temp=[ligne, colonne]
    if len(temp)==0 :
        temp=[0,0]
    return temp

def predation(d_pred,d_cible,cible,i,j,pos_cible_i,pos_cible_j,terrain):
    d_pred[i,j][1]+=20
    del d_cible[pos_cible_i,pos_cible_j]
    terrain[pos_cible_i,pos_cible_j].remove(cible)
    return
def predation_plant(d_pred,i,j,pos_cible_i,pos_cible_j):
    d_pred[i,j][1]+=20
    dict_plante[pos_cible_i,pos_cible_j]+=-20
    return

def reproduction(espece,d_pred,i,j,pos_cible_i,pos_cible_j,terrain) :
    if i==pos_cible_i :
        if i!=len(terrain[0])-1:
            if terrain[i+1,j]==[0] :
                d_pred[i+1,j]=[1,80]
                terrain[i+1,j].append(espece)
            elif terrain[i+1,pos_cible_j]==[0] :
                d_pred[i+1,pos_cible_j]=[1,80]
                terrain[i+1,pos_cible_j].append(espece)
        if i!=0:
            if terrain[i-1,j]==[0] :
                d_pred[i-1,j]=[1,80]
                terrain[i-1,j].append(espece)
            elif terrain[i-1,pos_cible_j]==[0] :
                d_pred[i-1,pos_cible_j]=[1,80]
                terrain[i-1,pos_cible_j].append(espece)
    if j==pos_cible_j :
        if j!=len(terrain)-1:
            if terrain[i,j+1]==[0] :
                d_pred[i,j+1]=[1,80]
                terrain[i,j+1].append(espece)
            elif terrain[pos_cible_i,j+1]==[0] :
                terrain[pos_cible_i,j+1].append(espece)
                d_pred[pos_cible_i,j+1]=[1,80]
        if j!=0 :
            if terrain[i,j-1]==[0] :
                d_pred[i,j-1]=[1,80]
                terrain[i,j-1].append(espece)
            elif terrain[pos_cible_i,j-1]==[0] :
                d_pred[pos_cible_i,j-1]=[1,80]
                terrain[pos_cible_i,j-1].append(espece)
    if i==pos_cible_i+1 :
        if j==pos_cible_j+1 :
            if i!=len(terrain)-1 :
                if terrain[i+1,j]==[0] :
                    d_pred[i+1,j]=[1,80]
                    terrain[i+1,j].append(espece)
            if j!=len(terrain)-1:
                if terrain[i,j+1]==[0] :
                    d_pred[i,j+1]=[1,80]
                    terrain[i,j+1].append(espece)
    if i==pos_cible_i-1 :
        if j==pos_cible_j+1 :
            if i !=0 :
                if terrain[i-1,j]==[0] :
                    d_pred[i-1,j]=[1,80]
                    terrain[i-1,j].append(espece)
            if j!=len(terrain)-1:
                if terrain[i,j+1]==[0] :
                    d_pred[i,j+1]=[1,80]
                    terrain[i,j+1].append(espece)
    return

#def deplacement_random (i,j, dict_esp,esp,Terrain) :
 #   if i==len(Terrain) and j==len(Terrain)[0]:
  #      a=random.randint(-1,0)
  ##      a=random.randint(-1,0)
    #     b=random.randint(-1,0)
       #   
        
   # a=random.randint(-1,1)
   # b=random.randint(-1,1)
    #while len(Terrain_final[i+a,j+b])!= 1:
     #   a=random.randint(-1,1)
      #  b=random.randint(-1,1)
  #  dict_esp[i+a,j+b]=dict_esp.pop[i,j]
   # Terrain[i,j].remove(esp)
    #Terrain[i+a,j+b].append(esp)
    #Terrain[i+a,j+b].append(esp)
    #return
def decompo_coords(a) :
    temp1=""
    res=[]
    for k in a :
        if k!="-" :
            temp1+=str(k)
        if k=="-" :
            res.append(int(temp1))
            temp1=""
    res.append(int(temp1))
    return res
def autretest() :
    for e4 in list(dict_esp4) :
        print(e4)
        print(Terrain_final[e4])
        Terrain_final[e4].remove(4)
        print(Terrain_final[e4])
    return
def final(n) :
    for _ in range(n):
        print(n)
        for e4 in list(dict_esp4) :
            if dict_esp4[e4][0]>=age_max_esp4 :           #Si l'animal est trop vieux
                del dict_esp4[e4]
                Terrain_final[e4].remove(4)
                continue
            elif dict_esp4[e4][1] == 0 :         #Si l'animal meurt de faim
                del dict_esp4[e4]
                Terrain_final[e4].remove(4)
                continue
            dict_esp4[e4][0]+=1
            if dict_esp4[e4][1]<=20 :        #Si l'animal a faim
              dict_esp4[e4][1]-=20  
              if perimetre_vision(1,e4[0],e4[1],3,Terrain_final)[0]!=0 and math.sqrt((perimetre_vision(1,e4[0],e4[1],3,Terrain_final)[0]-e4[0])**2+(perimetre_vision(1,e4[0],e4[1],3,Terrain_final)[1]-e4[1])**2)<=math.sqrt(2) :
                 predation(dict_esp4, dict_esp3, 3, e4[0],e4[1],perimetre_vision(1,e4[0],e4[1],3,Terrain_final)[0],perimetre_vision(1,e4[0],e4[1],3,Terrain_final)[1],Terrain_final)
              else :
                    deplacement(e4[0],e4[1],per_4, 3, Terrain_final,dict_esp4,4)
            elif dict_esp4[e4][0]>=2 :         #Si l'animal est suffisamment agé pour se reproduire
                dict_esp4[e4][1]-=20
                if perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[0]!=0 and math.sqrt((perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[0]-e4[0])**2+(perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[1]-e4[1])**2)<=math.sqrt(2) :
                    reproduction(4,dict_esp4,e4[0],e4[1],perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[0],perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[1],Terrain_final)
                else :
                    deplacement(e4[0],e4[1],per_4, 4, Terrain_final,dict_esp4,4)
            else : #Si il a rien fait, il fait un déplacement aléatoire
           #     deplacement_random(e4[0],e4[1],dict_esp4,4,Terrain_final)
               dict_esp4[e4][0]+=1
               dict_esp4[e4][1]-=20
            
            
            
        for e3 in list(dict_esp3) :
            if dict_esp3[e3][0]>=age_max_esp3 :           #Si l'animal est trop vieux
                del dict_esp3[e3]
                Terrain_final[e3].remove(3)
            dict_esp3[e3][0]+=1
            if dict_esp3[e3][1] == 0 :         #Si l'animal meurt de faim
                del dict_esp3[e3]
                Terrain_final[e3].remove(3)
            elif dict_esp3[e3][1]<=20 :        #Si l'animal a faim
                dict_esp3[e3][1]+=-20
                if perimetre_vision(1,e3[0],e3[1],2,Terrain_final)[0]!=0 and math.sqrt((perimetre_vision(1,e3[0],e3[1],2,Terrain_final)[0]-e3[0])**2+(perimetre_vision(1,e3[0],e3[1],2,Terrain_final)[1]-e3[1])**2)<=math.sqrt(2) :
                    predation(dict_esp3, dict_esp2, 2, e3[0],e3[1],perimetre_vision(1,e3[0],e3[1],2,Terrain_final)[0] )
                else :
                    deplacement(e3[0],e3[1],per_3, 2, Terrain_final,dict_esp3,3)
            elif dict_esp3[e3][0]>=2 :         #Si l'animal est suffisamment agé pour se reproduire
                dict_esp3[e3][1]+=-20
                if perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[0]!=0 and math.sqrt((perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[0]-e3[0])**2+(perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[1]-e3[1])**2)<=math.sqrt(2) :
                    reproduction(3,dict_esp3,e3[0],e3[1],perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[0],perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[1],Terrain_final)
                else :
                    deplacement(e3[0],e3[1],per_3, 2, Terrain_final,dict_esp3,3)
            else : #S'il n'a rien fait, il fait un déplacement aléatoire
          #      deplacement_random(e3,dict_esp3,3,Terrain_final)
                 dict_esp3[e3][0]+=1
                 dict_esp3[e3][1]+=-20

            
            
        for e2 in list(dict_esp2) :
            if dict_esp2[e2][0]>=age_max_esp2 :           #Si l'animal est trop vieux
                del dict_esp2[e2]
                Terrain_final[e2].remove(2)
            dict_esp2[e2][0]+=1
            if dict_esp2[e2][1] == 0 :         #Si l'animal est affamé
                del dict_esp2[e2]
                Terrain_final[e2].remove(2)
            elif dict_esp2[e2][1]<=20 :
                dict_esp2[e2][1]+=-20
                if perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[0]!=0 and math.sqrt((perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[0]-e2[0])**2+(perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[1]-e2[1])**2)<=math.sqrt(2) :
                    predation_plant(dict_esp2,e2[0],e2[1],perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[0],perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[1])
                else :
                    deplacement(e2[0],e2[1],per_2, 0, Terrain_final,dict_esp2,2)
            elif dict_esp2[e2][0]>=2 :
                dict_esp2[e2][1]+=-20
                if perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[0]!=0 and math.sqrt((perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[0]-e2[0])**2+(perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[1]-e2[1])**2)<=math.sqrt(2) :
                    reproduction(2,dict_esp2,e2[0],e2[1],perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[0],perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[1],Terrain_final)
                else :
                    deplacement(e2[0],e2[1],per_2, 1, Terrain_final,dict_esp2,2)
            else :
               # deplacement_random(e2,dict_esp2,2,Terrain_final)
               dict_esp2[e2][0]+=1
               dict_esp2[e2][1]+=-20
            
        
    return Terrain_final
#Bug dans la fonction perimetre vision a regarder
