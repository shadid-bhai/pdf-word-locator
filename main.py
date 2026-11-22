import json
import random
import re
import fitz  # PyMuPDF


def get_random_words(json_path: str, count: int = 1) -> list[str]:
    """Selects `count` unique random words from a JSON dictionary file."""
    with open(json_path, encoding="utf-8") as json_file:
        data = json.load(json_file)

    words = list(data.keys()) if isinstance(data, dict) else list(data)
    sample_size = min(count, len(words))
    return random.sample(words, sample_size)


def extract_word_from_pdf(pdf_path: str, keywords: list[str]) -> dict[str, list[int]]:
    """Searches a PDF and returns 1-indexed page numbers where each keyword appears."""
    found_keywords = {keyword: [] for keyword in keywords}

    # Pre-compile regex patterns for faster page-by-page scanning
    patterns = {
        keyword: re.compile(rf"\b{re.escape(keyword)}\b", re.IGNORECASE)
        for keyword in keywords
    }

    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            for keyword, pattern in patterns.items():
                if pattern.search(text):
                    found_keywords[keyword].append(page_num)

    return found_keywords


if __name__ == "__main__":
    JSON_PATH = "dictionary.json"
    PDF_PATH = "book.pdf"

    keywords = get_random_words(JSON_PATH, count=5)
    print(f"Selected Keywords: {keywords}")

    results = extract_word_from_pdf(PDF_PATH, keywords)
    print(f"Page Occurrences:  {results}")








