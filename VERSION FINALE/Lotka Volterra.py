from tkinter import *
import numpy as np
import matplotlib.pyplot as plt  
import random
import math
import matplotlib.animation as animation
import pygame

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

