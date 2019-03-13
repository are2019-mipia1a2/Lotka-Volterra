import numpy as np
#import Image as imag
import matplotlib.pyplot as plt  
import random

plaine =('oifdnzoenfze',2/5)
montagne=('ppp',1/8)
foret=('ppp',1/3)


                                           
def terrain_base(environnement) :
    """crée la matrice terrain base"""
    base=np.reshape(np.asarray([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]),(4,4)) 
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
    for x in range(4) :
        for y in range (4) :
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
                
    
    a=(np.reshape(np.asarray(a),(4,4))).dot(base)
    if random.random()<0.5 :
        a=np.transpose(a)
    b=(np.reshape(np.asarray(b),(4,4))).dot(base)
    if random.random()<0.5 :
        b=np.transpose(b)
    c=(np.reshape(np.asarray(c),(4,4))).dot(base)
    if random.random()<0.5 :
        c=np.transpose(c)
    d=(np.reshape(np.asarray(d),(4,4))).dot(base)
    if random.random()<0.5 :
        d=np.transpose(d)
    tempA=np.concatenate((a,b),axis=1)
    tempB=np.concatenate((c,d),axis=1)
    A=np.concatenate((tempA,tempB),axis=0)
    return A
def terrain_final(environnement) :
    return np.concatenate((np.concatenate((terrain_base(environnement),terrain_base(environnement)),axis=1),np.concatenate((terrain_base(environnement),terrain_base(environnement)),axis=1)),axis=0)
def affichage(matrice) :
    """permet d'afficher le terrain uniquement"""
    img=[]
    for j in matrice :
       temp=[]
       for k in j :
            if k==0 :
                temp.append((51,153,0))
            else : 
                temp.append((204,153,51))
       img.append(temp)      
    plt.imshow(img)
    plt.show()
    return   
def randomi(environnement) :
    _, a=environnement
    if a<random.random() :
        return 1
    else : 
        return 0