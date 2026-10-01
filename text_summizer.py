import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Text Summarizer")

text = st.text_area("Enter your text:")

if st.button("Summarize"):
    if text:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this text in simple words:\n\n{text}"
                }
            ]
        )

        st.subheader("Summary")
        st.write(response["message"]["content"])
    else:
        st.warning("Please enter some text.")
