#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class stack():
    items=[]
    def init(self):
        self.items([])
    def push(self,item):
        self.items.append(item)
        return self.items
    def peek(self,item):
        self.items.head(item)
        return self.items
    def pop(self, item):
        self.items.drop(item)
        return self.items
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    choice = int(input("Enter your choice:"))
    a = int(input())
    b = int(input())
    if choice==1:
        print(a+b)
    elif choice==2:
            print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a/b)
    else:
        print("Invalid option")


# In[ ]:




