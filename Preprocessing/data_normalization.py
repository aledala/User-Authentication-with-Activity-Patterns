import sys
import numpy as np
import argparse
from sklearn import preprocessing
import pandas
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('seqfile', help='Input Sequence File')
    args = parser.parse_args()
     
    df = np.loadtxt(args.seqfile, delimiter=',', dtype=float, usecols=range(1,14));
    #print(df.shape);
    #print(df[0]);   
    min_max_scaler = preprocessing.MinMaxScaler();
    x_scaled = min_max_scaler.fit_transform(df);
    x = pandas.DataFrame(x_scaled);
    x_scaled_training = x[0:450];
    x_scaled_test = x[450:457];
    #print(x);
    #print(x_scaled);
    class_labels = np.zeros(shape=(450), dtype=int);
    class_labels[0:19] = 1;

    #print(class_labels);
    test_labels = np.zeros(shape=(7), dtype=int);
  
    clf = SVC(C=1,kernel='linear')
    clf.fit(x_scaled_training, class_labels)
    #Y_predTest = clf.predict(X_test)
    Y_predTest = clf.predict(x_scaled_test);
    print(accuracy_score(test_labels, Y_predTest));

    '''
    Y_predTrain = clf.predict(X_train)
    Y_predTest = clf.predict(X_test)
    SVMtrainAcc.append(accuracy_score(Y_train, Y_predTrain))
    SVMtestAcc.append(accuracy_score(Y_test, Y_predTest))
    ''' 
    '''   
    ids = set();
    
    with open(args.seqfile) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content];
        for line in content:
            words = [x.strip() for x in line.split(',')]; 
            if (words[0].isdigit()):
                ids.add(int(words[0]));
             
    print(ids);
    '''

    return (0)


if __name__ == "__main__":
    main()
