#!/usr/bin/env python
# coding: utf-8

# # Basic

# In[1]:


print ("Hello World")


# In[2]:


print("Programming in Python is fun!")


# ## Calculation

# In[3]:


print (4 + 5)


# In[5]:


print (5 - 2)


# In[6]:


print (8 * 7)


# In[7]:


print (20 / 100)


# In[8]:


print (2 ** 10)


# #### Calculate the Golden ratio:1+√5/2

# In[1]:


ratio =((1+5**(1/2))/2)
print(ratio)


# #### Use Python to calculate (((1+2)∗3)/4)^5

# In[2]:


print((((1+2)*3)/4)**5)


# #### Most hard drives are divided into sectors of 512 bytes each.Our disk has a size of 16 GB.Fill in the blank to calculate how many sectors the disk has. Note: Your result should be in the format of just a number, not a sentence.

# In[1]:


disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount)


# ## Data Type

# In[3]:


a=4
print(type(a))


# In[4]:


a="Hello World"
print(type(a))


# In[5]:


a=20.9
print(type(a))


# In[8]:


a= 1j
print(type(a))


# In[9]:


a= True
print(type(a))


# In[11]:


a=["car","bike","truck"]
print(type(a))


# In[12]:


a=("car","bike","truck")
print(type(a))


# In[15]:


a={"Name":"Hira" , "Age":"21" , "Gender":"female"}
print(type(a))


# In[16]:


a=range(10)
print(type(a))


# In[17]:


a=memoryview(bytes(6))
print(type(a))


# In[10]:


a= None
print(type(a))


# ## Variables

# In[19]:


var = 45
print(var)


# In[20]:


a = 5
b = "Hira"
print(a)
print(b)


# In[25]:


a = int(24)
b = str(32)
c = float(44)
print(a)
print(b)
print(c)


# ### Legal Variable Name

# In[ ]:


myvar = "Hira"
my_var = "Hira"
_my_var = "Hira"
myVar = "Hira"
MYVAR = "Hira"
myvar2 = "Hira"


# ### Camel Case
# myVariableName = "Hira"
# 

# ### Pascal Case
# MyVariableName = "Hira"

# ### Snake Case
# my_variable_name = "Hira"

# In[27]:


fruits = ["car", "bike", "truck"]
a, b, c = fruits
print(a)
print(b)
print(c)


# ## Casting Variable

# In[2]:


a = int(1)
b = int(3.9)
c = int("6")
print(a)
print(b)
print(c)


# In[3]:


a = float(8)
b = float(4.8)
c = float('9')
print(a)
print(b)
print(c)


# In[4]:


a = str("Hira")
b = str(3)
c = str(4.8)
print(a)
print(b)
print(c)

