import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def extract_article_texts(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    articles = []
    for anchor in soup.find_all('a'):
        if anchor:
            text = anchor.get_text()
            articles.append({'text': text})
    
    return articles

if __name__ == "__main__":
    topic = "OpenAI"  # Replace with anything you want to search for
    url = f"https://news.google.com/search?q={topic}&hl=en-US&gl=US&ceid=US:en"
    
    html_content = fetch_webpage(url)
    
    if html_content:
        articles = extract_article_texts(html_content)
        print(f"Found {len(articles)} articles for {company_name}:")
        for article in articles:
            print(f"Text: {article['text']}")
            print()
