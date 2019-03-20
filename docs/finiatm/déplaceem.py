def perimetre_vision(ic,jc) :
    return [ic,jc]
def deplacement(i,j,per, cible, Terrain):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            return [i+1,j]
        else :
            return [i-1,j]
    if k[1]==j :
        if k[0]>i :
            return [i,j+1]
        else :
            return [i,j-1]
    if k[0]<i :
        if k[i]<j :
            return [i-1,j-1]
        else : 
            return [i-1,j+1]
    else :
        if k[i]>j :
            return [i+1,j+1]
        else :
            return [i+1,j-1]
        
    