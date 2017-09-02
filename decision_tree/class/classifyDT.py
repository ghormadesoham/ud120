def classify(features_train, labels_train):
### your code goes here--should return a trained decision tree classifer
 from sklearn import tree
 clf = tree.DecisionTreeClassifier(min_samples_split = 50)
 clf = clf.fit(features_train, labels_train)   
 return clf
#Notes
#min_samples_split parameter
#The minimum number of samples required to split an internal node
#increase the default value of 2 to 50 so see the jagged boundary of the decision surface become uniform

