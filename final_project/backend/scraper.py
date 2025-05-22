# scraper.py
import sys
import json
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from itertools import chain
import requests

def get_candidate_phrases(words):
    return list(chain(
        words,
        [' '.join(words[i:i+2]) for i in range(len(words)-1)],
        [' '.join(words[i:i+3]) for i in range(len(words)-2)]
    ))

def clean_text(text):
    return re.findall(r'\b\w+\b', text.lower())

def scrape_investopedia_definition(term):
    slug = term.replace(" ", "")
    url = f"https://www.investopedia.com/terms/{slug[0]}/{slug}.asp"

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        # Long-form
        full_def = soup.find("p", id="mntl-sc-block_2-0")
        if full_def:
            return {
                "term": term,
                "definition": full_def.get_text(strip=True),
                "url": url
            }
        # Short-form
        short_def = soup.find("div", id="short-definition__text_1-0")
        if short_def:
            return {
                "term": term,
                "definition": short_def.get_text(strip=True),
                "url": url
            }

    except requests.exceptions.RequestException:
        return None

    return None

def extract_defined_terms_from_paragraph(paragraph, max_terms=100):
    words = clean_text(paragraph)[:max_terms]
    candidates = get_candidate_phrases(words)
    unique_candidates = sorted(set(candidates), key=lambda x: -len(x))  # longest phrases first

    found_terms = []
    checked = set()

    for term in unique_candidates:
        if term in checked:
            continue
        checked.add(term)
        result = scrape_investopedia_definition(term)
        if result and result['definition']:
            found_terms.append(result)

    return found_terms

def main(paragraph_file: str, output_file: str):
    with open(paragraph_file, 'r') as f:
        paragraph = f.read()

    print("Extracting definitions from paragraph...")
    results = extract_defined_terms_from_paragraph(paragraph)

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Found {len(results)} terms with definitions.")
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scraper.py <input_paragraph.txt> <output_definitions.json>")
    else:
        main(sys.argv[1], sys.argv[2])
