# ����numpy��ѧ�����
import numpy as np
# ���뻭ͼ���߰�
import matplotlib.pyplot as plt
# ������д�������ݼ�
from sklearn.datasets import load_digits
# ���ڱ�ǩ��ֵ�������ѱ�ǩת�ɶ��ȱ���one-hot�ĸ�ʽ
# 0~9 
# 0->1000000000
# 1->0100000000
# 9->0000000001
from sklearn.preprocessing import LabelBinarizer
# ���ڰ����ݼ����Ϊѵ�����Ͳ��Լ�
from sklearn.model_selection import train_test_split
# ��������������
from sklearn.metrics import classification_report,confusion_matrix

# ����sigmoid����
def sigmoid(x):
    return 1/(1+np.exp(-x))

# ����sigmoid�����ĵ���
def dsigmoid(x):
    return x*(1-x)

# ������������
class NeuralNetwork:
    # ��ʼ�����磬��������ṹ
    # ���贫��(64,100,10)��˵�����壺
    # �����64����Ԫ�����ز�100����Ԫ�������10����Ԫ
    def __init__(self,layers):
        # Ȩֵ�ĳ�ʼ������Χ-1��1
        # �����ҿ���˼��һ��Ȩֵ��������ȡֵ��Χ�ܲ���ȡ0-1��Ϊʲô��
        self.W1 = np.random.random([layers[0],layers[1]])*2-1
        self.W2 = np.random.random([layers[1],layers[2]])*2-1
        # ��ʼ��ƫ��ֵ
        self.b1 = np.zeros([layers[1]])
        self.b2 = np.zeros([layers[2]])
        # �����list���ڱ���list
        self.loss = []
        # �����list���ڱ���
        self.accuracy = []

    # ѵ��ģ��
    # XΪ��������
    # TΪ���ݶ�Ӧ�ı�ǩ
    # lrѧϰ��
    # stepsѵ������
    # batch���δ�С
    # ʹ����������ݶ��½�����ÿ�������ȡһ�����ε����ݽ���ѵ��
    def train(self,X,T,lr=0.5,steps=20000,test=5000,batch=50):
        # ����steps+1��ѵ��
        for n in range(steps+1):
            # ���ѡȡһ����������
            index = np.random.randint(0,X.shape[0],batch) 
            x = X[index]
            # �������ز����
            L1 = sigmoid(np.dot(x,self.W1)+self.b1)
            # ������������
            L2 = sigmoid(np.dot(L1,self.W2)+self.b2)
            # ��������ѧϰ�ź�
            delta_L2 = (T[index]-L2)*dsigmoid(L2)
            # �����ز��ѧϰ�ź�
            delta_L1= delta_L2.dot(self.W2.T)*dsigmoid(L1)
            # �����ز㵽������Ȩֵ�ı�
            # ����һ�μ����˶��������������Ҫ��ƽ��
            self.W2 += lr * L1.T.dot(delta_L2) / X.shape[0]
            # ������㵽���ز��Ȩֵ�ı�
            # ����һ�μ����˶��������������Ҫ��ƽ��
            self.W1 += lr * x.T.dot(delta_L1) / X.shape[0]
             # �ı�ƫ��ֵ
            self.b2 = self.b2 + lr * np.mean(delta_L2, axis=0)
            self.b1 = self.b1 + lr * np.mean(delta_L1, axis=0)
            
            # ÿѵ��5000��Ԥ��һ��׼ȷ��
            if n%test==0:
                # Ԥ����Լ���Ԥ����
                Y2 = self.predict(X_test)
                # ȡ��Ԥ�����������ڵ�����
                # �������ֵ���ڵ�������3����ôԤ��������3
                predictions = np.argmax(Y2,axis=1)
                # ����׼ȷ��
                # np.equal(predictions,y_test)�ж�Ԥ��������ʵ��ǩ�Ƿ���ȣ���ȷ���True������ȷ���False
                # np.equal(predictions,y_test)ִ�к�õ�һ���������True��False���б�
                # Ȼ����np.mean���б���ƽ��TrueΪ1��FalseΪ0��
                # ����һ����10�������9��True��һ��False��ƽ����Ľ��Ϊ0.9����Ԥ���׼ȷ��Ϊ90%
                acc = np.mean(np.equal(predictions,y_test))
                # ����loss
                l = np.mean(np.square(y_test - predictions) / 2)
                # ����׼ȷ��
                self.accuracy.append(acc)
                # ����lossֵ
                self.loss.append(l)
                # ��ӡѵ������,׼ȷ�ʺ�loss
                print('steps:%d accuracy:%.3f loss:%.3f' % (n,acc,l))

    # ģ��Ԥ����
    def predict(self,x):
        L1 = sigmoid(np.dot(x,self.W1)+self.b1)#�������
        L2 = sigmoid(np.dot(L1,self.W2)+self.b2)#��������
        return L2

# ��������￪ʼ����
# ����ѵ������
steps = 50001
# �������������
test = 5000
# ��������
digits = load_digits()
# �õ�����
X = digits.data
# �õ���ǩ
y = digits.target
# �������ݹ�һ���������ڼӿ�ѵ���ٶ�
# X��ԭ������ֵ��Χ��0-255֮�䣬��һ������0-1֮��
X -= X.min()
X /= X.max() - X.min()
# �ָ�����1/4Ϊ�������ݣ�3/4Ϊѵ������
# ��1347��ѵ�����ݣ�450����������
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25) 

# ��������,�����64����Ԫ�����ز�100����Ԫ�������10����Ԫ
nm = NeuralNetwork([64,100,10])
# ��ǩת��Ϊ���ȱ���one-hot�ĸ�ʽ
labels_train = LabelBinarizer().fit_transform(y_train)

# ��ʼѵ��
print('Start training')
nm.train(X_train,labels_train,steps=steps,test=test)

# Ԥ���������
predictions = nm.predict(X_test) 
# predictions.shapeΪ(450,10)
# y_test.shapeΪ(450,)
# ������Ҫȡ��Ԥ�����������ڵ���������������������Ԥ��Ľ��
# np.argmax(predictions,axis=1)ִ�к�õ�����״Ҳ�����(450,)
predictions = np.argmax(predictions,axis=1)
# �ԱȲ������ݵ���ʵ��ǩ������Ԥ�������õ�׼ȷ�ʣ��ٻ��ʺ�F1ֵ
print(classification_report(y_test,predictions))
# ���ڲ������ݵ���ʵ��ǩ������Ԥ�������õ���������
print(confusion_matrix(y_test,predictions))

# ѵ��������loss�Ĺ�ϵͼ
plt.plot(range(0,steps+1,test),nm.loss)
plt.xlabel('steps')
plt.ylabel('loss')
plt.show()

# ѵ��������accuracy�Ĺ�ϵͼ
plt.plot(range(0,steps+1,test),nm.accuracy)
plt.xlabel('steps')
plt.ylabel('accuracy')
plt.show()


