
# Mon-English Instruction Dataset Project 

This repository contains the source code and methodology for compiling a high-quality Mon-English Instruction Dataset. The pipeline automatically processes raw bilingual dictionary files (CSV format) and converts them into a structured dataset (JSON format) optimized for training and fine-tuning Large Language Models (LLMs).

---

## 🌟 Key Features

* **Diverse Prompt Engineering:** Utilizes a randomized pool of instruction templates to ensure the AI model learns from varying contexts and conversational phrasings.

---

## 📂 Project Structure

```text
Mon_AI_Project/
├── README.md                          # Project documentation and overview
├── make_json.py                       # Python script to compile and structure raw CSVs into JSON
├── mon_eng_instruction_dataset.json   # The generated JSON instruction dataset for LLM training
└── [CSV Source Files]                 # Raw input dictionary files (A_list.csv, B_list.csv, etc.)
