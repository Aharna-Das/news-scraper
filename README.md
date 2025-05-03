# 📰 Google News Article Text Extractor

A lightweight Python script that scrapes article anchor texts from Google News search results for a given topic. It uses `requests` and `BeautifulSoup` to fetch and parse HTML content.

---

## 📌 Features

- 🔍 Search Google News for any topic
- 🧹 Extract anchor text (headlines, links, and tags)
- 📦 Simple and easy to run, using standard Python libraries

---

## 📁 Project Structure

.
├── news_scraper.py # Main Python script
├── README.md # This file


---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have Python installed (version 3.6 or above).

Install the required dependencies using:

```bash
pip install requests beautifulsoup4
```
▶️ How to Run
Edit the Topic (Optional)
Open the script and change the topic variable to your desired search term:

```bash
topic = "OpenAI"
Run the Script
```
```bash
python news_scraper.py
```
View Results
The script will output the number of anchor texts found on the Google News results page, along with each extracted text.

🔍 Example Output
```text
Found 42 articles for OpenAI:
Text: OpenAI’s latest model GPT-4 Turbo is now cheaper and faster
Text: Sam Altman says AI is reshaping the internet
```
Note: Results depend on the current state of the Google News page and may vary.

📜 Code Overview
fetch_webpage(url)
Fetches HTML content from the given URL using requests. Handles HTTP errors gracefully.

extract_article_texts(html_content)
Uses BeautifulSoup to parse the HTML and extract all <a> tag texts.

⚠️ Limitations
This script does not extract full article content, only the anchor text shown on the Google News search page.

Google may block or rate-limit frequent automated requests.

Page structure may change, which can break scraping logic.

📌 Disclaimer
This script is for educational and personal use only. Always review and respect the Terms of Service of any site you scrape.

