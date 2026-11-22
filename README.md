# 🔍 Random Word Finder

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/Library-PyMuPDF-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A lightweight Python utility that randomly samples vocabulary from a JSON dictionary and scans any PDF document to locate the exact page numbers where those words appear in context.

Useful for **language learners**, **vocabulary builders**, and **text researchers** looking to study how specific words are used inside books, papers, or manuals.

---

## ✨ Features

* **Random Vocabulary Sampling:** Pulls one or multiple unique words from any JSON list or key-value dictionary.
* **Exact Whole-Word Matching:** Uses boundary-aware regular expressions (`\b...\b`) so searching for `"art"` won't falsely match `"start"` or `"part"`.
* **Case-Insensitive Search:** Catches occurrences regardless of capitalization (`"Epistemology"`, `"epistemology"`, `"EPISTEMOLOGY"`).
* **Fast PDF Parsing:** Powered by `PyMuPDF` (`fitz`) for rapid text extraction across multi-hundred-page PDFs.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/shadid-bhai/Random-Word-Finder.git](https://github.com/shadid-bhai/Random-Word-Finder.git)
cd Random-Word-Finder
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

1. Prepare a JSON file containing a list of words (or a dictionary object where keys are words):
   ```json
   ["serendipity", "ephemeral", "ubiquitous", "pragmatic", "eloquent"]
   ```
2. Update `JSON_PATH` and `PDF_PATH` in `main.py` to point to your files.
3. Run the script:
   ```bash
   python main.py
   ```

### Example Output
```text
Selected Keywords: ['ubiquitous', 'pragmatic', 'ephemeral']
Page Occurrences:  {'ubiquitous': [14, 89, 204], 'pragmatic': [42], 'ephemeral': []}
```

---

## 🛠️ How It Works

1. **`get_random_words(json_path, count)`** loads the JSON dataset and selects `count` unique entries using `random.sample()`.
2. **`extract_word_from_pdf(pdf_path, keywords)`** iterates through each page of the PDF, runs pre-compiled case-insensitive regex patterns, and maps each keyword to a list of 1-indexed page numbers.

---

## 🌱 Future Ideas

* [ ] Add CLI arguments (`argparse`) so users can pass `--pdf`, `--dict`, and `--count` directly from the terminal.
* [ ] Print the surrounding sentence snippet alongside the page number for immediate reading context.
* [ ] Export results to CSV or Markdown study notes.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
