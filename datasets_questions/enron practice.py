#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))



# In[15]:


a=[]
for k in enron_data:
    if k=="ALLEN PHILLIP K":
        a.append(enron_data[k])
len(a)


# In[17]:


len(a)
b=[]
for i in a:
    for ii in i:
        b.append(ii)
len(b)        


# In[22]:


poi = []
for i in enron_data:
    if enron_data[i]["poi"] is True:
        poi.append(i)


# In[45]:


#Con esto obtendras el contenido del text
f = open("/Users/macbook/Documents/MisDocs/Scripts/ud120-projects/final_project/poi_names.txt","r")
if f.mode =="r":
    contents = f.read()


# In[68]:


yourResult = [line.split(' ') for line in f.readlines()]


# In[83]:


a=[]
for i in contents.split("("):
    if ")" in i:
        a.append(i)
len(a)


# In[84]:


pois = contents.split("(")


# In[86]:


enron_data


# In[91]:


enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]


# In[103]:


enron_data


# In[115]:


enron_data


# In[116]:



a=[]
for i in enron_data: 
    if "@enron.com" in enron_data[i]["email_address"]:
        print("error")
    else:
        a.append(i)
   

len(a)


# In[120]:


import numpy as np

a = np.array([1, 2, 3])


# In[121]:


a


# In[ ]:




