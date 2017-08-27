#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.
    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#this is slower :-(-it takes around 10 mins
from sklearn.svm import SVC
clf = SVC(kernel='rbf', C = 10000)#rbf or linear

#this is faster but inaccurate
#from sklearn.svm import LinearSVC
#clf=LinearSVC()

# train a smaller data set
#features_train = features_train[:len(features_train)//100] 
#labels_train = labels_train[:len(labels_train)//100] 

t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t0 = time()
pred=clf.predict(features_test)
print("prediction time:", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,pred)
print("accuracy:",accuracy , "%")


print("prediction for 10 th element:",pred[10])
print("prediction for 26 th element",pred[26])
print("prediction for 50 th element",pred[50])

count = 0;
for i in range(0,len(pred)):    # they gave the length in question to 1700 but using in-built function
 if pred[i] == 1:               # 1 for Chris and 0 for Sara 
  count+=1 # Python does not use ++ as syntax for increment operator 

print("Chris's emails :",count)    
#########################################################
