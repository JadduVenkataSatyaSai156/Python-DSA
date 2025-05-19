#!/usr/bin/env python
# coding: utf-8

# In[8]:


# first try
class Ticket:
    def __init__(self,customer_name,issue,priority):
        self.customer_name = customer_name
        self.issue = issue
        self.priority  =priority
class TicketingSystem:
    def __init__(self):
        self.queue = []
    def processing(self,customer_name,issue,priority):
        if None:
            queue = []
            queue.append(customer_name)
            queue.append(issue)
            queue.append(priority)
            return 
ticketingsystem = TicketingSystem()
print("select choices in the tickeitng system")
print("\n1.submit a ticket\n2.process a ticket\n3.display a ticket")
queue = []
choice  =int(input())
customer_name = input()
issue = input()
priority = input()
print("customer name:",customer_name,"\nissue:",issue,"\npriority:",priority)
if choice==1:
    if priority==("high"):
        queue.enque(issue)
        queue.deque(issue)
    else:
        queue.append(issue)
elif choice==2:
    queue.enque(customer_name)
elif choice==3:
    queue.enque(customer_name)
else:
    print("invalid choice")

