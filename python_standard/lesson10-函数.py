

def function3(a=10,b=20): #����Ĭ��ֵ
    c = a + b
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',c)

a = 1000


# In[24]:

def function5(b=20): #����Ĭ��ֵ
    global a   #ʹ��ȫ�ֱ���
    c = a + b
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',c)


# In[25]:

function5()


# In[27]:

# �з���ֵ�ĺ���
def add(a,b):
    c = a + b
    return c


# In[28]:

d = add(23,45)
print(d)


# In[ ]:




# In[ ]:



