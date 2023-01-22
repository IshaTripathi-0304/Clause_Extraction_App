import os
import os
import sys
import cv2 
import pandas as pd
import pytesseract 
from PIL import Image 
from sys import platform
from pdf2image import convert_from_path 
from joblib import dump, load

sys.path.append(os.path.abspath(r".."))
from ml.text_process import clean_text

model_folder = r"../ml/models/"
clf = load(os.path.join(model_folder,'clause_clf.joblib'))
tfidf_vectorizer = load(os.path.join(model_folder,'tfidf_vectorizer.joblib'))

pdf_folder_path = r"."

if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    poppler_path = r"C:\Users\07237X744\Downloads\poppler-23.01.0\Library\bin"

all_pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]
#print(all_pdf_files)

results_df = pd.DataFrame(columns = ['file', 'page', 'clause'])

for pdf_file in all_pdf_files:
    pdf_file_path = os.path.join(pdf_folder_path, pdf_file)
    pages = convert_from_path(pdf_file_path, dpi=500, poppler_path = poppler_path)
    pdf_pages_text = []
    for page in pages:
        #ocr_config = r'--oem 3 --psm 6'
        #pytesseract.image_to_string(page, config=ocr_config)
        text = str(pytesseract.image_to_string(page))
        #text = text.replace('-\n', '')
        pdf_pages_text.append(text)
    
    text_series = clean_text(pdf_pages_text)
    x = tfidf_vectorizer.transform(text_series)
    clause_pred = clf.predict(x)
    print(clause_pred)
    for i, c in enumerate(clause_pred):
        results_df.loc[len(results_df.index)] = [pdf_file, i+1, c] 

print(results_df)    
results_df.to_csv("results.csv",index=False)