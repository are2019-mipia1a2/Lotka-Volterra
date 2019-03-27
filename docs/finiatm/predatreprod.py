def predation(d_pred,d_cible,cible,i,j,pos_cible_i,pos_cible_j,terrain):
    d_pred[str(i)+"-"+str(j)][1]+=20
    del d_cible[str(pos_cible_i)+"-"+str(pos_cible_j)]
    terrain[pos_cible_i,pos_cible_j].remove(cible)
    return

def reproduction(d_pred,i,j,pos_cible_i,pos_cible_j,terrain) :
    if i==pos_cible_i :
        if terrain[i+1,j]==[0] :
            d_pred[str(i+1)+"-"+str(j)]=[1,80]
        elif terrain[i+1,pos_cible_j]==[0] :
            d_pred[str(i+1)+"-"+str(pos_cible_j)]=[1,80]
        elif terrain[i-1,j]==[0] :
            d_pred[str(i-1)+"-"+str(j)]=[1,80]
        elif terrain[i-1,pos_cible_j]==[0] :
            d_pred[str(i-1)+"-"+str(pos_cible_j)]=[1,80]
    if j==pos_cible_j :
        if terrain[i,j+1]==[0] :
            d_pred[str(i)+"-"+str(j+1)]=[1,80]
        elif terrain[pos_cible_i,j+1]==[0] :
            d_pred[str(pos_cible_i)+"-"+str(j+1)]=[1,80]
        elif terrain[i,j-1]==[0] :
            d_pred[str(i)+"-"+str(j-1)]=[1,80]
        elif terrain[pos_cible_i,j-1]==[0] :
            d_pred[str(pos_cible_i)+"-"+str(j-1)]=[1,80]
    if i==pos_cible_i+1 :
        if j==pos_cible_j+1 :
            if terrain[i+1,j]==[0] :
                d_pred[str(i+1)+"-"+str(j)]=[1,80]
            elif terrain[i,j+1]==[0] :
                d_pred[str(i)+"-"+str(j+1)]=[1,80]                
    if i==pos_cible_i-1 :
        if j==pos_cible_j+1 :
            if terrain[i-1,j]==[0] :
                d_pred[str(i-1)+"-"+str(j)]=[1,80]
            elif terrain[i,j+1]==[0] :
                d_pred[str(i)+"-"+str(j+1)]=[1,80]
    return