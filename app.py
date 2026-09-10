import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.write("Powered by Hugging Face")

token = os.environ.get("HF_TOKEN")

if not token:
    st.error("HF_TOKEN is not set.")
    st.stop()

client = InferenceClient(api_key=token)

model = st.selectbox(
    "Select Model",
    [
        "openai/gpt-oss-120b",
        "google/gemma-2-2b-it",
        "Qwen/Qwen2.5-Coder-32B-Instruct"
    ]
)

question = st.text_area(
    "Enter your question",
    placeholder="Example: Explain normalization in DBMS..."
)

if st.button("Ask AI"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI tutor. Explain simply."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            st.subheader("AI Response")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(str(e))