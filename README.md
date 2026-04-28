# News Searcher CLI

A command-line tool that fetches and displays recent news
articles on any topic using the NewsAPI.

## Features
- Search any topic in English or Spanish
- Shows title, source, date, summary and URL
- Saves results to a JSON file for further analysis
- Clean terminal output with formatted dates

## Tech stack
- Python 3.10+
- requests
- json (built-in)
- datetime (built-in)

## Setup

1. Get a free API key at https://newsapi.org/register
2. Open `main.py` and replace `YOUR_API_KEY_HERE`
3. Install dependencies and run:

```bash
pip install requests
python main.py
```

## Example usage

```
Enter a search topic: climate change

Results for: 'climate change'  (5 articles)
...
Results saved to results.json
```

## What I learned
- How to make HTTP requests with the `requests` library
- How to parse and navigate JSON responses
- How to handle API errors gracefully
- How to format and save structured data

## Author
Antonio de Jesus Ruiz Campos — built as part of a Python portfolio.
