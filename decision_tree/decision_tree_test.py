#!/usr/bin/env python
# coding: utf-8

# In[37]:


#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import math
from sklearn import tree
from sklearn.metrics import accuracy_score




### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train_transformed, features_test_transformed, labels_train, labels_test = preprocess()

min_samples_split =40


clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print accuracy_score(pred, labels_test)


# In[42]:


print "Esta es la cantidad de features que hay en el train -"
len(features_train_transformed[0])


# In[ ]:




