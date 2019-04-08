
# coding: utf-8

# In[1]:

import tensorflow as tf


# In[2]:

#定义一个变量
x = tf.Variable([1,2])
#定义一个常量
a = tf.constant([3,3])
#增加一个减法op
sub = tf.subtract(x,a)
#增加一个加法op
add = tf.add(x,sub)

#所有变量初始化
init = tf.global_variables_initializer()

with tf.Session() as sess:
    #执行变量初始化
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))


# In[3]:

#创建一个变量初始化为0
state = tf.Variable(0,name='counter')
#创建一个op，作用是使state加1
new_value = tf.add(state,1)
#赋值op
update = tf.assign(state,new_value)
#所有变量初始化
init = tf.global_variables_initializer()

with tf.Session() as sess:
    #执行变量初始化
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))


# In[ ]:



