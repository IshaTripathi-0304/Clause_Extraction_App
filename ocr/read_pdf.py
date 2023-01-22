import os
import sys
import cv2 
import shutil
import pytesseract 
from PIL import Image 
from sys import platform
from pdf2image import convert_from_path 

pdf_folder_path = r"..\data\train"
page_delimiter = "\n----$$$$----$$$$----\n"

if os.path.exists('train'):
    shutil.rmtree('train')
os.makedirs('train')

if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    poppler_path = r"C:\Users\07237X744\Downloads\poppler-23.01.0\Library\bin"

all_pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]
#print(all_pdf_files)
for pdf_file in all_pdf_files:
    print(pdf_file)
    pdf_file_path = os.path.join(pdf_folder_path, pdf_file)
    pages = convert_from_path(pdf_file_path, dpi=500, poppler_path = poppler_path)
    out_file_path = os.path.join("train", pdf_file.replace(".pdf",".txt"))
    f = open(out_file_path, "w")
    for page in pages:
        #ocr_config = r'--oem 3 --psm 6'
        #pytesseract.image_to_string(page, config=ocr_config)
        text = str(pytesseract.image_to_string(page))
        #text = text.replace('-\n', '')
        text = text + page_delimiter
        f.write(text)
    f.close()