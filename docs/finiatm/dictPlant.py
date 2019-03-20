import TravailTerrain as tt
ter=tt.k
def creatdplant(terrain):    #dictionnaire des plantes uniquement
    dplant=dict()
    for i in range(len(terrain)) :
        for j in terrain[i] :
            if terrain[i,j]==1 :
                dplant[str(i)+'-'+str(j)]=100
    return dplant