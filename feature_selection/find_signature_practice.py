#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))

word_data2 = list()
for i in word_data:
	if "sshacklensf" in i: # second one is "cgermannsf"
		i = i.replace("sshacklensf", "")
	if "cgermannsf" in i:
		i = i.replace("cgermannsf", "")
	if "houectect" in i:
		i = i.replace("houectect", "")
	if "houect" in i:
		i = i.replace("houect", "")
	word_data2.append(i)

authors = pickle.load( open(authors_file, "r") )

### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data2, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]





# In[2]:


from sklearn import tree 
from sklearn.metrics import accuracy_score 
#We assign the model to a variable
clf = tree.DecisionTreeClassifier() 
#We fit the input and output variables (train)
clf = clf.fit(features_train, labels_train)
#with the new coefficients we can predict the output test data
pred = clf.predict(features_test)
#we print the accuracy between the predictions and the test labels
print accuracy_score(labels_test, pred)


# In[3]:


#The importance feature with the highest importance is:
print max(clf.feature_importances_)
featureImportances =clf.feature_importances_
numpy.where(featureImportances == 0.875)

count = 0
for f in featureImportances:
	if(f > 0.2):
		print "f: ", f, "  index: ", count
		break
	count += 1
print vectorizer.get_feature_names()[count]


# In[ ]:




