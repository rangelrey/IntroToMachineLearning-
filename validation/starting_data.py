#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/python

""" 
PLEASE NOTE:
The api of train_test_split changed and moved from sklearn.cross_validation to
sklearn.model_selection(version update from 0.17 to 0.18)

The correct documentation for this quiz is here: 
http://scikit-learn.org/0.17/modules/cross_validation.html
"""

from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
features = iris.data
labels = iris.target

#X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

### import the relevant code and make your train/test split
### name the output datasets features_train, features_test,
### labels_train, and labels_test
from sklearn.model_selection import train_test_split


### set the random_state to 0 and the test_size to 0.4 so
### we can exactly check your result
features_train, features_test, labels_train, labels_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0 )

###############################################################
# DONT CHANGE ANYTHING HERE
clf = SVC(kernel="linear", C=1.)
clf.fit(features_train, labels_train)

print clf.score(features_test, labels_test)
##############################################################
def submitAcc():
    return clf.score(features_test, labels_test)


# In[ ]:




