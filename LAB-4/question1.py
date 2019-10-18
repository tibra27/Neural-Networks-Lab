#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT-4-QUESTION-1
#2016UCP1103
#ABHISHEK TIBREWAL
#AUTO ASSOCIATIVE MEMORY MODEL
######################################################


# In[2]:


import numpy as np


# In[3]:


def activate(x,y):
    if(x>0):
        return 1
    elif(x==0):
        return y
    return -1


# In[4]:


X1=np.array([[-1],[1],[-1],[1]])
X2=np.array([[1],[1],[1],[-1]])
X3=np.array([[-1],[-1],[-1],[1]])

m=3
p=len(X1)

X=[X1,X2,X3]


# In[5]:


M=X[0].dot(np.transpose(X[0]))
for i in X[1:]:
    M+=i.dot(np.transpose(i))
print(M)


# In[6]:


inp=np.array([[1],[1],[1],[-1]])
out=[]
for i in range(p):
    t=[]
    t.append(M[:,i])
    out.append(activate(np.transpose(inp).dot(np.transpose(np.array(t))),inp[i][0]))
print(out)


# In[ ]:





# In[ ]:




