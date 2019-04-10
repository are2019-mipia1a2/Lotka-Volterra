#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:30:48 2019

@author: 3800025
"""
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt  
import random
import math
import matplotlib.animation as animation

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

a = 10
b = 12          
c = 10
d = 1

#L = invert(lotka_volterra_chain_n_gen([a, b, c, d], [[0.2,0.0002, 0.1, 0.1], [0.1,0.0009, 0.7, 0.1], [0.25, 0.0006, 0.3, 0.1]],200)[0])
#print(L[0])
from pylab import plt

##for i in L:
   # plt.plot(range(201),i)
#plt.show()

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
"""
def update_occupied_land(Matrice, list_number_in, list_number_fin, List_of_signatures, dict, plant_signature, i):
    list_dif = []
    for n in Matrice:
        for j in n:
            if plant_signature in j:
                if List_of_signatures[len(List_of_signatures)-1] in j[2:]:
                    Matrice[n][j][1] = 0
            elif random.randint(1, list_number_in[n]) >= list_number_in[n] // random.randint(1,5):
                Matrice[n][j][1] = plant_signature
    a = int(list_number_fin[i] - list_number_in[i])
    print(a)
    list_dif.append(a)
    while i == i:
        
        
        if a < 0:
            while 1 == 1:
                    for j in range(len(Matrice)):
                        for k in range(len(Matrice[j])):
                            l = Matrice[j][k][0]
                            if a  != 0:
                                if l == List_of_signatures[i]:
                                    if random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5)  :
                                        if a != 0:
                                            v = a
                                            if i == 0:
                                                if dict[str(j)+"-"+str(k)][1] == 0:
                                                    Matrice[j][k][0] = 0 
                                                    a = a + 1
                                                elif dict[str(j)+"-"+str(k)][0] > 15:
                                                    Matrice[j][k][0] = 0
                                                    a = a + 1
                                                elif random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5): 
                                                    Matrice[j][k][0] = 0 
                                                    a = a + 1
                                                elif random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                    b=perimetre_vision(1, j, k, List_of_signatures[i+1], Matrice)
                                                    if len(b) == 2:
                                                        Matrice[b[0]][b[1]].append(List_of_signatures[i])
                                              # elif  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                               #    b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                                 #  c=perimetre_vision(1, j, k,0, Matrice)

                                                  # if len(b) == 2:
                                                   #    d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                                   #if len(b) == 2 and len(c) == 2 and len(d) == 2 :
                                                   #    if add > 0:
                                                    #      Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                     #      a = a - 1
                                                      #     add = a -1
                                            elif i == len(List_of_signatures) - 1:
                                                if List_of_signatures[i-1] in Matrice[j][k]:
                                                    Matrice[j][k][0] = List_of_signatures[i-1]
                                                    Matrice[j][k] = Matrice[j][k][0:2]
                                                    a = a + 1

                                                if dict[str(j)+"-"+str(k)][1] == 0:
                                                    Matrice[j][k][0] = 0 
                                                    a = a + 1
                                                elif dict[str(j)+"-"+str(k)][0] > 15:
                                                    Matrice[j][k][0] = 0
                                                    a = a + 1
                                               #elif  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                #   b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                                 #  c=perimetre_vision(1, j, k,0)
                                                  # if len(b) == 2:
                                                   #    d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                                   #if len(b) == 2 and len(c) == 2 and len(d) == 2 :
                                                      # if add > 0 :
                                                       #    Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                        #   a = a - 1
                                                         #  add = add -1
                                             #elif  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                              #     b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                               #    c=perimetre_vision(1, j, k,0, Matrice)           for e in k:
                                                #   if len(b) == 2:
                                                 #      d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                                  # if len(b) == 2 and len(c) == 2 and len(d) == 2 :
                                                   #    if add > 0:
                                                    #       Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                     #      a = a - 1
                                                      #     add = add - 1
                                            
                                            
                                            elif List_of_signatures[i-1] in Matrice[j][k]:
                                                Matrice[j][k][0] = List_of_signatures[i-1]

                                                Matrice[j][k] = Matrice[j][k][0:2]                                                
                                                a = a + 1
                                            elif random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                 b=perimetre_vision(1, j, k, List_of_signatures[i+1], Matrice)
                                                 if len(b) == 2:
                                                     Matrice[b[0]][b[1]].append(List_of_signatures[i])
                                            elif dict[str(j)+"-"+str(k)][1] == 0:
                                                Matrice[j][k][0] = 0 
                                                a = a + 1
                                            elif dict[str(j)+"-"+str(k)][0] > 15:
                                                Matrice[j][k][0] = 0
                                                a = a +1
                                            elif a == v:
                                                Matrice[j][k][0] = 0
                                                a = a + 1
                                         #elhttp://tkinter.unpythonic.net/wiki/if  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                          #         b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                           #        c=perimetre_vision(1, j, k,0, Matrice)Matrice, list_number_in, list_number_fin, List_of_signatures, dict, plant_
                                            #       if len(b) == 2:
                                             #          d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                              #     if len(b) == 2 and len(c) == 2 and len(d) == 2 :
                                               #        if add > 0:
                                                #           Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                 #         a = a - 1
                                                  #         add = add-1
                            else:

                                return Matrice

        if a > 0:                                                                                                                                                  
          # while 1 == 1:                                                                                                                                                   
                    for j in range(len(Matrice)):
                        for k in range(len(Matrice[j])):
                            l = Matrice[j][k][0]
                            if a  != 0:
                                v = aprint(a)

                                if l == List_of_signatures[i]:
                                    if 1==1  :
                                        if a != 0:
                                            if i == 0:
                                               #if dict[str(j)+"-"+str(k)][1] == 0:
                                                #   if subs < 0:
                                                 #      Matrice[j][k][0] = 0 
                                                  #     a = a + 1
                                                   #    subs = subs + 1
                                               #ifims.append(affichage(i)) dict[str(j)+"-"+str(k)][0] > 15:
                                                #   if subs < 0:
                                                 #      Matrice[j][k][0] = 0
                                                  #     a = a + 1
                                                 #    subs = subs +1
                                             #  elif random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                              #     if subs < 0:
                                               #     while 1 == 1   Matrice[j][k][0] = 0 
                                                #       a = a + 1
                                                # ims.append(affichage(i))      subs = subs + 1
                                                if random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                    b=perimetre_vision(1, j, k, List_of_signatures[i+1], Matrice)
                                                    if len(b) == 2:
                                                        Matrice[b[0]][b[1]].append(List_of_signatures[i])
                                                elif  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):

                                                    b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                                    c=perimetre_vision(1, j, k,0, Matrice)
                                                    if len(b) == 2:
                                                        d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                                    if len(b) == 2 and len(c) == 2 and len(d) == 2 :
                                                        Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                        a = a - 1
                                                elif v == a:
                                                    t = Matrice[j][k][0] 
                                                    f = 1
                                                    while t != 0:
                                                        r = perimetre_vision(f, j, k, List_of_signatures[i], Matrice)
                                                        if len(r) == 2:
                                                            t = Matrice[r[0]][r[1]][0]
                                                            x = r[0]
                                                            w = r[1]
                                                    f = f+1
                                                    Matrice[x][w][0] = 0
                                                    a = a -1
                                            elprint(a)
if i == len(List_of_signatures) - 1:
                                               #if List_of_signatures[i-1] in Matrice[j][k]:
                                                 # if subs < 0:if a == v:
                                              
                                                  #    Matrice[j][k][0] = List_of_signatures[i-1]
                                                   #    Matrice[j][k] = Matrice[j][k][0:2]
                                                    #   a = a + 1
                                                     #  subs = subs + 1
                                               #if dict[str(j)+"-"+str(k)][1] == 0:
                                               #    if subs < 0:
                                                #       Matrice[j][k][0] = 0 
                                                 #      a = a + 1
                                                  #   subs = subs + 1
                                               #elims.append(affichage(i))if dict[str(j)+"-"+str(k)][0] > 15:
                                                #   if subs <0: 
                                                 #      Matrice[j][k][0] = 0
                                                  #     a = a + 1
                                                   #    subs = subs +1
                                                    
                                                if  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                    b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                                    c=perimetre_vision(1, j, k,0)
                                                    if len(b) == 2:
                                                        d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                                    if len(b) == 2 and len(c) == 2 and len(d) == 2 :

                                                        Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                        a = a - 1
                                                elif  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                    b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                                    c=perimetre_vision(1, j, k,0, Matrice)
                                                    if len(b) == 2:
                                                         d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                                    if len(b) == 2 and len(c) == 2 and len(d) == 2 :
                                                        Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                        a = a - 1
                                                elif v == a:
                                                  ims.append(affichage(i))  t = Matrice[j][k][0] 
                                                    f = 1
                                                    while t != 0:
                                                        r = perimetre_vision(f, j, k, List_of_signatures[i], Matrice)

                                                        if len(r) == 2:
                                                            t = Matrice[r[0]][r[1]][0]
                                                            x = r[0]
                                                            w = r[1]
                                                    Matrice[x][w][0] = 0
                                                    a = a -1
                                            
                                             
                                           #elif List_of_signatures[i-1] in Matrice[j][k]:
                                            #  if subs < 0:
                                             #      Matrice[j][k][0] = List_of_signatures[i-1]
                                              #     Matrice[j][k] = Matrice[j][k][0:2]                                                
                                               #    a = a + 1
                                                #   subs = subs + 1
                                            elif random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                 b=perimetre_vision(1, j, k, List_of_signatures[i+1], Matrice)
                                                 if len(b) == 2:
                                                     Matrice[b[0]][b[1]].append(List_of_signatures[i])
                                           #elif dict[str(j)+"-"+str(k)][1] == 0:
                                             #  if subs<0:
                                              #     Matrice[j][k][0] = 0 
                                               #    a = a + 1
                                                #   subs = subs + 1    return Matrice
                                           #elif dict[str(j)+"-"+str(k)][0] > 15:
                                            #   if subs < 0: 
                                                # ims.append(affichage(i))     Matrice[j][k][0] = 0
                                              #     a = a + 1
                                               #    subs = subs + 1
                                            elif  random.randint(1, list_number_in[i]) >= list_number_in[i] // random.randint(1,5):
                                                    b=perimetre_vision(1, j, k, List_of_signatures[i], Matrice)
                                                    c=perimetre_vision(1, j, k,0, Matrice)
                                                    if len(b) == 2:
                                                        d = perimetre_vision(1, b[0], b[1], List_of_signatures[i], Matrice)
                                                    if len(b) == 2 and len(c) == 2 and len(d) == 2 :
                                                         Matrice[c[0]][c[1]].append(List_of_signatures[i])
                                                         a = a - 1

                                            elif v == a:
                                                t = Matrice[j][k][0] 
                                                f = 1
                                                while t != 0:
                                                    r = perimetre_vision(f, j, k, List_of_signatures[i], Matrice)
                                                    if len(r) == 2:
                                                        t = Matrice[r[0]][r[1]][0]
                                                        x = r[0]
                                                        w = r[1]
                                                    f = f+1
                                                Matrice[x][w][0] = 0
                                                a = a -1
                             

                            else:
                                return Matrice
                            #print(a)            affichage(update_occupied_land(Matrice, list_number_in, list_number_fin, List_of_signatures, dict, plant_signature, 0))
                            #print(Matrice)
                            #print(a)

           """                             
"""  
def creatdesp2(terrain):    #di1ctionnaire de l'espece 2 uniquement
    desp2={}
    a = 0
    for i in range(len(terrain)) :
        for j in range(len(terrain[i])) :
            for k in terrain[i][j]:
                if k != 0:m
                    desp2[str(i)+'-'+str(j)]=[1,80]
    return desp2
"""
Matrice_animaux = create_occupied_land_ecosystem([30, 50,60],[1, 2, 3], 13)

Matrice_plante = create_empty_land(13)

Matrice = Merge_matrix(Matrice_animaux, Matrice_plante)

list_number_in = [1, 1, 1]
list_number_fin = lotka_volterra_chain_one_gen(list_number_in, [[0.66, 0.75, 1, 1], [1, 0.5, 0.5, 1], [1, 0.5, 0.5, 1]])
List_of_signatures = [1, 2, 3]
plant_signature = 0

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

a = lotka_volterra_chain_n_gen([4000, 2000,1000, 500], [[0.5, 0.38, 0.6, 0.7], [0.3, 0.38, 0.004, 0.7], [0.63, 0.38, 0.004, 0.7]], 1000)
print(a)

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []


ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()


L = invert(lotka_volterra_chain_n_gen([10, 12, 10, 1], [[0.2,0.0002, 0.1, 0.1], [0.1,0.0009, 0.7, 0.1], [0.25, 0.0006, 0.3, 0.1]],200))
a = lotka_volterra_chain_n_gen([10, 12, 10, 1], [[0.2,0.0002, 0.1, 0.1], [0.1,0.0009, 0.7, 0.1], [0.25, 0.0006, 0.3, 0.1]],200)

from pylab import plt


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

a = lotka_volterra_chain_n_gen([4000, 2000,1000, 500], [[0.5, 0.38, 0.6, 0.7], [0.3, 0.38, 0.004, 0.7], [0.63, 0.38, 0.004, 0.7]], 1000)

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []

for i in a:
    v = create_occupied_land_ecosystem(i, [1, 2, 3, 4], 1000)
    t = create_empty_land(1000)
    v = Merge_matrix(v, t)
    ims.append(affichage(v))
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)
plt.show()