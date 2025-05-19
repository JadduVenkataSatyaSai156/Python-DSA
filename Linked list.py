#!/usr/bin/env python
# coding: utf-8

# In[2]:


# first try
class student_info:
    def init(name):
        self.name = name
    def init(roll):
        self.roll = roll
    def init(marks):
        self.marks = marks
    def init(none):
        self.none = none
    def init(self):
        if self.head == none:
            def add_students(self, name, roll, marks):
                name = input()
                roll = int(input())
                marks = int(input())
                return name, roll, marks
            name1 = input()
            roll1 = int(input())
            marks1 = int(input())
            self.head = add_students(name1, roll1, marks1)
            print(self.head)


# In[6]:


# second try
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next= new_node
    def print_list(self):
        current_node=self.head
        while current_node:
            print(current_node.data,end=" -> ")
            current_node=current_node.next
        print("None")
llist = LinkedList()
stu_name = input()
stu_roll = input()
stu_marks = int(input())
stu_gpa = (stu_marks+20)/20
if stu_gpa>=2 and stu_gpa<4:
    stu_gpa = 5
llist.append(stu_name)
llist.append(stu_roll)
llist.append(stu_gpa)
llist.print_list()

