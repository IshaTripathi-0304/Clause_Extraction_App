import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import string
import spacy

stopwords = stopwords.words('english')
nlp = spacy.load('en_core_web_sm')
punctuations = string.punctuation

def clean_text(docs, logging=False):
    texts = []
    counter = 1
    for doc in docs:
        if counter % 10 == 0 and logging:
            print("Processed %d out of %d documents." % (counter, len(docs)))
        counter += 1
        doc = nlp(doc, disable=['parser', 'ner'])
        tokens = [tok.lemma_.lower().strip() for tok in doc if tok.lemma_ != '-PRON-']
        tokens = [tok for tok in tokens if tok not in stopwords and tok not in punctuations]
        tokens = ' '.join(tokens)
        texts.append(tokens)
    return pd.Series(texts)