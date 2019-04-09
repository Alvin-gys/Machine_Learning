
# coding: utf-8

# In[1]:

import tensorflow as tf


# In[2]:

#Fetch：可以在session中同时计算多个op
#定义三个常量
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
#定义一个加法op
add = tf.add(input2,input3)
#定义一个乘法op
mul = tf.multiply(input1,add)

with tf.Session() as sess:
    #同时执行乘法op和加法op
    result = sess.run([mul,add])
    print(result)


# In[3]:

#Feed：先定义占位符，等需要的时候再传入数据
#创建占位符
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
#定义乘法op
output = tf.multiply(input1,input2)

with tf.Session() as sess:
    #feed的数据以字典的形式传入
    print(sess.run(output,feed_dict={input1:[8.],input2:[2.]}))


# In[ ]:



