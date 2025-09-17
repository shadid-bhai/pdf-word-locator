import pymupdf as flitz
import re
import json
import random

def word_finder(json_path, keywords):
    """A function that generates random words from json file to add to keywords list"""
    with open(json_path) as json_file:
        data = json.load(json_file)
        rand = random.randint(0, len(data)-1)
        for index, data in enumerate(data):
            if index == rand:
                keywords.append(data)

def extract_word_from_pdf(pdf_path, keywords):
    """A function that extracts the word from the pdf file"""
    found_keywords = {keyword: [] for keyword in keywords}

    with flitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc):
            text = page.get_text()
            for keyword in keywords:
                if re.search(rf"\b{re.escape(keyword)}\b", text, re.IGNORECASE):
                    found_keywords[keyword].append(page_num+1)
    return found_keywords


keywords = []
json_path = r"dictionary"
pdf_path = r"book"
word_finder(json_path, keywords)
print(keywords)
answer = extract_word_from_pdf(pdf_path, keywords)
print(answer)









