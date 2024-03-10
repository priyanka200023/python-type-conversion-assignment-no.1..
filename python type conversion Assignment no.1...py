#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT NO.1

# # python type conversion

# In[ ]:




Q.1 convert an integer to a floating point number
# In[1]:


a = 3                #this is int value
print(float(a))      #convert into float

Q.2  convert float to an integer
# In[2]:


b = 45.677           #this is float value
print(int(b))        # convert into int

Q.3 integer to a string 
# In[27]:


num = 34
print(type(num))
s =(str(num))
print(s)
print(type(s))

Q.4 convert list into tuple
# In[23]:


mylist = ["priyanka","sujata",3, 7.9]
t = tuple(mylist)
print(t)
print(type(t))

Q.5 convert tuple to list
# In[24]:


a = (1,2,3,4,5,6,7)
l = list(a)
print(l)
print(type(l))

Q.6  convert decimal to binary
# In[35]:


d = 45
print(bin(d))


# In[36]:


e = 50
print(bin(e))

Q.7 convert non-zero to boolean
# In[4]:


x = 42                #non zero number
print(bool(x))        #covert boolean


# In[2]:


y = 0
print(bool(y))


# In[3]:


num = 1
bool_num = bool(num)
print(bool_num)


# In[ ]:




