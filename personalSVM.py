from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import numpy as np
import pandas

Trainxdf = np.loadtxt("TrainFinalX.csv", delimiter=',', skiprows=1, dtype=float);
Trainydf = np.loadtxt("TrainFinalY.csv", delimiter=',', skiprows=1, dtype=float);

Testxdf = np.loadtxt("TestFinalX.csv", delimiter=',', dtype=float);
#Testydf = np.loadtxt("1503960366ytest.csv", delimiter=',', dtype=float);
#print(df.shape);
#print(df[0]); 

#min_max_scaler = preprocessing.MinMaxScaler();
#x_scaled = min_max_scaler.fit_transform(df);
#x = pandas.DataFrame(x_scaled);
#x_scaled_training = x[0:450];
#x_scaled_test = x[450:457];

#Train_scaled = min_max_scaler.fit_transform(Trainxdf);
#Training = pandas.DataFrame(Train_scaled);

#Test_scaled = min_max_scaler.fit_transform(Testxdf);
#Testing = pandas.DataFrame(Test_scaled);


#print(Test_scaled);
#print(Testing);
print(1)
clf = SVC(kernel='linear')
print(2)
clf.fit(Trainxdf, Trainydf)
print(3)
Y_predTest = clf.predict(Testxdf);
print(4)
print(Y_predTest);



