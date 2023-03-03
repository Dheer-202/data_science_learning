#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 1
print('The keyword use to create a function is "def".')

def odd_num(a,b):
    lis= []
    for i in range(a,b+1):
        if i%2!=0:
            lis.append(i)
    return lis

print(odd_num(1,25))


# In[ ]:


#quest 2
print("*args and **kwargs are used in function when we have to give many variables to a fuction. In which **kwargs is used when variables are in key word and value pair while *args is used when variables ar not value pairs")

def addd(*args):
    '''this code return all string value from variables'''
    b = args
    lis=[]
    for i in b:
        if type(i)== type("fgh"):
            lis.append(i)
    return lis

def ret(**kwargs):
    b= kwargs
    


# In[ ]:


#quest 3 

print("An iterator is a function which give us next consecutive value of iterables.")
print("the method used to initialise the iterator object is Iter() and the method used for iteration is Next().")

inp_lis= [2*i for i in range (1,11)]
inp_lis = iter(inp_lis)
for  i in range(0,5):
    print(next(inp_lis))


# In[ ]:


# ques 4
print("generally all function first run the code and store the results in memory then return all outputs. during it function store a large memory but generator function give the output as it evaluate without storing it in memory.")
print("the keyword yield is used to make a generator function.")
def fact(n):
    if n>=0:
        if n==0:
            return 1
        else:
            return n*fact(n-1)
    else:
        return "invalid input"  


def expo(n):
    for i in range (0,50):
        nth_term = (n**i)/fact(i)
        yield nth_term
    
obj= expo(6)
summ= 0
for i in obj:
    print(i)


# In[ ]:


#ques 5
def prim(n):
    for i in range(2,n+1):
        a=True
        for j in range(2,i):
            if i%j==0:
                a= False
                continue
        if a==True:
            yield i

obc= prim(10)
for i in obc:
    print(i)


# In[ ]:


#quest 06
x,y=0,1
i=1
while 0<i<11:
    val= x+y
    x=y
    y=val
    print(val)
    i+=1
    


# In[ ]:


#question no 7

a =['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
lis= []
for i in a:
    lis.append(i)
print(lis)


# In[ ]:


#quest 8
#checking pallindromic sequence

def pallindroem(a):
    if type(a)==str:
        a=a.lower()
    n= len(a)
    val=True
    if n/2==0:
        i=0
        while i<n/2:
            if a[i]!=a[n-1-i]:
                val= False
                break
            i+=1
    else:
        i=0
        while i<(n+1)/2:
            if a[i]!=a[n-1-i]:
                val= False
                break
            i+=1
    return val

print(pallindroem('mAlayalam'))


# In[ ]:


#questiion no 9
a= [i for i in range(1,101)]
odd = [i for i in a if i%2!=0]
print(odd)

