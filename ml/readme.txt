This module contains:
1. [requirements.txt]: list of Python packages required to run this module
2. [make_train_data.py]: the code to make training data [text, clause] csv
3. [text_process.py]: the code to convert the text data into vector [pandas series]
4. [train.py]: train.csv (made by above code) is used to train a vectorizer & ML classifier model and saves them into model folder
    - I have used a simple SGDClassifier model, but we can select any classifier model available at: https://scikit-learn.org/stable/supervised_learning.html

=================== To run this module ==================
########## Navigate to this folder on CMD using below command:
cd ml
########## Run below command
pip install -r requirements.txt
python -m spacy download en
python -m spacy download en_core_web_sm
>> Python
>>>> import nltk
>>>> nltk.download('stopwords')

python make_train_data.py
python train.py

----------------------------------------------------------
Imp Links referred:
https://spacy.io/usage/spacy-101

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html
