📚 PocketSchool — AI Study Companion

PocketSchool is an intelligent learning assistant designed to help students study faster and smarter.
Built as part of the Google x Kaggle 5-Day AI Agents Intensive Capstone, this project uses Gemini-powered agents to:

✔ Summarize notes
✔ Research topics
✔ Create personalized study plans
✔ Remember previous context using memory
✔ (Optional) Perform web search

🚀 Features
Feature	Description
🔹 Multi-Agent System	Notes Agent, Research Agent, Planner Agent
🔹 Gemini LLM Integration	Uses the latest models/gemini-2.5-flash model
🔹 Web Interface	Built with Streamlit for fast usability
🔹 Memory System	Saves previous responses for continuity
🔹 Search Tool (Optional)	Uses Google Custom Search API for real-world references
🔹 Extensible	Designed for more tools and agents
🧠 Agents Included
Agent	Purpose
✍️ NotesAgent	Summarizes text into simple points
🔍 ResearchAgent	Researches topics and outputs structured notes
🗓 PlannerAgent	Creates weekly personalized study plans
🏗️ Tech Stack

Python 3.10+

Streamlit

Google Generative AI

dotenv for secrets

JSON for memory storage

📦 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/PocketSchool.git
cd PocketSchool


Install dependencies:

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file inside the app/ folder:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
SEARCH_ENGINE_ID=YOUR_GOOGLE_CUSTOM_SEARCH_ID  # optional


⚠️ Never commit .env to GitHub.
A .gitignore file already prevents it from uploading.

▶️ Run the App

From the project root:

streamlit run app/app.py

🌍 Deployment Guide

PocketSchool can be deployed on:

Platform	Status	Notes
Streamlit Cloud ⭐ Best	✔ Working	Add secrets in Streamlit settings
Google Cloud Run	✔ Possible	Requires Docker
Hugging Face Spaces	✔	Add secrets manually
Vercel	⚠ Experimental	Requires wrapper
📂 Project Structure
PocketSchool/
 ├─ app/
 │   ├─ app.py
 │   ├─ agents.py
 │   ├─ tools.py
 │   ├─ memory.json
 │   └─ .env   (ignored)
 ├─ requirements.txt
 └─ README.md

🧪 Example Outputs

Summarization: Converts text into clean bullet notes

Research: Structured explanation with key points

Planning: A weekly learning schedule based on topic and available hours

🎯 Future Improvements

🔊 Text-to-Speech for summaries

🎓 Adaptive learning based on user progress

💾 Database storage instead of JSON

🧩 Plugin marketplace for new tools

🏅 Author & Credits

Built by: Harsh Dholiya

For: Google x Kaggle AI Agents Bootcamp 2025

Model Powered by: 📌 Gemini API
