#!/usr/bin/env python
# coding: utf-8

# In[3]:


def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
num=7
print("factorial of",num,"is",factorial(num))


# In[4]:


def factorial(n):
    return 1 if(n==0 or n==1) else(n*factorial(n-1))
num=5
print("factorial of",num,"is",factorial(num))


# In[ ]:




