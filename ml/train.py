import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import base64
import string
import re
from collections import Counter
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
import spacy
import pickle
from joblib import dump, load
from text_process import clean_text

#df = pd.read_csv(r'..\data\train.csv', encoding = "utf-8")
#df = pd.read_csv(r'..\data\train.csv', encoding = "ISO-8859-1")
df = pd.read_csv(r'train.csv', engine='python')

#print(df.head())
#print(df.shape)
train, test = train_test_split(df, test_size=0.33, random_state=42)
#print(train.index)
#print(test.index)
print(train.head())

'''
fig = plt.figure(figsize=(8,4))
sns.barplot(x = train['Clause'].unique(), y=train['Clause'].value_counts())
plt.show()
'''

train["Text"] = clean_text(train["Text"]).values
print(train["Text"].head())

tfidf_vectorizer = TfidfVectorizer()
X_train = tfidf_vectorizer.fit_transform(train["Text"])
Y_train = train["Clause"]

#print(X_train,Y_train)
#print(X_train.shape,Y_train.shape)
#print(tfidf_vectorizer.get_feature_names_out())

X_test = tfidf_vectorizer.transform(test["Text"])
Y_test = test["Clause"]

#print(X_test.shape,Y_test.shape)

from sklearn.linear_model import SGDClassifier

clf = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42,max_iter=5, tol=None)

clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

#print(Y_pred, Y_test)

#cm = confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])
cm = confusion_matrix(Y_test, Y_pred, labels=["contract", 'legistration', 'health', 'mech'])
print("confusion_matrix:")
print(cm)

print("Classifier Accuracy report")
print(classification_report(Y_test, Y_pred, target_names=["contract", 'legistration', 'health', 'mech']))

dump(clf, 'models/clause_clf.joblib') 
#clf = load('clause_clf.joblib')

dump(tfidf_vectorizer, 'models/tfidf_vectorizer.joblib') 
#tfidf_vectorizer = load('tfidf_vectorizer.joblib')