
import streamlit as st
import pandas as pd
import random

# Deep Research Assistant Section
def deep_research_builder():
    st.header("📘 Deep Research Builder – Learning Mastery")
    st.markdown("Use this tool to create a Deep Research GPT or custom AI assistant for any subject.")

    topic = st.text_input("Enter the learning topic or skill you'd like to master")
    if st.button("Generate Research Blueprint"):
        st.subheader("🔍 Suggested Prompt for Book Research")
        research_prompt = f"You're an elite strategist in learning design and transformation. Help me find the top books and resources to master '{topic}'."
        st.code(research_prompt, language='markdown')

        st.subheader("🧠 Deep Research Prompt Template")
        deep_prompt = f"You're an expert in {topic}. Based on the top 5–10 books or articles on this topic, synthesize the most important lessons, frameworks, and principles into a clear, customized learning guide for personal use."
        st.code(deep_prompt, language='markdown')

        st.subheader("🧬 GPT Training Prompt")
        system_prompt = f"You are a world-class advisor on '{topic}', trained on distilled insights from top books. Your job is to teach, coach, and prompt powerful application of this knowledge. Keep responses clear, motivational, and strategic."
        st.code(system_prompt, language='markdown')

        st.subheader("✨ Starter Prompts for Your GPT")
        st.markdown("1. 'Summarize the core principles of this field for a beginner.'")
        st.markdown("2. 'Help me apply one key insight to my life or business today.'")
        st.markdown("3. 'Give me a journaling prompt to reflect on this topic.'")
        st.markdown("4. 'Ask me 3 questions to help personalize this learning path.'")
        st.markdown("5. 'Show me how to structure this into a 7-day challenge.'")

# Main App Launcher
st.title("📚 Learning Mastery GPT Toolkit")
st.markdown("This toolkit helps you script, reflect, and build deep learning systems using GPT and Airtable integrations.")
deep_research_builder()
