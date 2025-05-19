#!/usr/bin/env python
# coding: utf-8

# In[1]:


# this is a brief overview of linked list implementation of stack before learning about the application
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        iternode=self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode!=None):
                print(iternode.data,end="")
                iternode=iternode.next
                if(iternode!=None):
                    print("\n")
            return
stack = Stack()
stack.push("https://woxsen.edu.in/technology/b-tech-data-science")
stack.push("https://woxsen.edu.in/technology")
stack.push("https://woxsen.edu.in")
stack.display()
print("\nTop element:",stack.peek())
print("\nPopped element:",stack.pop())
stack.display()


# In[2]:


# this is an application of a stack for a simple chatbot for university website navigation using push function and it shows basic functions of a user input with a response using conditional control statements.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        iternode=self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode!=None):
                print(iternode.data,end="")
                iternode=iternode.next
                if(iternode!=None):
                    print("\n")
            return
print("Woxsen Univeristy's Technological perspective")
stack = Stack()
user=input("Website Visitor: ")
print("You are now chatting with the chatbot from the admissions team")
stack.push(user)
if user=="Hello":
    response="Greetings, visitor! I hope that the visit is good.\nFeel free to ask anything! Till then i could show the programs offered for entry of first,\nthen a vision behind Woxsen Univeristy from the Vice President for the entry of second"
    stack.push(response)
    stack.display()
    choose=input()
    if(choose=="first"):
        response="https://woxsen.edu.in/schools/technology/"
    elif(choose=="second"):
        response="https://youtu.be/8OmO7hYRs1U?si=wSsGdRzffnFaMC9T"
    else:
        response="Invalid choice"
    stack.push(response)
    stack.display()
else:
    response="Please reframe your statement due to my lack of educational qualifications"
    stack.push()
    stack.display()

