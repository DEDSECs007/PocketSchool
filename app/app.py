import streamlit as st
import os
from agents import NotesAgent, ResearchAgent, PlannerAgent

# UI Title
st.title("📚 Pocket School — AI Study Companion")

task = st.selectbox(
    "Choose what you want help with:",
    ["Summarize Notes", "Research Topic", "Create Study Plan"]
)

user_input = st.text_area("Enter your text or topic here:")

if st.button("Generate"):
    if not os.getenv("GOOGLE_API_KEY"):
        st.error("❌ API Key not found! Add it in Streamlit Secrets.")
    elif not user_input.strip():
        st.warning("⚠️ Please enter some input first!")
    else:
        if task == "Summarize Notes":
            result = NotesAgent("a note simplification agent").summarize(user_input)

        elif task == "Research Topic":
            result = ResearchAgent("a student-friendly researcher").research(user_input)

        elif task == "Create Study Plan":
            result = PlannerAgent("a study planner expert").create_plan(user_input, 10)

        st.success(result)
