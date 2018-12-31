import sys
import numpy as np
import argparse
from sklearn import preprocessing
import pandas
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import scipy.cluster.hierarchy as hier

def cluster_accuracy(user_ids, distinct_users, clusters):
  
    nclusters = np.max(clusters)+1;
    
    dict_val = np.zeros(shape=(distinct_users.size), dtype=int);
    for i in range(distinct_users.size):
        dict_val[i] = i;
    
    cluster_labels = np.zeros(shape=(distinct_users.size,nclusters), dtype=int);
    mydict = dict(zip(distinct_users,dict_val));
    
    for i in range(clusters.size):
        cluster_labels[mydict[user_ids[i]]][clusters[i]] += 1;
    
    cluster_accuracy = [];
    weight = [];
    
    for i in range(1,nclusters):
        max_asg = max(cluster_labels[:,i]);
        total = sum(cluster_labels[:,i]);
        cluster_accuracy.append(max_asg/float(total));
        weight.append(total/float(clusters.size));
        
    w_avg= np.average(np.asarray(cluster_accuracy),weights = np.asarray(weight));
    avg= np.mean(cluster_accuracy);
    return (round(avg,5), round(w_avg,5));
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('seqfile', help='Input Sequence File')
    parser.add_argument('start_dim', help='Initial index of feature dimensions', type=int)
    parser.add_argument('end_dim', help='Final index of feature dimensions', type=int)
    args = parser.parse_args()
     
    user_ids = np.loadtxt(args.seqfile, delimiter=',', dtype=float, usecols=range(0,1));
    df = np.loadtxt(args.seqfile, delimiter=',', dtype=float, usecols=range(args.start_dim,args.end_dim));
    
    
    user_ids = user_ids.astype(int);
    distinct_users = np.unique(user_ids);
    
    Z = hier.linkage(df,'average');
    #np.savetxt('linkage_transform.csv', Z, fmt="%f", delimiter=',');
    
    clusters = np.empty(shape=(df.shape[0], 100), dtype=int);
    j=0;
    old_max = df.shape[0];
    n_cluster = [];
    purity = [];
    w_purity = [];
    
    for i in range(100):
      maxd = float(i)/25;
      
      clusters[:,j] = hier.fcluster(Z,maxd,criterion='distance');
      if np.max(clusters[:,j])==1:
        break;
      (avg,w_avg) = cluster_accuracy(user_ids,distinct_users,clusters[:,j]);
      
      if (np.max(clusters[:,j])<old_max):
        old_max = np.max(clusters[:,j]);
        n_cluster.append(np.max(clusters[:,j]));
        purity.append(avg);
        w_purity.append(w_avg);
        
      j+=1;
      
    clusters = clusters[:,:j];
    #np.savetxt('cluster_output.csv',clusters,fmt="%d",delimiter=',');
    print(n_cluster[::-1]);
    print(purity[::-1]);
    print(w_purity[::-1]);
    
    return (0)


if __name__ == "__main__":
    main()
