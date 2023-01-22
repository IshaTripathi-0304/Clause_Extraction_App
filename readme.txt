This is a basic AI application for extracting clauses/ classes from the pdf at the page level. This Project contains 5 Sub-applications/ folders where I have implemented the entire applications into sub-modules.

Key Technologies I learnt while implementing below solutions:
- Web App Development: HTML, CSS, JavaScript & Django
- ML Model Development: Spacy & Scikit-learn
- OCR: Tessract-OCR


- data
  Contains raw pdf files downloaded from public sources. 
  This folder also contains the code to divide the pdfs into train & test folders for Model training & finally for playing/ testing the built solution

- ocr
  Contains the code to ocr/extract the text (training files in data folder) from the pdf files

- ml
  Contains the code
  1. to generate the training data (csv format at page level) from the text files created from OCR process.
  2. to train the ML classification model for detecting one of the 4 types [contract, legistration, public_health, mech_eng.

- new_file
  Contains the code to make classification prediction on each page of a pdf present in this folder

- web-app
  Contains a basic Django web-application of two pages [upload file, view uploaded files]


I Plan to learn Cloud Application Development soon, so that all the 5 solutions can be deployed on cloud. By deploying this solution on cloud, the application will be available to anyone on internet & these sub-modules can interact with themselves automatically
