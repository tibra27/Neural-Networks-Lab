#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT-5-QUESTION-1
#2016UCP1103
#ABHISHEK TIBREWAL
#K-MEANS CLUSTERING ALGORITHM
######################################################


# In[4]:


import numpy as np
def manhatten(a,b):
    dx1=a[0]-b[0]
    dx2=a[1]-b[1]
    return(abs(dx1)+abs(dx2))


# In[5]:


X=[[2,2],[8,8],[7,7],[3,3],[2,3],[7,8]]
k=int(input("Enter the #clusters you want to make...."))
#print(k)
prev_C=[]
c_list=[]
for i in range(k):
    c_list.append([])
    print("Enter cenroid-",i," (x1 x2)-")
    prev_C.append(list(map(int,input().split())))



for i in range(len(X)):
    temp=[]
    for j in range(len(prev_C)):
        temp.append(manhatten(X[i],prev_C[j]))
    q=temp.index(min(temp))
    c_list[q].append(i)
print("Initial centroid:",prev_C)



it=1
while(True):
    new_C=[]
    for i in range(k):
        nodes=c_list[i]
        x1=0
        x2=0
        for j in range(len(nodes)):
            x1+=X[nodes[j]][0]
            x2+=X[nodes[j]][1]
        x1/=len(nodes)
        x2/=len(nodes)
        new_C.append([x1,x2])
    print("Centroid after Iteration-",it,":",new_C)
    print("Cluster after Iteration-",it,":",c_list)
    it+=1
    c_list=[]
    for i in range(k):
        c_list.append([])
    for i in range(len(X)):
        temp=[]
        for j in range(len(new_C)):
            temp.append(manhatten(X[i],new_C[j]))
        q=temp.index(min(temp))
        c_list[q].append(i)
    if(prev_C==new_C):
        print("Terminated....as last 2 iteration having same centroids")
        break
    prev_C=new_C
    
   # print("Initial centroid:",C)
   # print("Cluster after Iteration-",it,c_list)
    
            
    


# In[ ]:




