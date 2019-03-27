dict1={"ab":3,"aa":4}
dict2={"ab":3,"aa":4}
dict3={"ab":3,"aa":4}
def perimetre_vision(ic,jc) :
    return [ic,jc]
        
def deplacement1(i,j,per, cible, Terrain):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            dict1[str(i+1)+"-"+str(j)]=dict1.pop[str(i),str(j)]
        else :
            dict1[str(i-1)+"-"+str(j)]=dict1.pop[str(i),str(j)]
    if k[1]==j :
        if k[0]>i :
            dict1[str(i)+"-"+str(j+1)]=dict1.pop[str(i),str(j)]
        else :
            dict1[str(i)+"-"+str(j-1)]=dict1.pop[str(i),str(j)]
    if k[0]<i :
        if k[i]<j :
            dict1[str(i-1)+"-"+str(j-1)]=dict1.pop[str(i),str(j)]
        else : 
            dict1[str(i-1)+"-"+str(j+1)]=dict1.pop[str(i),str(j)]
    else :
        if k[i]>j :
            dict1[str(i+1)+"-"+str(j+1)]=dict1.pop[str(i),str(j)]
        else :
            dict1[str(i+1)+"-"+str(j-1)]=dict1.pop[str(i),str(j)]

def deplacement2(i,j,per, cible, Terrain):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            dict2[str(i+1)+"-"+str(j)]=dict2.pop[str(i),str(j)]
        else :
            dict2[str(i-1)+"-"+str(j)]=dict2.pop[str(i),str(j)]
    if k[1]==j :
        if k[0]>i :
            dict2[str(i)+"-"+str(j+1)]=dict2.pop[str(i),str(j)]
        else :
            dict2[str(i)+"-"+str(j-1)]=dict2.pop[str(i),str(j)]
    if k[0]<i :
        if k[i]<j :
            dict2[str(i-1)+"-"+str(j-1)]=dict2.pop[str(i),str(j)]
        else : 
            dict2[str(i-1)+"-"+str(j+1)]=dict2.pop[str(i),str(j)]
    else :
        if k[i]>j :
            dict2[str(i+1)+"-"+str(j+1)]=dict2.pop[str(i),str(j)]
        else :
            dict2[str(i+1)+"-"+str(j-1)]=dict2.pop[str(i),str(j)]
            
def deplacement3(i,j,per, cible, Terrain):
    k=[]
    k=perimetre_vision(per,i,j, cible,Terrain)
    if k[0]==i :
        if k[1]>j :
            dict3[str(i+1)+"-"+str(j)]=dict3.pop[str(i),str(j)]
        else :
            dict3[str(i-1)+"-"+str(j)]=dict3.pop[str(i),str(j)]
    if k[1]==j :
        if k[0]>i :
            dict3[str(i)+"-"+str(j+1)]=dict3.pop[str(i),str(j)]
        else :
            dict3[str(i)+"-"+str(j-1)]=dict3.pop[str(i),str(j)]
    if k[0]<i :
        if k[i]<j :
            dict3[str(i-1)+"-"+str(j-1)]=dict3.pop[str(i),str(j)]
        else : 
            dict3[str(i-1)+"-"+str(j+1)]=dict3.pop[str(i),str(j)]
    else :
        if k[i]>j :
            dict3[str(i+1)+"-"+str(j+1)]=dict3.pop[str(i),str(j)]
        else :
            dict3[str(i+1)+"-"+str(j-1)]=dict3.pop[str(i),str(j)]

