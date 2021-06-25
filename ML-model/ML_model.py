import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import svm
from sklearn import metrics
import pickle

features_df = pd.read_csv('traffic_features.csv', sep=',', engine ='python')
y = features_df.pop('is_Attack')
# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(features_df, y, test_size=0.3)

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # RBF Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))
print("Confusion Matrix\n" ,confusion_matrix(y_test,y_pred))
print("\nClassification report\n\n",classification_report(y_test,y_pred))

# Save the classifier for real time prediction
pickle.dump(clf, open(r"trainedClassifier.pkl", 'wb'), protocol=2)
