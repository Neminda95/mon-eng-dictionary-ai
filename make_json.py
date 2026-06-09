import csv
import json
import random

# ၁. ပြေင်စဳဇာတ် မလိက်သၟာန် (Instructions) နာနာသာ်
instruction_templates = [
    "Translate the following English term to Mon and provide its definition.",
    "What is the Mon translation and dictionary definition for this English word?",
    "Convert this English phrase into Mon and explain its meaning.",
    "Give the Mon meaning and definition for the following English word.",
    "Translate this English word into Mon."
]

# ပြဟ်ဏံ စေတ်ရံင်ယၟုဖိုင် CSV မၞး ညံင်ဂွံတူကဵု ယၟုဖိုင်သၟဝ်ဏံညိ
csv_filename = "mon_eng_dictionary_combined_excel_ready.csv"
json_filename = "mon_eng_instruction_dataset.json"

dataset = []

# ၂. ဗှ်ဒေတာနူဖိုင် CSV နကဵုလၟေင်ကော်လံ (Index)
with open(csv_filename, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    
    for row in reader:
        # ယဝ်ရတန်းဂှ် လိက်ဟွံမွဲ သာ်ဟွံသေင် နွံအောန်နူ ၂ ကော်လံမ္ဂး ကဵုဍေဟ်ကျော်အာ
        if len(row) < 2:
            continue
            
        english_word = row[0].strip()
        mon_definition = row[1].strip()
        
        # ယဝ်ရဒှ်တန်း ခေါင်းစဉ် (Header) "English, Mon" မ္ဂး ကဵုဍေဟ်ကျော်ထောံညိ
        if "english" in english_word.lower() or "mon" in mon_definition.lower():
            continue
            
        if not english_word or not mon_definition:
            continue
            
        # ရုဲစှ်ေ မလိက်သၟာန် နကဵုအစဳအဇန် Random
        chosen_instruction = random.choice(instruction_templates)
        
        # ပြေင်ဗီုပြင် Instruction-Prompt Dataset (JSON)
        data_entry = {
            "instruction": chosen_instruction,
            "input": english_word,
            "output": mon_definition
        }
        dataset.append(data_entry)

# ၃. သိမ်းဆည်းထောံ နကဵုဖိုင် JSON
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"Successfully created JSON dataset with {len(dataset)} examples!")
print(f"Saved as: {json_filename}")