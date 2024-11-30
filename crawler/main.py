import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from keybert import KeyBERT

# Initialize the KeyBERT model
kw_model = KeyBERT()

def simple_crawler_with_keywords(start_url, max_pages=10, top_n=5):
    visited = set()
    to_visit = [start_url]
    page_count = 0

    while to_visit and page_count < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
        
        try:
            # Fetch the page content
            response = requests.get(url)
            response.raise_for_status()
            print(f"Crawling: {url}")
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            continue

        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        visited.add(url)
        page_count += 1

        # Extract text content from the page
        text = soup.get_text(separator=' ', strip=True)

        # Extract keywords using KeyBERT
        keywords = kw_model.extract_keywords(
            text, 
            keyphrase_ngram_range=(1, 2), 
            stop_words='english', 
            top_n=top_n
        )

        # Print the extracted keywords
        print(f"Top Keywords for {url}:")
        for keyword, score in keywords:
            print(f"- {keyword} (Score: {score:.4f})")
        print("\n" + "-" * 50 + "\n")

        # Find all links on the page and add them to the queue
        for link in soup.find_all('a', href=True):
            full_url = urljoin(url, link['href'])
            if full_url not in visited:
                to_visit.append(full_url)

    print("Crawling complete.")

# Usage example
simple_crawler_with_keywords('https://attack.mitre.org/', max_pages=5, top_n=5)
