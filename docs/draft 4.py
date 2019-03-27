import random
import numpy as np
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
    L1 = [] while a != 0:
                for j in matrix:
                    for k in i:
                        for l in j:
                            if l == List_of_signatures[i]:
                                if random.randint(1, list_number_in) >= list_number_in // random.randint(1,15)  :
                                    if a != 0:
                                      
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
    return L_all, L

a = 10
b = 12          
c = 10
d = 1

L = invert(lotka_volterra_chain_n_gen([a, b, c, d], [[0.2,0.0002, 0.1, 0.1], [0.1,0.0009, 0.7, 0.1], [0.25, 0.0006, 0.3, 0.1]],200)[0])
print(L[0])
from pylab import plt

for i in L:
    plt.plot(range(201),i)
plt.show()

def test_life(L, i, j):
    return L[i][j] != 0


def create_empty_land(n):
    L= []
    for i in range(n):
        L1 = []
        for i in range(n): while a != 0: while a != 0:
                for j in matrix:
                    for k in i:
                        for l in j:
                            if l == List_of_signatures[i]:
                                if random.randint(1, list_number_in) >= list_number_in // random.randint(1,15)  :
                                    if a != 0:
                                      
                for j in matrix:
                    for k in i:
                        for l in j:
                            if l == List_of_signatures[i]:
                                if random.randint(1, list_number_in) >= list_number_in // random.randint(1,15)  :
                                    if a != 0:
                                      
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
    L = np.reshape(np.asarray(L), (len(M1), len(M2), 2))
    return L

        
def create_occupied_land(n, m, signature):
    Empty_matrix = m
    k = len(m)
    for i in range(n):          
        a = random.randint(0, k-1)
        b = random.randint(0, k-1)
        while Empty_matrix[a][b] != 0:
            a = random.randint(0, k-1) while a != 0:
                for j in matrix:
                    for k in i:
                        for l in j:
                            if l == List_of_signatures[i]:
                                if random.randint(1, list_number_in) >= list_number_in // random.randint(1,15)  :
                                    if a != 0:
                                      
            b = random.randint(0, k-1)           
        Empty_matrix[a][b] = signature
    return Empty_matrix

def create_occupied_land_ecosystem(List_number_species, List_of_signatures, m):
    """len(List_of_species == len(List_of_signature)"""
            
    General_ecosystem_matrix = create_empty_land(m)
    for i in range(len(List_number_species)-1):
       General_ecosystem_matrix = create_occupied_land(List_number_species[i], General_ecosystem_matrix, List_of_signatures[i])
    General_ecosystem_matrix = np.reshape(np.asarray(General_ecosystem_matrix), (m, m))
    return General_ecosystem_matrix
            
        
mt = create_empty_land(30)
a =create_occupied_land(100, mt, 1)
b =create_occupied_land(300, create_empty_land(70),2) 
a =create_occupied_land_ecosystem([1000,400, 700], [1, 3, 4], 70)

c = Merge_matrix(a, b)
print(c)  while a != 0:
                for j in matrix:
                    for k in i:
                        for l in j:
                            if l == List_of_signatures[i]:
                                if random.randint(1, list_number_in) >= list_number_in // random.randint(1,15)  :
                                    if a != 0:
                                      
Double_liste=Merge_matrix(a, b)

import math
Ligne=16
Colonne=16
def perimetre_vision(per,i,j, cible,Terrain) : #s'applique sur un animal de position (i,j) qui cherche une proie de valeur cible
    temp=[]
    npsh =0
    npsd =0
    npsg =0
    3npsb =0
    if i-per<0 :
        npsg=abs(i-per)      #npsg : ne pas sortir à gauche
    if i+per>len(Terrain[0]) :
        npsd = i+per-len(Terrain[0])     #npsd : ne pas sortir à droite
    if j-per<0 :
    3    npsh=abs(j-per)                 #npsh : ne pas sortir en haut
    if j+per>len(Terrain) :
        npsb = j+per-len(Terrain)      #npsb : ne pas sortir en bas
    for ligne in range(i-per+npsg,i+per-npsd-1):
        for colonne in range(j-per+npsh, j+per-npsb+1):
            #print("ligne :",ligne,"colonne :",colonne,"valeur :",Terrain[ligne,colonne])
            if cible in Terrain[ligne,colonne] :
                if len(temp)==0 :
                    temp=[ligne, colonne]
                if math.sqrt((i-ligne)**2+(j-colonne)**2)<math.sqrt((i-temp[0])**2+(j-temp[1])**2) :
                    temp=[ligne, colonne]
    return temp
b = create_occupied_land_ecosystem([30, 30, 12], [0, 1, 2], 10)
c = create_occupied_land_ecosystem([40], [3], 10)
a = Merge_matrix(b, c)
print(perimetre_vision(1, 6, 7, 1,a))


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
    plt.imshow(img)
    plt.show()
    return 

def update_occupied_land(Matrice, list_number_in, list_number_fin, List_of_signatures, dict)
    List_dif = []
    for i in range(len(list_number_in)):
        a = list_number_in - list_number_fin
        List_def.append(a)
        for i in range(len(List_dif)):
            a = abs(list_dif[i])
            while a != 0:
                for j in Matrice:
                    for k in i:
                        l = Matrice[j][k][0]
                        if a < 0
                            if l == List_of_signatures[i]:
                                if random.randint(1, list_number_in) >= list_number_in // random.randint(1,5)  :
                                    if a != 0:
                                        if i == 0:
                                            if dict[j+"-"+k][1] == 0
                                                Matrice[j][k][l] = 0 
                                                a = a + 1
                                            elif dict[j+"-"+k][0] > 15:
                                                Matrice[j][k][l] = 0
                                            elif random.randint(1, list_number_in) >= list_number_in // random.randint(1,5):
                                                Matrice[j][k][l] = 0 
                                                a = a + 1
                                            elif random.randint(1, list_number_in) >= list_number_in // random.randint(1,5):
                                                a=perimètre_vision(1, j, k, List_of_signatures[i+1])
                                                if len(a) == 2:
                                                    Matrice[a[0]][a[1]].append(List_of_signatures[i])
                                            elif  random.randint(1, list_number_in) >= list_number_in // random.randint(1,5):
                                                a=perimètre_vision(1, j, k, List_of_signatures[i])
                                                b=perimètre_vision(1, j, k,0)
                                                if len(a) == 2:
                                                    c = perimètre_vision(1, a[0], a[1], List_of_signatures[i])
                                                if len(a) == 2 and len(b) == 2 and len(c) == 2 :
                                                    Matrice[b[0]][b[1]].append(List_of_signatures[i]
                                                    a = a - 1
                                             
                                        elif List_of_signatures[i-1] in Matrice[j][k]:
                                            Matrice[j][k][l] = List_of_signatures[i-1]
                                            Matrice[j][k] = Matrice[j][k][0:2]
                                            a = a + 1
                                        elif dict[j+"-"+k][1] == 0
                                            Matrice[j][k][l] = 0 
                                            a = a + 1
                                        elif dict[j+"-"+k][0] > 15:
                                                Matrice[j][k][l] = 0
                                        
                                            
                        else :
                                if l == List_of_signatures[i]:
                                if random.randint(1, list_number_in) >= list_number_in // random.randint(1,5)  :
                                    if a != 0:
                                        if i == 0:
                                            if dict[j+"-"+k][1] == 0
                                                Matrice[j][k][l] = 0 
                                                a = a + 1
                                            elif dict[j+"-"+k][0] > 15:
                                                Matrice[j][k][l] = 0
                                            elif random.randint(1, list_number_in) >= list_number_in // random.randint(1,5):
                                                Matrice[j][k][l] = 0 
                                                a = a + 1
                                            elif random.randint(1, list_number_in) >= list_number_in // random.randint(1,5):
                                                a=perimètre_vision(1, j, k, List_of_signatures[i+1]
                                                if len(a) == 2:
                                                    Matrice[a[0]][a[1]].append(List_of_signatures[i]
                                        elif List_of_signatures[i-1] in Matrice[j][k]:
                                            Matrice[j][k][l] = List_of_signatures[i-1]
                                            Matrice[j][k] = Matrice[j][k][0:2]
                                            a = a + 1
                                        elif dict[j+"-"+k][1] == 0
                                            Matrice[j][k][l] = 0 
                                            a = a + 1
                                        elif dict[j+"-"+k][0] > 15:
                                                Matrice[j][k][l] = 0
                            
                                                
                                            
                                        
            
        



#"def dynamic_change(Matrix,dif_prey, dif_pred,a, b)
 #  " a = min(dif_prey, dif_pred) 
  #  "for i in range(a):
  #      "random.randoint"
