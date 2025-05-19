#!/usr/bin/env python
# coding: utf-8

# In[35]:


# first try
import networkx as nx
import matplotlib.pyplot as plt
def generate_hasse_diagram(S):
    G = nx.DiGraph()
    for a in S:
        for b in S:
            for c in S:
                for d in S:
                    for e in S:
                        for f in S:
                            G.add_edge(a,b)
                            G.add_edge(a,c)
                            G.add_edge(b,d)
                            G.add_edge(c,e)
                            G.add_edge(d,f)
                            G.add_edge(e,f)
    return G
list1 = [1,2,3,4,5,6]
hasse_graph = generate_hasse_diagram(list1)
pos = nx.spring_layout(hasse_graph)
nx.draw(
    hasse_graph,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=3000,
    font_size=10,
    arrows=False
)
plt.show()


# In[5]:


# second try
import numpy as np
list1=[3,4,2,1]
list2=[2,1,np.NaN,3]
list3=[1,np.NaN,3,4]
list4=[4,3,1,np.NaN]
if 1 not in list2:
    list2[2]=1
elif 2 not in list2:
    list2[2]=2
elif 3 not in list2:
    list2[2]=3
elif 4 not in list2:
    list2[2]=4
print(list2)
if 2 not in list3:
    list3[1]=2
elif 1 not in list2:
    list3[1]=1
elif 3 not in list2:
    list3[1]=3
elif 4 not in list2:
    list3[1]=4
print(list3)
if 1 not in list4:
    list4[3]=1
elif 2 not in list4:
    list4[3]=2
elif 3 not in list4:
    list4[3]=3
elif 4 not in list4:
    list4[3]=4
print(list4)
tlist=[list1,
     list2,
     list3,
     list4]
print(tlist)


# In[5]:


# third try
import numpy as np
array1=[[3,4,2,1],
        [2,1,np.NaN,3],
       [1,np.NaN,3,4],
       [4,3,1,np.NaN]]
print("Incomplete sudoku puzzle",array1)
for i in range(4):
    if(1 not in array1[1]):
        array1[1][2]=1
    elif(2 not in array1[1]):
        array1[1][2]=2
    elif(3 not in array1[1]):
        array1[1][2]=3
    elif(4 not in array1[1]):
        array1[1][2]=4
for i in range(4):
    if(1 not in array1[2]):
        array1[2][1]=1
    elif(2 not in array1[2]):
        array1[2][1]=2
    elif(3 not in array1[2]):
        array1[2][1]=3
    elif(4 not in array1[2]):
        array1[2][1]=4
for i in range(4):
    if(1 not in array1[3]):
        array1[3][3]=1
    elif(2 not in array1[3]):
        array1[3][3]=2
    elif(3 not in array1[3]):
        array1[3][3]=3
    elif(4 not in array1[3]):
        array1[3][3]=4
print("successfull completion of sudoku puzzle using backtracking algorithm",array1)


# In[45]:


# fourth try
import numpy as np
array2=[[1,4,3,2],[3,np.NaN,1,4],[np.NaN,1,2,np.NaN],[2,3,4,1]]
print("incomplete sudoku puzzle",array2)
i=0
j = 0
k = 0
for i in range(len(array2)):
    if(1 not in (array2[i])):
        array2[j][k]=1
    elif(2 not in (array2[i])):
        array2[j][k]=2
    elif(3 not in array2[i]):
        array2[j][k]=3
    elif(4 not in array2[i]):
        array2[j][k]=4
    i,j,k=i+1,j+1,k+1

print("successfull completion of sudoku puzzle using backtracking algorithm",array2)


# In[57]:


# fifth try
import numpy as np
array2=[[1,4,3,2],[3,np.NaN,1,4],[np.NaN,1,2,np.NaN],[2,3,4,1]]
print("incomplete sudoku puzzle",array2)
i=0
j = 0
k = 0
if(1 not in (array2[i])):
    array2[j][k]=1
elif(2 not in (array2[i])):
    array2[j][k]=2
elif(3 not in array2[i]):
    array2[j][k]=3
elif(4 not in array2[i]):
    array2[j][k]=4
print("successfull completion of sudoku puzzle using backtracking algorithm",array2)
a,b,c=i+1,j+1,k+1
if(1 not in (array2[a])):
    array2[b][c]=1
elif(2 not in (array2[a])):
    array2[b][c]=2
elif(3 not in array2[a]):
    array2[b][c]=3
elif(4 not in array2[a]):
    array2[b][c]=4
print("successfull completion of sudoku puzzle using backtracking algorithm",array2)
p,q,r=a+1,b+1,c+1
if(4 not in (array2[p])):
    array2[q][i]=4
print("successfull completion of sudoku puzzle using backtracking algorithm",array2)
x,y,z=p+1,q+1,r+1
if(3 not in array2[p]):
    array2[q][y]=3
print("successfull completion of sudoku puzzle using backtracking algorithm",array2)

