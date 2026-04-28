import requests
import json
from datetime import datetime

# ── Config ─────────────────────────────────────────────────
API_KEY  = "7154ed19f5424d98b7429db5520b811a"   
BASE_URL = "https://newsapi.org/v2/everything"

# ── Fetch news ─────────────────────────────────────────────
def fetch_news(query, language="en", max_results=5):
    """
    Fetches news articles from NewsAPI.
    Args:
        query      : search term (e.g. "artificial intelligence")
        language   : "en" for English, "es" for Spanish
        max_results: number of articles to return
    Returns:
        list of article dicts, or empty list on error
    """
    params = {
        "q"        : query,
        "language" : language,
        "pageSize" : max_results,
        "sortBy"   : "publishedAt",
        "apiKey"   : API_KEY,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return []

    data = response.json()
    return data.get("articles", [])


# ── Display results ────────────────────────────────────────
def display_articles(articles, query):
    if not articles:
        print("No articles found.")
        return

    print(f"\n{'='*55}")
    print(f"  Results for: '{query}'  ({len(articles)} articles)")
    print(f"{'='*55}\n")

    for i, article in enumerate(articles, start=1):
        title       = article.get("title", "No title")
        source      = article.get("source", {}).get("name", "Unknown")
        published   = article.get("publishedAt", "")
        url         = article.get("url", "")
        description = article.get("description", "No description available.")

        # Format date
        try:
            dt = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
            published = dt.strftime("%b %d, %Y %H:%M")
        except ValueError:
            pass

        print(f"[{i}] {title}")
        print(f"    Source    : {source}")
        print(f"    Published : {published}")
        print(f"    Summary   : {description[:120]}...")
        print(f"    URL       : {url}")
        print()


# ── Save to JSON ───────────────────────────────────────────
def save_to_json(articles, filename="results.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f"Results saved to {filename}")


# ── Main ───────────────────────────────────────────────────
if __name__ == "__main__":
    query = input("Enter a search topic: ")

    print(f"\nSearching for '{query}'...")
    articles = fetch_news(query, language="en", max_results=5)

    display_articles(articles, query)
    save_to_json(articles)
