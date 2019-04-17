
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt  
import random
import math
import matplotlib.animation as animation
import pygame
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:15:54 2019
@author: 3800147
"""

Dimension = 32
Ligne = Dimension
Colonne = Dimension
environnement=1/4
List_number_species=[42,42,52]
age_max_esp2=3
age_max_esp3=4
age_max_esp4=5
per_2 =15       #périmètre
per_3=20
per_4=25
faim_e4 = 25        # à partir de combien ils ont faim
faim_e3 =30
faim_e2 =30
amr_e4=1.2    #age de maturité sexuelle
amr_e3=1/2
amr_e2=1/3
faim_perdue_e4=10
faim_perdue_e3=10
faim_perdue_e2=10
gestation_e4=1/9
gestation_e3=1/9
gestation_e2=1/9
len_e4=[]
len_e3=[]
len_e2=[]
len_plant=[]
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
    a=environnement
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
def creatdict_esp2(Terrain):    #dictionnaire de l'espece 2 uniquement m
    desp2=dict()
    for i in range(len(Terrain)) :
        for j in range(len(Terrain[i])) :
            if Terrain[i][j]==2 :
                desp2[i,j]=[0,100,0]
    return desp2

def creatdict_esp2f(Terrain):    #dictionnaire de l'espece 2 uniquement f
    desp2f=dict()
    for i in range(len(Terrain)) :
        for j in range(len(Terrain[i])) :
            if Terrain[i][j]==-2 :
                desp2f[i,j]=[0,100,0]
    return desp2f

def creatdict_esp3(Terrain):    #dictionnaire de l'espece 3 uniquement m
    desp3=dict()
    for i in range(len(Terrain)) :
        for j in range(len(Terrain[i])) :
            if Terrain[i][j]==3 :
                desp3[i,j]=[0,100,0]       #1er elmt : âge 2eme elmt : jauge de faim
    return desp3

def creatdict_esp3f(Terrain):    #dictionnaire de l'espece 3 uniquement f 
    desp3f=dict()
    for i in range(len(Terrain)) :
        for j in range(len(Terrain[i])) :
            if Terrain[i][j]==-3 :
                desp3f[i,j]=[0,100,0]       #1er elmt : âge 2eme elmt : jauge de faim
    return desp3f

def creatdict_esp4(terrain):    #dictionnaire de l'espece 3 uniquement
    desp4=dict()
    for i in range(len(terrain)) :
        for j in range(len(terrain[i])) :
            if terrain[i][j]==4 :
                desp4[i,j]=[0,100,0]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp4

def creatdict_esp4f(terrain):    #dictionnaire de l'espece 3 uniquement
    desp4f=dict()
    for i in range(len(terrain)) :
        for j in range(len(terrain[i])) :
            if terrain[i][j]==-4 :
                desp4f[i,j]=[0,100,0]        #1er elmt : âge 2eme elmt : jauge de faim
    return desp4f

def creatdict_plant(terrain):    #dictionnaire des plantes uniquement, Terrain : terrain_final
    dplant=dict()
    for i in range(len(terrain)) :
        for j in range(len(terrain[0])) :
            if terrain[i][j]==0:
                dplant[i,j]=[100,False,0]
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
               if abs(e)>abs(i):          #modif du truc pour test plante
                   i=e  
           if i==0:
                temp.append((51,153,0))  #vert
           elif i==1:
                temp.append((255, 255, 0))  #jaune
           elif i==2:
                temp.append((204, 164, 131))  #marron1
           elif i==-2 :
                temp.append((117, 94, 75))   #marron2
           elif i==3:
                temp.append((225, 52, 170)) #violet1
           elif i==-3 :
                temp.append((138, 32, 104)) #violet2
           elif i==-4 :
                temp.append((0, 127, 255)) #bleu1
           elif i==4:
                temp.append((0, 0, 255))    #bleu2
       img.append(temp)      
    return img

Terrain_plante=terrain_final(environnement,Ligne,Colonne)
Terrain_especes= create_occupied_land_ecosystem([List_number_species[0]//2,List_number_species[0]//2,List_number_species[1]//2,List_number_species[1]//2,List_number_species[2]//2,List_number_species[2]//2], [2,-2,3,-3,4,-4], Ligne)
dict_plante=creatdict_plant(Terrain_plante)
dict_esp2m=creatdict_esp2(Terrain_especes)
dict_esp3m=creatdict_esp3(Terrain_especes)
dict_esp4m=creatdict_esp4(Terrain_especes)
dict_esp2f=creatdict_esp2f(Terrain_especes)
dict_esp3f=creatdict_esp3f(Terrain_especes)
dict_esp4f=creatdict_esp4f(Terrain_especes)
global Terrain_final
Terrain_final=Merge_matrix(Terrain_plante, Terrain_especes)

def deplacement(i,j,per, cible, Terrain,dict_esp,esp):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]>i :
        if k[1]>j :
            if j!=len(Terrain_final[0])-1 and i!=len(Terrain_final)-1 and len(Terrain_final[i+1][j+1])==1 :
                dict_esp[i+1,j+1]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i+1,j+1].append(esp)
            elif i!=len(Terrain_final)-1 and len(Terrain_final[i+1][j])==1 :
                dict_esp[i+1,j]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i+1,j].append(esp)
            elif len(Terrain_final[i][j+1])==1 :
                dict_esp[i,j+1]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i,j+1].append(esp)
        elif k[1]<j and j!=0 :
            if i!=len(Terrain_final)-1 and len(Terrain_final[i+1][j-1])==1 :
                dict_esp[i+1,j-1]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i+1,j-1].append(esp)
            elif len(Terrain_final[i+1][j])==1 and i!=len(Terrain_final)-1 :
                dict_esp[i+1,j]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i+1,j].append(esp)
            elif j<0 :
                if len(Terrain_final[i][j-1])==1 :
                    dict_esp[i,j-1]=dict_esp.pop((i,j))
                    Terrain[i,j].remove(esp)
                    Terrain[i,j-1].append(esp)
        elif len(Terrain_final[i+1][j])==1 and i!=len(Terrain_final)-1 :
            dict_esp[i+1,j]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+1,j].append(esp)
            
    elif k[0]<i :
        if k[1]>j :
            if j!=len(Terrain_final[0])-1 and len(Terrain_final[i-1][j+1])==1 :
                dict_esp[i-1,j+1]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i-1,j+1].append(esp)
            elif j!=len(Terrain_final[0])-1 and len(Terrain_final[i][j+1])==1 :
                dict_esp[i,j+1]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i,j+1].append(esp)
            elif len(Terrain_final[i-1][j])==1 :
                dict_esp[i-1,j]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i-1,j].append(esp)
        elif k[1]<j and len(Terrain_final[i-1][j-1])==1 :
            dict_esp[i-1,j-1]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j-1].append(esp)
        elif len(Terrain_final[i-1][j])==1 :
            dict_esp[i-1,j]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i-1,j].append(esp)
    elif k[0]==i :
        if k[1]!=j :
            if k[1]<j and len(Terrain_final[i,j-1])==1 :
                dict_esp[i,j-1]=dict_esp.pop((i,j))
                Terrain[i,j].remove(esp)
                Terrain[i,j-1].append(esp)
            elif j!=len(Terrain_final[0])-1 and len(Terrain_final[i][j+1])==1 : 
                    dict_esp[i,j+1]=dict_esp.pop((i,j))
                    Terrain[i,j].remove(esp)
                    Terrain[i,j+1].append(esp)
            

def perimetre_vision(per,i,j, cible,Terrain) : #s'applique sur un animal de position (i,j) qui cherche une proie de valeur cible
    temp=[]
    npsh =0
    npsd =0
    npsg =0
    npsb =0
    if i-per<0 :
        npsg=per-i      #npsg : ne pas sortir à gauche
    if i+per>=len(Terrain[0]) :
        npsd = i+per-len(Terrain[0])+1     #npsd : ne pas sortir à droite
    if j-per<0 :
        npsh=per-j                 #npsh : ne pas sortir en haut
    if j+per>=len(Terrain) :
        npsb = j+per-len(Terrain)+1      #npsb : ne pas sortir en bas
    for ligne in range(i-per+npsg,i+per-npsd+1):
        for colonne in range(j-per+npsh, j+per-npsb+1):
            if cible in Terrain[ligne][colonne] :

                if ligne!=i or colonne!=j :
                    if len(temp)==0 :
                        temp=[ligne, colonne]
                    if math.sqrt((i-ligne)**2+(j-colonne)**2)<math.sqrt((i-temp[0])**2+(j-temp[1])**2) :
                        temp=[ligne, colonne]
    if len(temp)==0 :
        temp=[-1,-1]
    return temp

def predation(d_pred,d_cible,cible,i,j,pos_cible_i,pos_cible_j,terrain):
    d_pred[i,j][1]+=20
    #print(pos_cible_i, pos_cible_j,list(d_cible))
    terrain[pos_cible_i,pos_cible_j].remove(cible)
    del d_cible[(pos_cible_i,pos_cible_j)]
    
    return
def predation_plant(d_pred,i,j,pos_cible_i,pos_cible_j):
    if dict_plante[pos_cible_i,pos_cible_j][0]-20 >0 :        
        d_pred[i,j][1]+=20
        dict_plante[pos_cible_i,pos_cible_j][0]-=20
    else :
        d_pred[i,j][1]+=dict_plante[pos_cible_i,pos_cible_j][0]
        dict_plante[pos_cible_i,pos_cible_j][0]=0
        dict_plante[pos_cible_i,pos_cible_j][1]=True
    return
def reproduction(espece,d_predm,d_predf,i,j,pos_cible_i,pos_cible_j,terrain) :
    if espece in terrain[i][j] :
        d_predf[pos_cible_i,pos_cible_j][2]=1
    else :
        d_predf[i,j][2]=1
    if i==pos_cible_i :
        if j>pos_cible_j :
            if i!=len(terrain)-1 :
                if len(terrain[i+1,j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i+1,j]=[0,100,0]
                        terrain[i+1,j].append(espece)
                    else :
                        d_predf[i+1,j]=[0,100,0]
                        terrain[i+1,j].append(-espece)
                elif len(terrain[i+1,pos_cible_j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i+1,pos_cible_j]=[0,100,0]
                        terrain[i+1,pos_cible_j].append(espece)
                    else :
                        d_predf[i+1,pos_cible_j]=[0,100,0]
                        terrain[i+1,pos_cible_j].append(-espece)
            elif i!=0 :
                if len(terrain[i-1,j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i-1,j]=[0,100,0]
                        terrain[i-1,j].append(espece)
                    else :
                        d_predf[i-1,j]=[0,100,0]
                        terrain[i-1,j].append(-espece)
                elif len(terrain[i-1,pos_cible_j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i-1,pos_cible_j]=[0,100,0]
                        terrain[i-1,pos_cible_j].append(espece)
                    else :
                        d_predf[i-1,pos_cible_j]=[0,100,0]
                        terrain[i-1,pos_cible_j].append(-espece)
            elif j!=len(terrain[0])-1 :
                if len(terrain[i,j+1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,j+1]=[0,100,0]
                        terrain[i,j+1].append(espece)
                    else :
                        d_predf[i,j+1]=[0,100,0]
                        terrain[i,j+1].append(-espece)
            elif pos_cible_j!=0 :
                if len(terrain[i,pos_cible_j-1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,pos_cible_j-1]=[0,100,0]
                        terrain[i,pos_cible_j-1].append(espece)
                    else :
                        d_predf[i,pos_cible_j-1]=[0,100,0]
                        terrain[i,pos_cible_j-1].append(-espece)
        elif j<pos_cible_j :
            if i!=len(terrain)-1 :
                if len(terrain[i+1,j])==1 :
                     if random.randint(0,1)==0 :
                        d_predm[i+1,j]=[0,100,0]
                        terrain[i+1,j].append(espece)
                     else :
                        d_predf[i+1,j]=[0,100,0]
                        terrain[i+1,j].append(-espece)
                elif len(terrain[i+1,pos_cible_j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i+1,pos_cible_j]=[0,100,0]
                        terrain[i+1,pos_cible_j].append(espece)
                    else :
                        d_predf[i+1,pos_cible_j]=[0,100,0]
                        terrain[i+1,pos_cible_j].append(-espece)
            elif i!=0 :
                if len(terrain[i-1,j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i-1,j]=[0,100,0]
                        terrain[i-1,j].append(espece)
                    else :
                        d_predf[i-1,j]=[0,100,0]
                        terrain[i-1,j].append(-espece)
                elif len(terrain[i-1,pos_cible_j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i-1,pos_cible_j]=[0,100,0]
                        terrain[i-1,pos_cible_j].append(espece)
                    else :
                        d_predf[i-1,pos_cible_j]=[0,100,0]
                        terrain[i-1,pos_cible_j].append(-espece)
            elif j!=0 :
                if len(terrain[i,j-1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,j-1]=[0,100,0]
                        terrain[i,j-1].append(espece)
                    else :
                        d_predf[i,j-1]=[0,100,0]
                        terrain[i,j-1].append(-espece)
            elif pos_cible_j!=len(terrain[0])-1 :
                if len(terrain[i,pos_cible_j+1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,pos_cible_j+1]=[0,100,0]
                        terrain[i,pos_cible_j+1].append(espece)
                    else :
                        d_predf[i,pos_cible_j+1]=[0,100,0]
                        terrain[i,pos_cible_j+1].append(-espece)
                    
    elif j==pos_cible_j : 
        if i>pos_cible_i :
            if j!=len(terrain[0])-1 :
                if len(terrain[i,j+1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,j+1]=[0,100,0]
                        terrain[i,j+1].append(espece)
                    else :
                        d_predf[i,j+1]=[0,100,0]
                        terrain[i,j+1].append(-espece)
                elif len(terrain[pos_cible_i,j+1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[pos_cible_i,j+1]=[0,100,0]
                        terrain[pos_cible_i,j+1].append(espece)
                    else :
                        d_predf[pos_cible_i,j+1]=[0,100,0]
                        terrain[pos_cible_i,j+1].append(-espece)
            elif j!=0 :
                if len(terrain[i,j-1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,j-1]=[0,100,0]
                        terrain[i,j-1].append(espece)
                    else :
                        d_predf[i,j-1]=[0,100,0]
                        terrain[i,j-1].append(-espece)
                elif len(terrain[pos_cible_i,j-1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[pos_cible_i,j-1]=[0,100,0]
                        terrain[pos_cible_i,j-1].append(espece)
                    else :
                        d_predf[pos_cible_i,j-1]=[0,100,0]
                        terrain[pos_cible_i,j-1].append(-espece)
            if i!=len(terrain)-1:
                if len(terrain[i+1,j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i+1,j]=[0,100,0]
                        terrain[i+1,j].append(espece)
                    else :
                        d_predf[i+1,j]=[0,100,0]
                        terrain[i+1,j].append(-espece)
            elif pos_cible_i!=0 :
                if len(terrain[pos_cible_i,j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[pos_cible_i,j]=[0,100,0]
                        terrain[pos_cible_i,j].append(espece)
                    else :
                        d_predf[pos_cible_i,j]=[0,100,0]
                        terrain[pos_cible_i,j].append(-espece)
        if i<pos_cible_i :
            if j!=len(terrain[0])-1 :
                if len(terrain[i,j+1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,j+1]=[0,100,0]
                        terrain[i,j+1].append(espece)
                    else :
                        d_predf[i,j+1]=[0,100,0]
                        terrain[i,j+1].append(-espece)
                elif len(terrain[pos_cible_i,j+1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[pos_cible_i,j+1]=[0,100,0]
                        terrain[pos_cible_i,j+1].append(espece)
                    else :
                        d_predf[pos_cible_i,j+1]=[0,100,0]
                        terrain[pos_cible_i,j+1].append(-espece)
            elif j!=0 :
                if len(terrain[i,j-1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i,j-1]=[0,100,0]
                        terrain[i,j-1].append(espece)
                    else :
                        d_predf[i,j-1]=[0,100,0]
                        terrain[i,j-1].append(-espece)
                elif len(terrain[pos_cible_i,j-1])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[pos_cible_i,j-1]=[0,100,0]
                        terrain[pos_cible_i,j-1].append(espece)
                    else :
                        d_predf[pos_cible_i,j-1]=[0,100,0]
                        terrain[pos_cible_i,j-1].append(-espece)
            if i!=0:
                if len(terrain[i-1,j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[i-1,j]=[0,100,0]
                        terrain[i-1,j].append(espece)
                    else :
                        d_predf[i-1,j]=[0,100,0]
                        terrain[i-1,j].append(-espece)
            elif pos_cible_i!=len(terrain)-1 :
                if len(terrain[pos_cible_i+1,j])==1 :
                    if random.randint(0,1)==0 :
                        d_predm[pos_cible_i+1,j]=[0,100,0]
                        terrain[pos_cible_i+1,j].append(espece)
                    else :
                        d_predf[pos_cible_i+1,j]=[0,100,0]
                        terrain[pos_cible_i+1,j].append(-espece)
    
    else :
        if len(terrain[i,pos_cible_j])==1 :
            if random.randint(0,1)==0 :
                d_predm[i,pos_cible_j]=[0,100,0]
                terrain[i,pos_cible_j].append(espece)
            else :
                d_predf[i,pos_cible_j]=[0,100,0]
                terrain[i,pos_cible_j].append(-espece)
        elif len(terrain[pos_cible_i,j])==1 :
            if random.randint(0,1)==0 :
                d_predm[pos_cible_i,j]=[0,100,0]
                terrain[pos_cible_i,j].append(espece)
            else :
                d_predf[pos_cible_i,j]=[0,100,0]
                terrain[pos_cible_i,j].append(-espece)

def deplacement_random (i,j, dict_esp,esp,Terrain) :
   if i==len(Terrain)-1 :
        a=random.randint(-1,0)
        if j==len(Terrain[0])-1:
            b=random.randint(-1,0)
        elif j==0 :
            b=random.randint(0,1)
        else :
            b=random.randint(-1,1)
        if len(Terrain[i+a,j+b])==1 :
            dict_esp[i+a,j+b]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+a,b+j].append(esp)
   elif i==0 :
        a=random.randint(0,1)
        if j==len(Terrain[0])-1:
            b=random.randint(-1,0)
        elif j==0 :
            b=random.randint(0,1)
        else :
            b=random.randint(-1,1)
        if len(Terrain[i+a,j+b])==1 :
            dict_esp[i+a,j+b]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+a,b+j].append(esp)
   elif j==0 :
        b=random.randint(0,1)
        a=random.randint(-1,1)
        if len(Terrain[i+a,j+b])==1 :
            dict_esp[i+a,j+b]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+a,b+j].append(esp)
   elif j==len(Terrain[0])-1 :
        b=random.randint(-1,0)
        a=random.randint(-1,1)
        if len(Terrain[i+a,j+b])==1 :
            dict_esp[i+a,j+b]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+a,b+j].append(esp)
   else :
        a=random.randint(-1,1)
        b=random.randint(-1,1)
        if len(Terrain[i+a,j+b])==1 :
            dict_esp[i+a,j+b]=dict_esp.pop((i,j))
            Terrain[i,j].remove(esp)
            Terrain[i+a,b+j].append(esp)
        
def proche(i,j,esp1,esp2,desp1,desp2,per,terrain) :
    e1=perimetre_vision(per,i,j,esp1,terrain)
    e2=perimetre_vision(per,i,j,esp2,terrain)
    if e1[0]!=-1 and e2[0]!=-1 :
      if math.sqrt((e1[0]-i)**2+(e1[1]-j)**2)<math.sqrt((e2[0]-i)**2+(e2[1]-j)**2) :
          return (esp1, e1, desp1)
      else :
          return (esp2, e2, desp2)
    elif e1[0]!=-1 and e2[0]==-1 :
        return (esp1, e1, desp1)
    elif e2[0]!=-1 and e1[0]==-1 :
        return (esp2, e2, desp2)
    else : 
        return ('Rien')
        
def cgmt(*args) :
    for e4 in list(dict_esp4m) :
            if dict_esp4m[e4][0]>=age_max_esp4 :           #Si l'animal est trop vieux
                del dict_esp4m[e4]
                Terrain_final[e4].remove(4)
                continue
            elif dict_esp4m[e4][1] == 0 :         #Si l'animal meurt de faim
                del dict_esp4m[e4]
                Terrain_final[e4].remove(4)
                continue
            if dict_esp4m[e4][1]<=faim_e4 :        #Si l'animal a faim
              dict_esp4m[e4][1]-=faim_perdue_e4  
              dict_esp4m[e4][0]+=1/12
              if dict_esp4m[e4][2]!=0 :
                   dict_esp4m[e4][2]-=gestation_e4
              if len(dict_esp3m)!=0 or len(dict_esp3f)!=0 :                #Il mange l'espèce 3 en priorité sauf que s'il n'y en a plus alors il mange de l'espece 2
                  if len(proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f,1,Terrain_final))==3 :
                     esp,pos,dictcible=proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f, 1,Terrain_final)
                     predation(dict_esp4m, dictcible, esp, e4[0],e4[1],pos[0],pos[1],Terrain_final)
                  elif len(proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f,per_4,Terrain_final))==3 :
                      esp,_,_ =proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f,per_4,Terrain_final)
                      deplacement(e4[0],e4[1],per_4, esp, Terrain_final,dict_esp4m,4)
              else :
                  if len(proche(e4[0],e4[1],2,-2,dict_esp3m, dict_esp3f,1,Terrain_final))==3 :
                     esp,pos,dictcible=proche(e4[0],e4[1],2,-2,dict_esp2m,dict_esp2f,1,Terrain_final)
                     predation(dict_esp4m, dictcible, esp, e4[0],e4[1],pos[0],pos[1],Terrain_final)
                  elif len(proche(e4[0],e4[1],2,-2,dict_esp3m, dict_esp3f,per_4,Terrain_final))==3 :
                      esp,_,_ =proche(e4[0],e4[1],2,-2,dict_esp2m, dict_esp2f,per_4,Terrain_final)
                      deplacement(e4[0],e4[1],per_4, esp, Terrain_final,dict_esp4m,4)
            elif dict_esp4m[e4][0]>=amr_e4 and dict_esp4m[e4][2]==0:         #Si l'animal est suffisamment agé pour se reproduire et qu'il n'est pas en période de gestation
                dict_esp4m[e4][1]-=faim_perdue_e4
                dict_esp4m[e4][0]+=1/12
                if perimetre_vision(1,e4[0],e4[1],-4,Terrain_final)[0]!=-1 : #Si l'espece de sexe opposé est a coté, ils se reproduisent
                    reproduction(4,dict_esp4m,dict_esp4f,e4[0],e4[1],perimetre_vision(1,e4[0],e4[1],-4,Terrain_final)[0],perimetre_vision(1,e4[0],e4[1],-4,Terrain_final)[1],Terrain_final)
                elif perimetre_vision(per_4,e4[0],e4[1],-4,Terrain_final)[0]!=-1 :
                    deplacement(e4[0],e4[1],per_4, -4, Terrain_final,dict_esp4m,4)
            else : #Si il a rien fait, il fait un déplacement aléatoire, perd de la faim et vieillit
               dict_esp4m[e4][1]-=faim_perdue_e4
               dict_esp4m[e4][0]+=1/12
               if dict_esp4m[e4][2]!=0 :
                   dict_esp4m[e4][2]-=gestation_e4
               deplacement_random(e4[0],e4[1],dict_esp4m,4,Terrain_final)
               
    for e4 in list(dict_esp4f) :
            if dict_esp4f[e4][0]>=age_max_esp4 :           #Si l'animal est trop vieux
                del dict_esp4f[e4]
                Terrain_final[e4].remove(-4)
                continue
            elif dict_esp4f[e4][1] == 0 :         #Si l'animal meurt de faim
                del dict_esp4f[e4]
                Terrain_final[e4].remove(-4)
                continue
            if dict_esp4f[e4][1]<=faim_e4 :        #Si l'animal a faim
              dict_esp4f[e4][1]-=faim_perdue_e4  
              dict_esp4f[e4][0]+=1/12
              if dict_esp4f[e4][2]!=0 :
                   dict_esp4f[e4][2]-=gestation_e4
              if len(dict_esp3m)!=0 or len(dict_esp3f)!=0 :                #Il mange l'espèce 3 en priorité sauf que s'il n'y en a plus alors il mange de l'espece 2
                  if len(proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f,1,Terrain_final))==3 :
                     esp,pos,dictcible=proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f,1,Terrain_final)
                     predation(dict_esp4f, dictcible, esp, e4[0],e4[1],pos[0],pos[1],Terrain_final)
                  elif len(proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f,per_4,Terrain_final))==3 :
                      esp,_,_ =proche(e4[0],e4[1],3,-3,dict_esp3m, dict_esp3f,per_4,Terrain_final)
                      deplacement(e4[0],e4[1],per_4, esp, Terrain_final,dict_esp4f,-4)
              else :
                  if len(proche(e4[0],e4[1],2,-2,dict_esp3m, dict_esp3f,1,Terrain_final))==3 :
                     esp,pos,dictcible=proche(e4[0],e4[1],2,-2,dict_esp2m,dict_esp2f,1,Terrain_final)
                     predation(dict_esp4f, dictcible, esp, e4[0],e4[1],pos[0],pos[1],Terrain_final)
                  elif len(proche(e4[0],e4[1],2,-2,dict_esp3m, dict_esp3f,per_4,Terrain_final))==3 :
                      esp,_,_ =proche(e4[0],e4[1],2,-2,dict_esp2m, dict_esp2f,per_4,Terrain_final)
                      deplacement(e4[0],e4[1],per_4, esp, Terrain_final,dict_esp4f,-4)
            elif dict_esp4f[e4][0]>=amr_e4 and dict_esp4f[e4][2]==0:         #Si l'animal est suffisamment agé pour se reproduire et qu'il n'est pas en période de gestation
                dict_esp4f[e4][1]-=faim_perdue_e4
                dict_esp4f[e4][0]+=1/12
                if perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[0]!=-1 : #Si l'espece de sexe opposé est a coté, ils se reproduisent
                    reproduction(4,dict_esp4m,dict_esp4f,e4[0],e4[1],perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[0],perimetre_vision(1,e4[0],e4[1],4,Terrain_final)[1],Terrain_final)
                elif perimetre_vision(per_4,e4[0],e4[1],4,Terrain_final)[0]!=-1 :
                    deplacement(e4[0],e4[1],per_4, 4, Terrain_final,dict_esp4f,-4)
            else : #Si il a rien fait, il fait un déplacement aléatoire, perd de la faim et vieillit
               dict_esp4f[e4][1]-=faim_perdue_e4
               dict_esp4f[e4][0]+=1/12
               if dict_esp4f[e4][2]!=0 :
                   dict_esp4f[e4][2]-=gestation_e4
               deplacement_random(e4[0],e4[1],dict_esp4f,-4,Terrain_final)
               
                
    for e3 in list(dict_esp3f) :
            if dict_esp3f[e3][0]>=age_max_esp3 :           #Si l'animal est trop vieux
                del dict_esp3f[e3]
                Terrain_final[e3].remove(-3)
                continue
            elif dict_esp3f[e3][1] == 0 :         #Si l'animal meurt de faim
                del dict_esp3f[e3]
                Terrain_final[e3].remove(-3)
                continue
            if dict_esp3f[e3][1]<=faim_e3 :        #Si l'animal a faim
              dict_esp3f[e3][1]-=faim_perdue_e3  
              dict_esp3f[e3][0]+=1/12
              if dict_esp3f[e3][2]!=0 :
                   dict_esp3f[e3][2]-=gestation_e3
              if len(proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f,1,Terrain_final))==3 :          #S'il est a coté de sa cible (male ou femelle)
                     esp,pos,dictcible=proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f,1,Terrain_final)
                     predation(dict_esp3f, dictcible, esp, e3[0],e3[1],pos[0],pos[1],Terrain_final)
              elif len(proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f,per_3,Terrain_final))==3 :
                      esp,_,_ =proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f,per_3,Terrain_final)
                      deplacement(e3[0],e3[1],per_3, esp, Terrain_final,dict_esp3f,-3)
    
            elif dict_esp3f[e3][0]>=amr_e3 and dict_esp3f[e3][2]==0:         #Si l'animal est suffisamment agé pour se reproduire et qu'il n'est pas en période de gestation
                dict_esp3f[e3][1]-=faim_perdue_e3
                dict_esp3f[e3][0]+=1/12
                if perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[0]!=-1 : #Si l'espece de sexe opposé est a coté, ils se reproduisent
                    reproduction(3,dict_esp3m,dict_esp3f,e3[0],e3[1],perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[0],perimetre_vision(1,e3[0],e3[1],3,Terrain_final)[1],Terrain_final)
                elif perimetre_vision(per_3,e3[0],e3[1],3,Terrain_final)[0]!=-1 :
                    deplacement(e3[0],e3[1],per_3, 3, Terrain_final,dict_esp3f,-3)
            else : #Si il a rien fait, il fait un déplacement aléatoire, perd de la faim et vieillit
               dict_esp3f[e3][1]-=faim_perdue_e3
               dict_esp3f[e3][0]+=1/12
               if dict_esp3f[e3][2]!=0 :
                   dict_esp3f[e3][2]-=gestation_e3
               deplacement_random(e3[0],e3[1],dict_esp3f,-3,Terrain_final)
            
    for e3 in list(dict_esp3m) :
            if dict_esp3m[e3][0]>=age_max_esp3 :           #Si l'animal est trop vieux
                del dict_esp3m[e3]
                Terrain_final[e3].remove(3)
                continue
            elif dict_esp3m[e3][1] == 0 :         #Si l'animal meurt de faim
                del dict_esp3m[e3]
                Terrain_final[e3].remove(3)
                continue
            if dict_esp3m[e3][1]<=faim_e3 :        #Si l'animal a faim
              dict_esp3m[e3][1]-=faim_perdue_e3  
              dict_esp3m[e3][0]+=1/12
              if dict_esp3m[e3][2]!=0 :
                   dict_esp3m[e3][2]-=gestation_e3
              if len(proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f,1,Terrain_final))==3 :          #S'il est a coté de sa cible (male ou femelle)
                     esp,pos,dictcible=proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f, 1,Terrain_final)
                     predation(dict_esp3m, dictcible, esp, e3[0],e3[1],pos[0],pos[1],Terrain_final)
              elif len(proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f,per_3,Terrain_final))==3 :
                      esp,_,_ =proche(e3[0],e3[1],2,-2,dict_esp2m, dict_esp2f,per_3,Terrain_final)
                      deplacement(e3[0],e3[1],per_3, esp, Terrain_final,dict_esp3m,3)
    
            elif dict_esp3m[e3][0]>=amr_e3 and dict_esp3m[e3][2]==0:         #Si l'animal est suffisamment agé pour se reproduire et qu'il n'est pas en période de gestation
                dict_esp3m[e3][1]-=faim_perdue_e3
                dict_esp3m[e3][0]+=1/12
                if perimetre_vision(1,e3[0],e3[1],-3,Terrain_final)[0]!=-1 : #Si l'espece de sexe opposé est a coté, ils se reproduisent
                    reproduction(3,dict_esp3m,dict_esp3f,e3[0],e3[1],perimetre_vision(1,e3[0],e3[1],-3,Terrain_final)[0],perimetre_vision(1,e3[0],e3[1],-3,Terrain_final)[1],Terrain_final)
                elif perimetre_vision(per_3,e3[0],e3[1],3,Terrain_final)[0]!=-1 :
                    deplacement(e3[0],e3[1],per_3, -3, Terrain_final,dict_esp3m,3)
            else : #Si il a rien fait, il fait un déplacement aléatoire, perd de la faim et vieillit
               dict_esp3m[e3][1]-=faim_perdue_e3
               dict_esp3m[e3][0]+=1/12
               if dict_esp3m[e3][2]!=0 :
                   dict_esp3m[e3][2]-=gestation_e3
               deplacement_random(e3[0],e3[1],dict_esp3m,3,Terrain_final)

            
            
    for e2 in list(dict_esp2m) :
            if dict_esp2m[e2][0]>=age_max_esp2 :           #Si l'animal est trop vieux
                del dict_esp2m[e2]
                Terrain_final[e2].remove(2)
                #print(e2,"meurt vieux")
                continue
            if dict_esp2m[e2][1] == 0 :         #Si l'animal est affamé
                del dict_esp2m[e2]
                Terrain_final[e2].remove(2)
                #print(e2,"meurt faim")
                continue
            elif dict_esp2m[e2][1]<=faim_e2 :
                dict_esp2m[e2][1]+=-5
                dict_esp2m[e2][0]+=1/12
                if dict_esp2m[e2][2]!=0 :
                    dict_esp2m[e2][2]-=1
                if perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[0]!=-1 :
                    predation_plant(dict_esp2m,e2[0],e2[1],perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[0],perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[1])
                elif perimetre_vision(per_2,e2[0],e2[1],0,Terrain_final)[0]!=-1 :
                    deplacement(e2[0],e2[1],per_2, 0, Terrain_final,dict_esp2m,2)
            elif dict_esp2m[e2][0]>=amr_e2 and dict_esp2m[e2][2]==0:
                dict_esp2m[e2][1]+=-5
                dict_esp2m[e2][0]+=1/12
                if perimetre_vision(1,e2[0],e2[1],-2,Terrain_final)[0]!=-1 :
                    reproduction(2,dict_esp2m,dict_esp2f,e2[0],e2[1],perimetre_vision(1,e2[0],e2[1],-2,Terrain_final)[0],perimetre_vision(1,e2[0],e2[1],-2,Terrain_final)[1],Terrain_final)
                elif perimetre_vision(per_2,e2[0],e2[1],-2,Terrain_final)[0]!=-1 :
                    deplacement(e2[0],e2[1],per_2, -2, Terrain_final,dict_esp2m,2)
            else :
               dict_esp2m[e2][0]+=1/12
               dict_esp2m[e2][1]-=faim_perdue_e2
               if dict_esp2m[e2][2]!=0 :
                   dict_esp2m[e2][2]-=gestation_e2
               deplacement_random(e2[0],e2[1],dict_esp2m,2,Terrain_final)
               
    for e2 in list(dict_esp2f) :
            if dict_esp2f[e2][0]>=age_max_esp2 :           #Si l'animal est trop vieux
                del dict_esp2f[e2]
                Terrain_final[e2].remove(-2)
                #print(e2,"meurt vieux")
                continue
            if dict_esp2f[e2][1] == 0 :         #Si l'animal est affamé
                del dict_esp2f[e2]
                Terrain_final[e2].remove(-2)
                #print(e2,"meurt faim")
                continue
            elif dict_esp2f[e2][1]<=faim_e2 :
                dict_esp2f[e2][1]+=-5
                dict_esp2f[e2][0]+=1/12
                if dict_esp2f[e2][2]!=0 :
                    dict_esp2f[e2][2]-=1
                if perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[0]!=-1 :
                    predation_plant(dict_esp2f,e2[0],e2[1],perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[0],perimetre_vision(1,e2[0],e2[1],0,Terrain_final)[1])
                elif perimetre_vision(per_2,e2[0],e2[1],0,Terrain_final)[0]!=-1 :
                    deplacement(e2[0],e2[1],per_2, 0, Terrain_final,dict_esp2f,-2)
            elif dict_esp2f[e2][0]>=amr_e2 and dict_esp2f[e2][2]==0:
                dict_esp2f[e2][1]+=-5
                dict_esp2f[e2][0]+=1/12
                if perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[0]!=-1 :
                    reproduction(2,dict_esp2m,dict_esp2f,e2[0],e2[1],perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[0],perimetre_vision(1,e2[0],e2[1],2,Terrain_final)[1],Terrain_final)
                elif perimetre_vision(per_2,e2[0],e2[1],2,Terrain_final)[0]!=-1 :
                    deplacement(e2[0],e2[1],per_2, 2, Terrain_final,dict_esp2f,-2)
            else :
               dict_esp2f[e2][0]+=1/12
               dict_esp2f[e2][1]-=faim_perdue_e2
               if dict_esp2f[e2][2]!=0 :
                   dict_esp2f[e2][2]-=gestation_e2
               deplacement_random(e2[0],e2[1],dict_esp2f,-2,Terrain_final)
               
    for ep in list(dict_plante) :
            if dict_plante[ep][1]: #lorsque la plante est mangée, 3 tours pour qu'elle repousse
                if 0 in Terrain_final[ep[0]][ep[1]] :   #elle vient de mourir
                    Terrain_final[ep].remove(0)
                    Terrain_final[ep].append(1)
                    dict_plante[ep][2]=3
                else :
                    dict_plante[ep][2]-=1
                    if dict_plante[ep][2]==0 :
                        dict_plante[ep][1]=False
            elif dict_plante[ep][0]==0 and not dict_plante[ep][1]:
                Terrain_final[ep].append(0)
                Terrain_final[ep].remove(1)
                dict_plante[ep][0]=50
            #else :
              #  dict_plante[ep][0]+=10
                    
    len_e4.append(len(dict_esp4m)+len(dict_esp4f))
    len_e3.append(len(dict_esp3m)+len(dict_esp3f))
    len_e2.append(len(dict_esp2m)+len(dict_esp2f))
    len_plant.append(len(dict_plante))
    
    return Terrain_final
#Bug dans la fonction perimetre vision a regarder

#affichagefinal(100)
window = Tk()
 
window.title("Dynamiques de populations")

a = Label(window, text="dimension")
b = Label(window, text="environnement")
c = Label(window, text="Liste des populations d'éspèces")
d = Label(window, text="age maximum 1")
e = Label(window, text="age maximum 2")
f = Label(window, text="age maximum 3")
g = Label(window, text="perimètre 2")
h = Label(window, text="perimètre 3")
i = Label(window, text="faim_e4")
k = Label(window, text="faim_e3")
l = Label(window, text="faim_e2")
m = Label(window, text="faim_e4")
n = Label(window, text="amr_e4")
o = Label(window, text="amr_e3")
p = Label(window, text="amr_e2")
q = Label(window, text="faim perdue_e4")
r = Label(window, text="faim perdue_e3")
s = Label(window, text="faim perdue_e2")
t = Label(window, text="gest 4")
u = Label(window, text="gest 3")
v = Label(window, text="gest 4")
w = Label(window, text="len_e4")
x = Label(window, text="len_e3")
y = Label(window, text="len_e2")
z = Label(window, text="len_plant_e4")

L = [a, b, c, d, e, f, g, h, i, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
for i in range(len(L)):
    L[i].grid(column=0, row = i)

A = Entry(window, width=10)
B = Entry(window, width=10)
C = Entry(window, width=10)
D = Entry(window, width=10)
E = Entry(window, width=10)
F = Entry(window, width=10)
G = Entry(window, width=10)
H = Entry(window, width=10)
I = Entry(window, width=10)
K = Entry(window, width=10)
L = Entry(window, width=10)
M = Entry(window, width=10)
N = Entry(window, width=10)
O = Entry(window, width=10)
P = Entry(window, width=10)
Q = Entry(window, width=10)
R = Entry(window, width=10)
S = Entry(window, width=10)
T = Entry(window, width=10)
U = Entry(window, width=10)
V = Entry(window, width=10)
W = Entry(window, width=10)
X = Entry(window, width=10)
Y = Entry(window, width=10)
Z = Entry(window, width=10)

c = [A, B, C, D, E, F, G, H, I, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, W, X, Y, Z]
for i in range(len(c)):
    c[i].grid(column=2, row = i)

    
A = A.get()
B = B.get()
C = C.get()
D = D.get()
E = E.get()
F = F.get()
G = G.get()
H = H.get()
I = I.get()
K = K.get()
L = L.get()
M = M.get()
N = N.get()
O = O.get()
P = P.get()
Q = Q.get()
R = R.get()
S = S.get()
T = T.get()
U = U.get()
V = V.get()
W = W.get()
X = X.get()
Y = Y.get()
Z = Z.get()
def update(*args) :
   cgmt()
   im.set_array(affichage(Terrain_final))
   return im

def clicked():
    Dimension = int(A)
    Ligne = Dimension
    Colonne = Dimension
    environnement=float(B)
    List_number_species=list(C)
    age_max_esp2=int(D)
    age_max_esp3=int(E)
    age_max_esp4=int(F)
    per_2 =int(G)      #périmètre
    per_3=int(H)
    per_4=int(I)
    faim_e4 = int(K)        # à partir de combien ils ont faim
    faim_e3 =int(L)
    faim_e2 =int(M)
    amr_e4=float(N)    #age de maturité sexuelle
    amr_e3=float(O)
    amr_e2=float(P)
    faim_perdue_e4=float(Q)
    faim_perdue_e3=float(R)
    faim_perdue_e2=float(S)
    gestation_e4=float(T)
    gestation_e3=float(U)
    gestation_e2=float(V)
    len_e4=list(W)
    len_e3=L=list(X)
    len_e2=list(Y)
    len_plant=list(Z)
    figure = plt.figure()
    Terrain_final
    delay=400
    im = plt.imshow(affichage(Terrain_final))
    ani = animation.FuncAnimation(figure, update, interval=delay, blit=False)
    plt.show()



btn = Button(window, text="Commencer animation", command=clicked)
btn.grid(column=1, row=28)



window.mainloop()



def lotka_volterra_one_gen(proie, pred, a1, b1, c1 ,d1) :
    proie_in = proie
    predateur_in = pred
    pr = proie
    pre = pred
    pr1 = pr
    pr = pr + (a1*pr - b1*pr*pre)
    pre = pre + (c1*b1*pr1*pre - d1*pre)
    if pr < 0 :
        pr = 0
    if pre < 0:
        pre = 0
      
    return pr, pre, proie_in, predateur_in

def lotka_volterra_n_gen(proie, pred, a, b, c, d, n):
    proie_in = proie
    predateur_in = pred
    L_pr = [proie]
    L_pre = [pred]
    pr = proie
    pre = pred
    for i in range(n):
        pr, pre = lotka_volterra_one_gen(pr, pre, a, b, c, d)
        L_pr.append(pr)
        L_pre.append(pre)
    return L_pr, L_pre, proie_in, predateur_in


def lotka_volterra_chain_one_gen(L_pop, L_abcd):
    """
    L_pop = [pop_0, pop_2, ..., pop_inf]
    L_abcd = [[a, b, c, d], [a1, b1, c1, d1], ..., [a_inf, b_inf, c_inf, d_inf]]; len(L_abcd) = len(L_pop)-1
    """
    L_new = []
    for i in range(len(L_pop)): 
        if i == 0:
            a = lotka_volterra_one_gen(L_pop[i+1], L_pop[i], L_abcd[i][0], L_abcd[i][1], L_abcd[i][2], L_abcd[i-1][3] )
            L_new.append(a[1])
        elif i == len(L_pop) -1:
            a = lotka_volterra_one_gen(L_pop[i], L_pop[i-1], L_abcd[i-1][0], L_abcd[i-1][1], L_abcd[i-1][2], L_abcd[i-1][3] )
            L_new.append(a[0])
        else:
            a = lotka_volterra_one_gen(L_pop[i+1], L_pop[i], L_abcd[i][0], L_abcd[i][1], L_abcd[i][2], L_abcd[i][3] )
            b = lotka_volterra_one_gen(L_pop[i], L_pop[i-1], L_abcd[i-1][0], L_abcd[i-1][1], L_abcd[i-1][2], L_abcd[i-1][3] )
            c= (a[1] + b[0])/2
            L_new.append(c)
    return L_new

def invert(L):
    L1 = []
    for i in range(len(L[0])):
        L2 = []
        for k in L :
            L2.append(k[i])
        L1.append(L2)
    return L1

            
            

def lotka_volterra_chain_n_gen(L_pop, L_abcd, n):
    L = L_pop
    L_all = [L]
    for i in range(n):
        L =lotka_volterra_chain_one_gen(L, L_abcd)
        L_all.append(L)
    return L_all

def test_life(L, i, j):
    return L[i][j] != 0


def create_empty_land(n):
    L= []
    for i in range(n):
        L1 = []
        for i in range(n):
            L1.append(0)
        L.append(L1)
    return L


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
    return L

        
def create_occupied_land(n, m, signature):
    Empty_matrix = m
    k = len(m)
    for i in range(int(n)):
        a = random.randint(0, k-1)
        b = random.randint(0, k-1)
        while Empty_matrix[a][b] != 0:
            a = random.randint(0, k-1)
            b = random.randint(0, k-1)
        Empty_matrix[a][b] = signature
    return Empty_matrix
def create_occupied_land_ecosystem(List_number_species, List_of_signatures, m):
    """len(List_of_species == len(List_of_signature)"""
            
    General_ecosystem_matrix = create_empty_land(m)
    for i in range(len(List_number_species)):
       General_ecosystem_matrix = create_occupied_land(List_number_species[i], General_ecosystem_matrix, List_of_signatures[i])
    
    return General_ecosystem_matrix
            
        
mt = create_empty_land(30)
a =create_occupied_land(100, mt, 1)
b =create_occupied_land(300, create_empty_land(70),2) 
a =create_occupied_land_ecosystem([1000,400, 700], [1, 3, 4], 70)

c = Merge_matrix(a, b)
#print(c) 
#Double_liste=Merge_matrix(a, b)

import math
Ligne=16, 1, 1, 1, 1,
Colonne=16
def perimetre_vision(per,i,j, cible,Terrain) : #s'applique sur un animal de position (i,j) qui cherche une proie de valeur cible
    temp=[0, 0]
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
            try:
                if cible in Terrain[ligne][colonne] :
                    if len(temp)==0 :
                        try :
                            temp=[ligne, colonne]
                        except IndexError:
                                temp = temp
                    if math.sqrt((i-ligne)**2+(j-colonne)**2)<math.sqrt((i-temp[0])**2+(j-temp[1])**2) :
                        try :
                            temp=[ligne, colonne]
                        except IndexError:
                            temp = temp
            except IndexError:
                temp = temp
                            
    return temp
b = create_occupied_land_ecosystem([30, 30, 12], [0, 1, 2], 10)
c = create_occupied_land_ecosystem([40], [3], 10)
a = Merge_matrix(b, c)
#print(perimetre_vision(1, 6, 7, 1,a))


def affichage(matrice):
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

    return img

Matrice_animaux = create_occupied_land_ecosystem([30, 50,60],[1, 2, 3], 13)

Matrice_plante = create_empty_land(13)

Matrice = Merge_matrix(Matrice_animaux, Matrice_plante)

list_number_in = [1, 1, 1]
list_number_fin = lotka_volterra_chain_one_gen(list_number_in, [[0.66, 0.75, 1, 1], [1, 0.5, 0.5, 1], [1, 0.5, 0.5, 1]])
List_of_signatures = [1, 2, 3]
plant_signature = 0

def  animate(nums_in, sigs, coefs):
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    done = False
    a = nums_in
    b = 0
    for i in a:
        b = b + i
    b = int( math.sqrt(b*4))
    while not done:
        pygame.time.delay(100)
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
        Matrice1 = create_occupied_land_ecosystem(a,sigs, b)
        Matrice2 = create_empty_land(b)
        Matrice = Merge_matrix(Matrice1, Matrice2)

        i = 1000//b

        for j in range(len(Matrice)):
            for k in range(len(Matrice[j])):
                    e = Matrice[j][k][0]
                    if e == 0:
                        pygame.draw.rect(screen, (51,153,0), pygame.Rect(i*k, i*j, i, i))
                    if e == 1:
                        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(i*k, i*j, i, i))
                    if e == 2:
                        pygame.draw.rect(screen, (204,153,51), pygame.Rect(i*k, i*j, i, i))
                    if e == 3:
                        pygame.draw.rect(screen, (128,0,128), pygame.Rect(i*k, i*j, i, i))
                    if e == 4:
                        pygame.draw.rect(screen, (192,192,192), pygame.Rect(i*k, i*j, i, i))
        a = lotka_volterra_chain_one_gen(a, coefs)
        c = 0
        for j in a:
            c = c + 1
        if b**2 > 0.9*c:
            b = 0
            for i in a:
                b = b + i            
            b = int(math.sqrt(b*4))

        
        pygame.display.flip()




window = Tk()
 
window.title("Dynamiques de populations")

lbl = Label(window, text="Ce programme permet de simuler l'évolution de la population d'une chaine alimentaire de deux manières différentes")
lbl2 = Label(window, text="Une simulation basée sur une analyse cas par cas des éspèces selon une logique pragmatique et intuitive")
lbl3 = Label(window, text="L'autre qui suit le système d'équations différentielles de Lotka-Volterra")
lbl4 = Label(window, text="----------------------------------------------------------------------------------------------------------------------------------------")

lbl.grid(column=0, row=0)
lbl2.grid(column=0, row = 1)
lbl3.grid(column=0, row = 2)
lbl4.grid(column=0, row = 3)

lbla = Label(window, text="Population a")
lbl2a = Label(window, text="Population b")
lbl3a= Label(window, text="Population c")
lbl4a = Label(window, text="Population d")

lbla.grid(column=0, row=4)
lbl2a.grid(column=0, row = 5)
lbl3a.grid(column=0, row = 6)
lbl4a.grid(column=0, row = 7)

txt = Entry(window,width=10)
txt1 = Entry(window,width=10)
txt2 = Entry(window,width=10)
txt3 = Entry(window,width=10)

txt.grid(column=1, row=4)
txt1.grid(column=1, row=5)
txt2.grid(column=1, row=6)
txt3.grid(column=1, row=7)

lblaa = Label(window, text="alpha 1")
lbl2aa = Label(window, text="beta 1")
lbl3aa= Label(window, text="delta 1")
lbl4aa = Label(window, text="gamma 1")

lblaa.grid(column=2, row=4)
lbl2aa.grid(column=2, row = 5)
lbl3aa.grid(column=2, row = 6)
lbl4aa.grid(column=2, row = 7)

txtaa = Entry(window,width=10)
txt1aa = Entry(window,width=10)
txt2aa = Entry(window,width=10)
txt3aa = Entry(window,width=10)

txtaa.grid(column=3, row=4)
txt1aa.grid(column=3, row=5)
txt2aa.grid(column=3, row=6)
txt3aa.grid(column=3, row=7)

lblb = Label(window, text="alpha 2")
lbl2b = Label(window, text="beta 2")
lbl3b= Label(window, text="delta 2")
lbl4b = Label(window, text="gamma 2")

lblb.grid(column=4, row=4)
lbl2b.grid(column=4, row = 5)
lbl3b.grid(column=4, row = 6)
lbl4b.grid(column=4, row = 7)

txtb = Entry(window,width=10)
txt1b = Entry(window,width=10)
txt2b = Entry(window,width=10)
txt3b = Entry(window,width=10)

txtb.grid(column=5, row=4)
txt1b.grid(column=5, row=5)
txt2b.grid(column=5, row=6)
txt3b.grid(column=5, row=7)

lblbb = Label(window, text="alpha 3")
lbl2bb = Label(window, text="beta 3")
lbl3bb= Label(window, text="delta 3")
lbl4bb = Label(window, text="gamma 3")

lblbb.grid(column=6, row=4)
lbl2bb.grid(column=6, row = 5)
lbl3bb.grid(column=6, row = 6)
lbl4bb.grid(column=6, row = 7)

txtbb = Entry(window,width=10)
txt1bb = Entry(window,width=10)
txt2bb = Entry(window,width=10)
txt3bb = Entry(window,width=10)

txtbb.grid(column=7, row=4)
txt1bb.grid(column=7, row=5)
txt2bb.grid(column=7, row=6)
txt3bb.grid(column=7, row=7)


def clicked():
    a = txt.get()
    b = txt1.get()
    c = txt2.get()
    d = txt3.get()
    a1 = txtaa.get()
    b1 = txt1aa.get()
    c1 = txt2aa.get()
    d1 = txt3aa.get()
    a2 = txtb.get()
    b2 = txt1b.get()
    c2 = txt2b.get()
    d2 = txt3b.get()
    a3 = txtbb.get()
    b3 = txt1bb.get()
    c3 = txt2bb.get()
    d3 = txt3bb.get()
    for i in [a, b, c, d, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3]:
        if i =="":
            return
    L = invert(lotka_volterra_chain_n_gen([float(a), float(b), float(c),float(d)], [[float(a1), float(b1), float(c1), float(d1)], [float(a2), float(b2), float(c2), float(d2)], [float(a3), float(b3), float(c3), float(d3)]],350))

    from pylab import plt

    for i in L:
        plt.plot(range(351),i)
    plt.show()

def clicked1():
    a = txt.get()
    b = txt1.get()
    c = txt2.get()
    d = txt3.get()
    a1 = txtaa.get()
    b1 = txt1aa.get()
    c1 = txt2aa.get()
    d1 = txt3aa.get()
    a2 = txtb.get()
    b2 = txt1b.get()
    c2 = txt2b.get()
    d2 = txt3b.get()
    a3 = txtbb.get()
    b3 = txt1bb.get()
    c3 = txt2bb.get()
    d3 = txt3bb.get()
    animate([float(a), float(b), float(c),float(d)], [1, 2, 3, 4], [[float(a1), float(b1), float(c1), float(d1)], [float(a2), float(b2), float(c2), float(d2)], [float(a3), float(b3), float(c3), float(d3)]])
btn = Button(window, text="Graph Lotka-Volterra", command=clicked)
btn.grid(column=2, row=0)

btn = Button(window, text="Animation Lotka-Volterra", command=clicked1)
btn.grid(column=3, row=0)

window.mainloop()

