import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.neighbors import KNeighborsClassifier #KNN 클래스 불러옴
from sklearn.model_selection import KFold #교차 검증을 위한 kFlod 불러옴
from sklearn.pipeline import Pipeline #정규화를 위한 라이브러리
from sklearn.preprocessing import StandardScaler #정규화를 위한 라이브러리2

data=pd.read_csv("C:\\Users\\Seomyungwon\\Desktop\\Python_Test\\zoo.csv", encoding='CP949')

clf = KNeighborsClassifier(n_neighbors=3) #k가 3인 k-NN 분류기(클래스)를 생성
clf = Pipeline([('norm',StandardScaler()), ('knn',clf)]) #정규화 작업 진행

kf = KFold(n_splits=5) #데이터에 대한 x-validation 진행할 때 x값 setting
#print(kf)

features=data.ix[:, :17] #zoo.csv에서 label 제외한 데이터 추출
labels=data['class_type']

#print(features)
#print(label)

means = []

for train, test in kf: #K번 train, test 만들 때 알아서 하나만 test data로 저장
    clf.fit(features.ix[train,], labels.ix[train,]) #k-NN 분류기에 train 데이터와 라벨 넣음
    prediction = clf.predict(features.ix[test,]) # test 데이터를 넣고 예상값을 뽑아냄

    curmean = np.mean(prediction == labels.ix[test,]) #예상값이 맞은 것에 대해서 평균을 내줌
    print(curmean) #정확도 확인
    means.append(curmean) #means 리스트에 추가

print("accuracy : {:.1%}".format(np.mean(means)))
