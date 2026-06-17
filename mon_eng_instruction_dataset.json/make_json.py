import csv
import json
import random
import os

instruction_templates = [
    "Translate the following English term to Mon and provide its definition.",
    "What is the Mon translation and dictionary definition for this English word?",
    "Convert this English phrase into Mon and explain its meaning.",
    "Give the Mon meaning and definition for the following English word.",
    "Translate this English word into Mon."
]

csv_filenames = [
    "Mon_English_Master_Dictionary copy.csv",
    "A_list_Eng_Mon.csv",
    "B_list_Eng_Mon.csv",
    "C_list_Eng_Mon.csv",
    "D_list_Eng_Mon.csv",
    "E_list_Eng_Mon.csv",
    "F_list_Eng_Mon.csv",
    "G_list_Eng_Mon.csv",
    "H_list_Eng_Mon.csv",
    "I_list_Eng_Mon.csv",
    "J_list_Eng_Mon.csv",
    "K_list_Eng_Mon.csv",
    "L_list_Eng_Mon.csv",
    "M_list_Eng_Mon.csv",
    "N_list_Eng_Mon.csv",
    "O_list_Eng_Mon.csv",
    "P_list_Eng_Mon.csv",
    "Q_list_Eng_Mon.csv",
    "R_list_Eng_Mon.csv",
    "S_list_Eng_Mon.csv",
    "T_list_Eng_Mon.csv",
    "U_list_Eng_Mon.csv",
    "V_list_Eng_Mon.csv",
    "W_list_Eng_Mon.csv",
    "X_list_Eng_Mon.csv",
    "Y_list_Eng_Mon.csv",
    "Z_list_Eng_Mon.csv"
]

json_filename = "mon_eng_instruction_dataset.json"
dataset = []
seen_pairs = set()

for csv_filename in csv_filenames:
    if not os.path.exists(csv_filename):
        continue
        
    print(f"Processing: {csv_filename} ...")
    
    with open(csv_filename, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        
        for row in reader:
            if len(row) < 2:
                continue
                
            english_word = row[0].strip()
            mon_definition = row[1].strip()
            
            if "english" in english_word.lower() or "mon" in mon_definition.lower() or "word" in english_word.lower():
                continue
                
            if not english_word or not mon_definition:
                continue
            
            pair_identifier = (english_word, mon_definition)
            if pair_identifier in seen_pairs:
                continue
            seen_pairs.add(pair_identifier)
                
            chosen_instruction = random.choice(instruction_templates)
            
            data_entry = {
                "instruction": chosen_instruction,
                "input": english_word,
                "output": mon_definition
            }
            dataset.append(data_entry)

with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully created JSON dataset with {len(dataset)} examples!")
print(f"Saved as: {json_filename}")
