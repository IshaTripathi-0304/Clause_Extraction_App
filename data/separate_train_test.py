import os
import shutil
from sklearn.model_selection import train_test_split

train_dir = 'train'
test_dir = 'test'
raw_pdf_folder = r"all_raw_pdf_files"
#raw_pdf_folder = r"."

test_data_ratio = 0.15

def create_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)

create_dir(train_dir)
create_dir(test_dir)

all_folders = [name for name in os.listdir(raw_pdf_folder) if os.path.isdir(os.path.join(raw_pdf_folder,name))]
print(all_folders)

for folder in all_folders:
    folder_path = os.path.join(raw_pdf_folder,folder)
    all_pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    
    train_pdfs, test_pdfs = train_test_split(all_pdf_files, test_size=test_data_ratio, random_state=42)
    
    print(len(all_pdf_files), len(train_pdfs), len(test_pdfs))
    
    for file in train_pdfs:
        dest_fname = folder + "_" + file[:20] + ".pdf"
        shutil.copyfile(os.path.join(folder_path,file), os.path.join(train_dir, dest_fname))
    for file in test_pdfs:
        dest_fname = folder + "_" + file[:20] + ".pdf"
        shutil.copyfile(os.path.join(folder_path,file), os.path.join(test_dir, dest_fname))