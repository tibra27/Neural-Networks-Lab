#!/usr/bin/env python
# coding: utf-8

# In[5]:


#ASSIGNMENT-1-QUESTION-2
#2016UCP1103
#ABHISHEK TIBREWAL
#PERCEPTRON LEARNING RULE
######################################################

import numpy as np

w=[[1],[-1],[0],[0.5]]
weight=np.array(w)
out=[1,-1,-1]
I1=np.array([[1],[-2],[1.5],[0]])
I2=np.array([[1],[-0.5],[-2],[-1.5]])
I3=np.array([[0],[1],[-1],[1.5]])
I=[I1,I2,I3]
c=1
epoc=1
while(epoc!=5):
    print("Epoc-",epoc)
    for i in range(len(I)):
        net=np.dot(np.transpose(w),I[i])
        response=1 if net>0 else -1
        w=w+c*(out[i]-response)*I[i]
        print(w)
    epoc+=1


# In[ ]:




