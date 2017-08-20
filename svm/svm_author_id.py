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
clf = SVC(kernel='linear')

#this is faster but inaccurate
#from sklearn.svm import LinearSVC
#clf=LinearSVC()

# train a smaller data set
features_train = features_train[:len(features_train)//100] 
labels_train = labels_train[:len(labels_train)//100] 

t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t0 = time()
pred=clf.predict(features_test)
print("prediction time:", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,pred)
print("accuracy:",accuracy , "%")

#########################################################