#!/usr/bin/env python
# coding: utf-8

# In[8]:


import nltk
#descargamos todo los documentos (corpus)
nltk.download()

from nltk.corpus import stopwords
sw = stopwords.words("english")


# In[15]:


from nltk.stem.snowball import SnowballStemmer


# In[18]:


#Hay palabras como responsivity, response, responsiveness que realmente son lo mismo
#con stemmer, extraeremos la raiz de la palabra
stemmer = SnowballStemmer("english")

print stemmer.stem("responsiveness")


# In[ ]:




