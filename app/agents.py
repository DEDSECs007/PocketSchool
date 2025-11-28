import os
import google.generativeai as genai
from tools import search_web

# Load API Key for both local + Streamlit Secrets environments
API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

class Agent:
    def __init__(self, role):
        self.role = role
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    def run(self, prompt):
        full_prompt = f"You are {self.role}.\n\n{prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text


class NotesAgent(Agent):
    def summarize(self, text):
        return self.run(f"Summarize this text into simple study notes:\n{text}")


class ResearchAgent(Agent):
    def research(self, topic):
        web_results = search_web(topic)
        return self.run(
            f"Use the below web search results to write structured notes:\n\n"
            f"Web Results:\n{web_results}\n\n"
            f"Topic Query: {topic}"
        )


class PlannerAgent(Agent):
    def create_plan(self, subject, hours):
        return self.run(
            f"Create a detailed weekly study plan for {subject} for {hours} hours per week."
        )
