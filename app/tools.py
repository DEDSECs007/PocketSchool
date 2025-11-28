import requests
import os
from dotenv import load_dotenv

# Load .env file from absolute location
load_dotenv(r"X:\000 PocketSchool\app\.env")

API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")


# ---- Google Search Tool ----
def search_web(query):
    if not API_KEY or not SEARCH_ENGINE_ID:
        return "❌ Missing API Key or Search Engine ID. Check .env file."

    url = (
        "https://www.googleapis.com/customsearch/v1?"
        f"key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        results = data.get("items", [])

        if not results:
            return "🔍 No results found."

        extracted = [
            f"📌 **{item['title']}**\n🔗 {item['link']}"
            for item in results[:5]
        ]

        return "\n\n".join(extracted)

    except Exception as e:
        return f"⚠️ Search Error: {str(e)}"
