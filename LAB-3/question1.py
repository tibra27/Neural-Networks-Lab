#!/usr/bin/env python
# coding: utf-8

# In[36]:


#ASSIGNMENT-3-QUESTION-1
#2016UCP1103
#ABHISHEK TIBREWAL
#FEED-FORWARD BACK-PROPAGATION ALGORITHM
######################################################


# In[37]:


import numpy as np
import math


# In[38]:


def Activation_sigmoid(net):
    x=1/(1+(math.e**(-1*net)))
    return x


# In[39]:


alpha=0.9   #Learning Rate
d=1       #Desired output


# In[40]:


in_nodes=int(input("Enter # of input nodes:: "))
inp=list(map(float,input("Enter values of input nodes:: ").split()))
inp=[[i] for i in inp]
hide_nodes=int(input("Enter # of hidden nodes:: "))
inp=np.array(inp)

hide_weights=[]
for i in range(hide_nodes):
    print("Enter values of weights at hidden node",i+1,":: ")
    w=list(map(float,input().split()))
    w=[[i] for i in w]
    hide_weights.append(np.array(w))
print("Enter values of weights at output node:: ")
w=list(map(float,input().split()))
w=[[i] for i in w]
out_weights=np.array(w)
bias_hidden=list(map(float,input("Enter values of bias at hidden nodes:: ").split()))
bias_out=float(input("Enter values of bias at output nodes:: "))

print(inp)
print(hide_weights)
print(out_weights)
print(bias_hidden)
print(bias_out)    


# In[41]:


epoc=1000
for x in range(epoc):  
    print("EPOCH-",x+1)
    ##Feed-Forward for Hidden Layer
    hidden_inp=[]
    for i in range(hide_nodes):
        net=np.dot(np.transpose(hide_weights[i]),inp)
        net=net[0][0]
        net+=bias_hidden[i]
        out=Activation_sigmoid(net)
        hidden_inp.append([out])
    hidden_inp=np.array(hidden_inp)
    #print(hidden_inp)

    ##Feed-Forward for Output Layer
    net=np.dot(np.transpose(out_weights),hidden_inp)
    net=net[0][0]
    net+=bias_out
    out=Activation_sigmoid(net)
    #print(out)

    ##Back Propagation
    Error_out=out*(1-out)*(d-out)
    print("Error=",Error_out)
    if(Error_out<=0.001):
        break
    Error_hidden=[]
    for i in range(hide_nodes):
        err=hidden_inp[i][0]*(1-hidden_inp[i][0])*(Error_out*out_weights[i][0])
        Error_hidden.append(err)
    #print(Error_out)
    #print(Error_hidden)


    #weight update between hidden & output layer
    print("Weights at Output node::",end=" ")
    for i in range(hide_nodes):
        out_weights[i][0]+=(alpha*Error_out*hidden_inp[i][0])
        print(out_weights[i][0],end=" ")
    print("\n")
    #print(out_weights)


    #weight update between hidden & input layer
   
    for i in range(hide_nodes):
        print("Weights at Hidden node",i+1,"::",end=" ")
        for j in range(in_nodes):
            hide_weights[i][j][0]+=(alpha*Error_hidden[i]*inp[j][0]) 
            print(hide_weights[i][j][0],end=" ")
        print("\n")
    #print(hide_weights)

    #bias weight update for output layer
    bias_out+=(alpha*Error_out)
    print("Bias weight at Output node:: ",bias_out)

    #bias weight update for hidden layer
    for i in range(hide_nodes):
        print("Bias weight at Hidden node ",i+1 ,":: ",end=" ")
        bias_hidden[i]+=(alpha*Error_hidden[i])
        print(bias_hidden[i])
    print("\n")

