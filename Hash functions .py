#!/usr/bin/env python
# coding: utf-8

# In[1]:


# first try for hashmap
storage = ["Electronics","Clothing","Accessories","Books"]
sub = ["male","female"]
sub5 = ["Fiction","Biography/Autobiography","Non-Fiction","Self Help","Business","Technology"]

i = input("enter category: ")
#j = input("enter sub caategory: ")
if i==storage[0]:
    print(storage[0])
elif i==storage[1]:
    j = input("enter gender specific(male/female): ")
    if j==sub[0]:
        print(storage[1],sub[0])
    else:
        print(storage[1],sub[1])
elif i==storage[2]:
    j = input("enter gender specific(male/female): ")
    if j==sub[0]:
        print(storage[2],sub[0])
    else:
        print(storage[2],sub[1])
elif i==storage[3]:
    k = input("enter genre: ")
    if k==sub5[0]:
        print(storage[3],sub5[0])
    elif k==sub5[1]:
        print(storage[3],sub5[1])
    elif k==sub5[2]:
        print(storage[3],sub5[2])
    elif k==sub5[3]:
        print(storage[3],sub5[3])
    elif k==sub5[4]:
        print(storage[3],sub5[4])
    elif k==sub5[5]:
        print(storage[3],sub5[5])


# In[ ]:


class Product:
    def __init__(self,product):
        self.product=product
        self.next=None
class HashTable:
    def __init__(self):
        self.category = category

