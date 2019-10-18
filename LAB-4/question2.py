#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT-4-QUESTION-2
#2016UCP1103
#ABHISHEK TIBREWAL
#HETERO ASSOCIATIVE MEMORY MODEL
######################################################


# In[6]:


import numpy as np


# In[7]:


def activate(x):
    res=[]
    for i in range(len(x[0])):
        if x[0][i]>0:
            res.append(1)
        else:
            res.append(-1)
    t=[]
    t.append(res)
    t=np.array(t)
    return t
        


# In[8]:


X1=np.array([[1,-1,-1,-1,-1,1]])
X2=np.array([[-1,1,1,-1,-1,-1]])
X3=np.array([[-1,-1,1,-1,1,1]])

Y1=np.array([[1,1,-1,-1,-1]])
Y2=np.array([[1,-1,1,-1,-1]])
Y3=np.array([[-1,1,1,1,-1]])

m=3
p=len(X1)

X=[X1,X2,X3]
Y=[Y1,Y2,Y3]


M=np.transpose(X[0]).dot(Y[0])
for i in range(1,m):
    M+=(np.transpose(X[i]).dot(Y[i]))
print(M)


# In[9]:


alpha=np.array([[-1,-1,-1,-1,-1,-1]])
beta_old=activate(alpha.dot(M))
print(beta_old)
while(True):
    alpha_new=activate(beta_old.dot(np.transpose(M)))
    beta_new=activate(alpha_new.dot(M))
    if np.array_equal(beta_new,beta_old):
        print("TERMINATION..........")
        print(beta_new)
        break
    beta_old=beta_new


# In[ ]:




