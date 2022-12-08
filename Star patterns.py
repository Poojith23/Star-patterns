#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()


# In[2]:


a = 8
for i in range(0, 5):
    for j in range(0, a):
        print(end=" ")
    a = a - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()


# In[3]:


k = 16
l = 1
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 4
    for j in range(0, l):
        print("* ", end="")
    l = l + 2
    print()


# In[6]:


# Program to print full pyramid 
num_rows = int(input("Enter the number of rows"));
for i in range(0, num_rows):
    for j in range(0, num_rows-i-1):
        print(end=" ")
    for j in  range(0, i+1):
        print("*", end=" ")
    print()


# In[ ]:




