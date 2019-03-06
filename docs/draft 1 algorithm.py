def lotka_volterra_one_gen(proie, pred, a1, b1, c1 ,d1) :
    proie_in = proie
    predateur_in = pred
    pr = proie
    pre = pred
    pr1 = pr
    pr = pr + (a1*pr - b1*pr*pre)
    pre = pre + (c1*b1*pr1*pre - d1*pre)
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

def lotkavolterra_hybride_one_gen(pred, hybride, proie, a, b, c, d, a1, b1, c1, d1):
    effect_1 = lotka_volterra_one_gen(hybride, pred, a, b, c, d)
    effect_2 = lotka_volterra_one_gen(proie, hybride, a1, b1, c1, d1)
    effect_1 = effect_1[0], effect_1[2]
    effect_2 = effect_2[1], effect_2[3]
    effect_gen = effect_1[1] + (effect_1[0]-effect_1[1]) +(effect_2[0]-effect_1[1])
    return effect_gen

"""def lotkavolterra_hybride_n_gen(pred, hybride, proie, a, b, c, d, a1, b1, c1, d1, n):
    L_hybride = [hybride]
    L_proie = [proie]
    L_pred = [pred]
    hbr = hybride
    pr = proie
    pre = pred
    for i in range(n):
        pr= (lotka_volterra_one_gen(pr, hbr, a1, b1, c1, d1))[0]
        pre = (lotka_volterra_one_gen(hbr, pre, a, b, c, d))[1]
        hbr = lotkavolterra_hybride_one_gen(pre, hybride, pr, a, b, c, d, a1, b1, c1, d1 )
        L_hybride.append(hbr)
        L_proie.append(pr)
        L_pred.append(pred)
    return L_hybride, L_pred, L_proie

a, b, c=lotkavolterra_hybride_n_gen(1000, 100, 1000, 0.25, 0.0006, 0.5, 0.1, 0.25, 0.0006, 0.5, 0.1, 100 )

x = lotkavolterra_hybride_n_gen(1000, 100, 1000, 0.25, 0.0006, 0.5, 0.1, 0.25, 0.0001, 0.5, 0.1, 100)[0]
y = lotka_volterra_one_gen(100, 70, 0.25, 0.0006, 0.5, 0.1)[2]
z = lotka_volterra_one_gen(70, 100, 0.25, 0.0006, 0.5, 0.1)[1]

print (x)

from pylab import *
%matplotlib inline
plot(range(101), a)
plot(range(101), b)
plot(range(101), c)
show()
plot(a, b)
plot(a, c)
plot(b, c)
show()"""

def lotkavolterra_chain_ one_gen(L):
    for i in L : 
        if i = 0:
            