from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#k-NN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np



iris_dataset = load_iris()

print(iris_dataset)

target = iris_dataset['target'] #label

#data split (train / test)
train_input, test_input, train_label, test_label = train_test_split(iris_dataset['data'],
                                                                    target,
                                                                    test_size=0.25, #test set ratio
                                                                    random_state=42) #random seed

# k-NN model
knn = KNeighborsClassifier(n_neighbors = 1)

knn.fit(train_input, train_label) # classification model의 학습 데이터와 label 데이터 적용

predict_label = knn.predict(test_input) # classification model의 결과 예측

print('test accuracy {:.2f}'.format(np.mean(test_label == predict_label))) #정확도 출력 1

print('test accuracy {:.2f}'.format(accuracy_score(test_label, predict_label))) #정확도 출력 2



