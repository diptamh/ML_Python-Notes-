
# coding: utf-8

# In[1]:


a=2
print (a)


# In[4]:


import keyword
print (keyword.kwlist)


# In[5]:


for i in range (100,1,-1):
    print(i)


# In[8]:


a,b=[int (x)for x in input ("Enter 2 num:").split()]
print ("Product is :",a*b)


# In[10]:


s="Glob"
s= None
print (s)


# In[15]:


a,b,c=[int (x)for x in input ("Enter each run of a player in 3 matches:").split('!')]
print ("Total is :",a+b+c)
print ("Avg is :",(a+b+c)/3)
d,e=[int (y)for y in input ("Enter no of overs and runs given:").split('!')]
print ("Economy :",e/d)


# In[18]:


a=10
print ("The value of a is %f"%(a))


# In[22]:


s="Globsyn"
s[2:7:3]


# In[45]:


a=input ("Enter a string :")
b=len(a)
p=0
c=['A','E','I','O','U']
for x in range(b):
    if (a.find('A')):
        p=p+1
    if (a.find('E')):
        p=p+1
    if (a.find('I')):
        p=p+1
    if (a.find('O')):
        p=p+1
    if (a.find('U')):
        p=p+1
print (p)


# In[61]:


a,b,c=[str (x)for x in input ("Enter each run of a player in 3 matches:").split( )]
#print ("Total is :",a+b+c)
n=0
if(a.find("*")):
    n=n+1
if(b.find("*")):
    n=n+1
if(c.find("*")):
    n=n+1
print(n)
print ("Avg is :",(int(a [string])+(int(b [string])+(int(c [string]))/(3-n))


# In[62]:


rec={}
n=int(input ("Enter student in number"))
i=1
while i<=n:
    name=input("Enter student name: ")
    marks =input("Enter % of marks of student: ")
    rec[name]=marks
    i=i+1
print ("Name of student ","\t","% of marks")
for x in rec:
    print ("\t",x,"\t\t",rec[x])


# In[ ]:


rec={}
n=int(input ("Enter student in number"))
i=1

while i<=n:
    name=input("Enter student name: ")
    marks =input("Enter % of marks of student: ")
    rec[name]=marks
    i=i+1
print ("Name of student ","\t","% of marks")
for x in rec:
    print ("\t",x,"\t\t",rec[x])

