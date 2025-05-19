#!/usr/bin/env python
# coding: utf-8

# In[69]:


# first try
from array import *
price_1 = [10,20,30,40,50]
popularity_1 = ["low","medium","high"]
categories_1 = ["clothing","apparel","electronics"]
#for i in price_1:
#    print(i)
#for j in popularity_1:
#    print(j)
#for k in categories_1:
#    print(k)
# bubble sort
#def bubble_sort(price):
#n = len(price_1)
for i in range(len(price_1)):
    price_1[i],price_1[i-1]=price_1[i-1],price_1[i]
    print("price based on popularity:",price_1)
    break
#bubble_sort(price_1)
#def bubble_sort1(popularity):
for m in range(len(popularity_1)):
    popularity_1[m],popularity_1[m-1]=popularity_1[m-1],popularity_1[m]
    print("popularity based on high price:",popularity_1)
    break
#for k in range(m-1):
 #   for h in range(0,m-k-1):
  #      if popularity_1[h]>popularity_1[h+1]:
   #         popularity_1[h],popularity_1[h+1]=popularity_1[h+1],popularity_1[h]
    #        print(popularity_1)
#bubble_sort1(popularity_1)
#print(bubble_sort(price_1),bubble_sort1(popularity_1))


# In[ ]:




