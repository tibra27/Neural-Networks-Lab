#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT-6-QUESTION-1
#2016UCP1103
#ABHISHEK TIBREWAL
#SELF ORGANISING MAPS
######################################################


# In[62]:


def function(p):
    if(p>=1 and p<=4):
        return 0.6
    elif(p>=5 and p<=8):
        return 0.5
    else:
        return 0.4


# In[63]:


I1=[1,1,0,0]
I2=[0,0,0,1]
I3=[1,0,0,0]
I4=[0,0,1,1]
I=[I1,I2,I3,I4]

W1=[0.2,0.6,0.5,0.9]
W2=[0.8,0.4,0.7,0.3]
W=[W1,W2]
m=len(W)   #No. of output units
p=12    #No. of iterations


# In[64]:


p_it=0
for i in range(int(p/len(I))):
    for j in range(len(I)):
        p_it+=1
        mn=100000000000000
        unit=0
        for k in range(m):
            x=0
            for t in range(len(I[j])):
                x+=((W[k][t]-I[j][t])**2)
            if(x<mn):
                mn=x
                unit=k+1
        s=0
        print("Iteration-",p_it)
        print("Winner is-",unit)
        #for t in range(len(I[j])):
            #s+=(I[j][t]-W[unit-1][t])
        #print(s)
        for t in range(len(W[unit-1])):
            W[unit-1][t]+=(function(p_it)*(I[j][t]-W[unit-1][t]))
        for t in range(m):
            print("\t\tW",t+1,"-",W[t])
            
        


# In[ ]:




