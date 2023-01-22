import os
import pandas as pd
from pathlib import Path

ocr_out_folder = r"../ocr/train/"
page_delimiter = "\n----$$$$----$$$$----\n"

all_files = [f for f in os.listdir(ocr_out_folder) if f.endswith(".txt")]

#print(all_files)
train_df = pd.DataFrame(columns = ["pdf", "page", 'Text', 'Clause'])

for file in all_files:
    txt = Path(os.path.join(ocr_out_folder,file)).read_text()
    pages = txt.split(page_delimiter)[:-1]
    #temp_df = pd.DataFrame(columns = ["pdf", "page", 'Text', 'Clause'])
    temp_df = train_df.iloc[:0]
    temp_df['Text'] = pages
    temp_df['Clause'] = file.split("_")[0]
    temp_df["pdf"] = file
    temp_df['page'] = list(range(1, temp_df.shape[0]+1))
    train_df = pd.concat([train_df, temp_df], ignore_index=True)
    print(file, len(pages), temp_df.shape, train_df.shape)

train_df.to_csv("train.csv",index=False)    