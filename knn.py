from math import *
#import math
import random
a_lists = open("iris.data.txt").read()
a_list = a_lists.split('\n')
#print(a_list)
alist2=[]
classification=[]
for i in a_list:
        alist2.append(i.split(','))
print(alist2)
print(len(alist2))
k=0
for i in alist2:
    blist=[]
    for j in i:
        blist.append(float(j))
    alist2[k]=blist
    k+=1
print(alist2)
tr=int(len(alist2)*9/10)
test=int(len(alist2)*1/10)
length_1fold=test
index=[]
#trdataset=[]
fold_dts=[]
tdataset=[]
'''i=0
while(i<tr):
    ran=random.randint(0,len(alist2)-1)
    if(ran not in trindex):
        trindex.append(ran)
        trdataset.append(alist2[ran])
        i+=1
i=0'''
i=0
j=0
kfold=int(input("K-fold:"))
while(j<kfold):
    tdataset=[]
    i=0
    while(i<length_1fold):
        ran=random.randint(0,len(alist2)-1)
        if(ran not in index):
            index.append(ran)
            tdataset.append(alist2[ran])
            i+=1
    fold_dts.append(tdataset)
    j+=1
            
#print(fold_dts)
#print(len(fold_dts[0]))
total=0
pre_tt=[]
rec_tt=[]
m=0
kfold1=11
knn=int(input("KNN:"))
while(m<kfold1):
    index=[]
    trdataset=[]
    testdataset=[]
    i=0
    while i<kfold-1:
        ran=random.randint(0,len(fold_dts)-1)
        if ran not in index:
            index.append(ran)
            for ii in fold_dts[ran]:
                trdataset.append(ii)
            i+=1
    i=0
    while i<1:
        ran=random.randint(0,len(fold_dts)-1)
        if ran not in index:
            #index.append(ran)
            for ii in fold_dts[ran]:
                testdataset.append(ii)
            i+=1
    print(len(testdataset))            
    print(testdataset)
    print(len(trdataset))
    print(trdataset)
    
    distance=[]
    clslis=[]
    orres=[]
    eres=[]
    tcase=0
    for i in testdataset:
        des=[]
        o=[]
        print(i)
        for j in trdataset:
            #print(j)        
            d=0    
            for k1 in range(len(j)-1):
                d+=pow(i[k1]-j[k1],2)
                
                #print(k1)
            #print(d)
            des.append(sqrt(d))
            #if len(clslis)==0:
            o.append(j[len(j)-1])
            if j[len(j)-1] not in classification:
                classification.append(j[len(j)-1])
            tcase+=1
        distance.append(des)
        
        clslis.append(o)
        orres.append(i[len(i)-1])
    #print(distance)
    #print(orres)
    #print(clslis)
    #for i in 
    for i in range(len(distance)):
        print(i)
        tempo_dis=distance[i]
        tempo_clslis=clslis[i]
        
        #cls=clslis
        for j in range(len(tempo_dis)-1):
            for jj in range(j+1,len(tempo_dis)):
                if(tempo_dis[j]>tempo_dis[jj]):
                    tempo_dis[j],tempo_dis[jj]= tempo_dis[jj],tempo_dis[j]
                    tempo_clslis[j],tempo_clslis[jj]=tempo_clslis[jj],tempo_clslis[j]
        distance[i]=tempo_dis
        clslis[i]=tempo_clslis
        
    #print(distance)
    #print(orres)
    #print(classification)
    classification.sort()
    count_for_cls=[]
    print(clslis)
    for h in clslis:
        #print(h)
        count_for_cls=[]
        for iii in range(len(classification)):
            count_for_cls.append(0)
        for jl in range(int(knn)):
            for jj in range(len(classification)):
                #print(h[jl])
                if h[jl] == classification[jj]:
                    count_for_cls[jj]+=1
        max1=max(count_for_cls)
        print(count_for_cls)
        ind=count_for_cls.index(max1)
        print(ind)
        eres.append(classification[ind])
    prscision=[]
    for i in range(len(classification)):
        prscision.append([])
        for j in range(len(classification)): 
            prscision[i].append(0)
     
    print(prscision)  
    print(classification)  
    for i in classification:
        for j in range(len(orres)):
            indqx1=classification.index(i)
            print(indqx1)
            if orres[j]==i and eres[j]==i:
                
                prscision[indqx1][indqx1]+=1
            elif orres[j]==i and eres[j]!=i:
                indqx=classification.index(eres[j])
                prscision[indqx1][indqx]+=1
    
            
    print(orres)
    print(eres)
    print(prscision)  
    acc=0
    tt_p=[]
    gT=[]
    pre_t=[]
    rec_t=[]

    totooal=0 
    for i in range(len(classification)):
        tt_p.append(0)
        gT.append(0)
        if m==0:
            pre_tt.append(0)
            rec_tt.append(0)
        pre_t.append(0)
        rec_t.append(0)
    for i in range(len(classification)):
        for j in range(len(classification)):   
            tt_p[i]+= prscision[i][j]
            totooal+=  prscision[i][j]
    for i in range(len(classification)):
        for j in range(len(classification)):   
            gT[j]+= prscision[i][j]
    #print(tt_p)
    #print(gT)  
    
    for i in range(len(prscision)):
        acc+=prscision[i][i]
        pre_t[i]=prscision[i][i]/tt_p[i]
        rec_t[i]=prscision[i][i]/gT[i]
    for i in range(len(prscision)):
        pre_tt[i]+=pre_t[i]
        rec_tt[i]+=rec_t[i]
    acc=acc/totooal
    print(acc)
    total+=acc
    m+=1
for i in range(len(prscision)):
    pre_tt[i]=pre_tt[i]/kfold1
    rec_tt[i]=rec_tt[i]/kfold1
total=total/kfold1
print(pre_tt)
print(rec_tt)
f=[]
for i in range(len(prscision)):
    f.append(0)
for i in range(len(prscision)):
    f[i]=2*(pre_tt[i]*rec_tt[i])/(pre_tt[i]+rec_tt[i])
print(f)
print(total)

