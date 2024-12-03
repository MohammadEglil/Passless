import requests
from bs4 import BeautifulSoup
from keybert import KeyBERT

# Initialize KeyBERT model
kw_model = KeyBERT()

def fetch_items(endpoint_url):
    """
    Fetch items from the API endpoint and return a list of item dictionaries.
    """
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()
        data = response.json()
        
        # Return the list of items (with links and IDs)
        items = data.get('items', [])
        print(f"Fetched {len(items)} items from the endpoint.")
        return items
    except requests.RequestException as e:
        print(f"Failed to fetch data from the endpoint: {e}")
        return []

def extract_keywords_from_page(url, top_n=5):
    """
    Extract keywords from a webpage using KeyBERT.
    """
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()

        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        # Extract keywords
        keywords = kw_model.extract_keywords(
            text, 
            keyphrase_ngram_range=(1, 2), 
            stop_words='english', 
            top_n=top_n
        )
        return [keyword for keyword, score in keywords]  # Return only keywords, not scores
    except requests.RequestException as e:
        print(f"Failed to fetch or process {url}: {e}")
        return []

def update_keywords(endpoint_url, item_id, keywords):
    """
    Update the keywords for an item by making a PUT request.
    """
    put_url = f"{endpoint_url}/{item_id}"  # Adjust the URL to match the PUT endpoint
    try:
        # Send a PUT request with the `Keywords` as a list
        response = requests.put(
            put_url,
            json={"Keywords": keywords},  # Directly pass the list of keywords
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            print(f"Successfully updated keywords for item ID {item_id}.")
        else:
            print(f"Failed to update keywords for item ID {item_id}. Response: {response.text}")
    except requests.RequestException as e:
        print(f"Failed to update keywords for item ID {item_id}: {e}")

        
def main():
    endpoint_url = "http://4.226.1.49/items"
    
    # Fetch items from the endpoint
    items = fetch_items(endpoint_url)
    
    if not items:
        print("No items to process.")
        return

    # Crawl each item's link and extract keywords, then update the item
    for item in items:
        item_id = item.get('id')  # Extract the ID of the item
        link = item.get('link')  # Extract the link of the item
        
        if not item_id or not link:
            print(f"Skipping item due to missing ID or link: {item}")
            continue

        print(f"Crawling: {link}")
        keywords = extract_keywords_from_page(link)
        
        # Update the keywords for the item using the PATCH endpoint
        if keywords:
            print(f"Updating keywords for item ID {item_id}: {keywords}")
            update_keywords(endpoint_url, item_id, keywords)
        else:
            print(f"No keywords extracted for {link}. Skipping update.")
    
    print("Processing complete.")

# Entry point
if __name__ == "__main__":
    main()
