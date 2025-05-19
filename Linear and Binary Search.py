#!/usr/bin/env python
# coding: utf-8

# In[3]:


# first try of linear search
Array1 = ["Electronics","Clothing","Books","Furniture"]
name = input("choose any option of categories-\n1).Electronics\n2).Clothing\n3).Books\n4).Furniture\n selected option:")
for i in Array1:
    if i==name:
        print(i)
        break
    else:
        print("Invalid Choice")


# In[7]:


#second try for linear search
Array1 = ["Electronics","Clothing","Books","Furniture"]
name=input("enter  choice: ")
for i in Array1:
    if i==name:
        print(Array1.index(i),i)


# In[1]:


# first try for binary search
Array2 = ["Electronics","Clothing","Books","Furniture"]
name = input("choose any option of categories-\n1).Electronics\n2).Clothing\n3).Books\n4).Furniture\n selected option:")
n = len(Array2)
a1 = Array2[n-n]
a2 = Array2[n-1]
ai1 = Array2.index(a1)
ai2 = Array2.index(a2)
avg = (((ai1)+(ai2))/2)
iavg = int(avg)
for iavg in range(n):
    if Array2[iavg]==name:
        print(iavg,Array2[iavg])
        iavg=iavg+1
        break

