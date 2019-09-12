#ASSIGNMENT-1-QUESTION-1
#2016UCP1103
#ABHISHEK TIBREWAL
#HEBBIAN LEARNING RULE
######################################################

import numpy as np

w=[[1],[-1],[0],[0.5]]
weight=np.array(w)

x1=np.array([1],[-2],[1.5],[0])
x2=np.array([1],[-0.5],[-2],[-1.5])
x3=np.array([0],[1],[-1],[1.5])

c=1

net1=np.dot(np.transpose(w),x1)
response1=1 if net1>0 else -1
print(response1)
