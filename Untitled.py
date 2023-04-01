#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


#ques 1
ser = pd.Series((4,8,15,16,23,42))
print(ser)


# In[ ]:


#quest 2
a= [ i for i in range(1,101) if i%10==0]
a= pd.Series(a)
print(a)


# In[ ]:


#quest 3
dic = {
    'Name': ['Alice', 'Bob','Claire'],
    'Age': [25,30,27],
    'Gende0r': ["Female","Male","Female"]
}
df = pandas.DataFrame(dic)


# In[ ]:


#ques 4
print("DataFrame is tabular representation of any data. It is different from Series as bieng a 2-D dimensional data while Series is 1-D representation of Data.")


# In[ ]:


#quest 5
print("Some Common Function to manipulate Data are pandas.iloc(), pandas.head(), pandas.tail(), pandas.drop()")
print(df)
school = ['GOV', 'PRIVATE', 'GOV']
df.insert(3,'school',school)
print(df)


# In[ ]:


#ques 6
print("Series and Dataframe are value mutable but not size mutable.")


# In[ ]:


#quest 7
a= df['Name']
b= df['Age']
c= df['school']
data = pd.DataFrame(a)
data.insert(1,'Age', b)
data.insert(2,'school',c)
print(data)


# In[ ]:




