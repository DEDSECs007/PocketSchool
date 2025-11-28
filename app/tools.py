import os
import requests

API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

def search_web(query):
    if not SEARCH_ENGINE_ID:
        return "No search engine ID configured. Basic mode."

    url = (
        "https://www.googleapis.com/customsearch/v1?"
        f"key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    )

    try:
        res = requests.get(url).json()
        results = res.get("items", [])

        if not results:
            return "No web results found."

        return "\n".join(
            f"- {item['title']}: {item['link']}"
            for item in results[:5]
        )

    except Exception as e:
        return f"(Search error: {e})"
