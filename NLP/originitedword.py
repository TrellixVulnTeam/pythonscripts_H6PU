# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:11:39 2019

@author: User
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize

sentence="Hello Guru99, You have to build a very good site and I love visiting your site."
words=word_tokenize(sentence)
ps=PorterStemmer()
for w in words:
    rootWord=ps.stem(w)
    print(rootWord)