#!/usr/bin/env python
# coding: utf-8

# In[5]:


#ASSIGNMENT-2-QUESTION-1
#2016UCP1103
#ABHISHEK TIBREWAL
#SINGLE LAYER DISCRETE PERCEPTRON TRAINING ALGORITHM
######################################################

import numpy as np

w=[[0],[0],[0],[0]]
weight=np.array(w)
out=[-1,1,-1,1,-1,1,-1,1]
I1=np.array([[0],[0],[0],[1]])
I2=np.array([[0],[0],[1],[1]])
I3=np.array([[0],[1],[0],[1]])
I4=np.array([[0],[1],[1],[1]])
I5=np.array([[1],[0],[0],[1]])
I6=np.array([[1],[0],[1],[1]])
I7=np.array([[1],[1],[0],[1]])
I8=np.array([[1],[1],[1],[1]])
I=[I1,I2,I3,I4,I5,I6,I7,I8]
c=0.5
epoc=1
while(True):
    print("Epoc-",epoc)
    f=0
    for i in range(len(I)):
        net=np.dot(np.transpose(w),I[i])
        response=1 if net>0 else -1           #signum function
        w=w+((c*(out[i]-response)*I[i])/2)
        if(out[i]-response!=0):
            f+=1
        for j in w:
            print(j[0],end=" ")
        print("\n")
    epoc+=1
    if(f==0):
        break


# In[ ]:





# In[ ]:




