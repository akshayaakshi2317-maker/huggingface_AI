# huggingface_AI

A simple AI Chatbot built using **Python, Streamlit, and Hugging Face Inference API**.

<img width="851" height="359" alt="Screenshot 2026-09-10 201239" src="https://github.com/user-attachments/assets/22bee546-4f74-4783-816d-016f9f8d9af6" />

<img width="718" height="404" alt="Screenshot 2026-09-10 201303" src="https://github.com/user-attachments/assets/7afdac7c-d72d-43ff-bcaa-e199fa842bd9" />

## Features

* Ask questions and get AI-generated answers
* Multiple Hugging Face models
* Simple and user-friendly interface
* Student-friendly AI responses
* Built with Streamlit

## Technologies Used

* Python
* Streamlit
* Hugging Face Inference API
* Hugging Face Hub

## Models

The chatbot supports:

* `openai/gpt-oss-120b`
* `google/gemma-2-2b-it`
* `Qwen/Qwen2.5-Coder-32B-Instruct`

## Installation

Install the required packages:

```bash
pip install streamlit huggingface_hub
```

## Hugging Face Token

Create a Hugging Face access token and set it as an environment variable.

### Windows PowerShell

```powershell
$env:HF_TOKEN="your_huggingface_token"
```

## Run the Application

```bash
streamlit run app.py
```

The chatbot will open in your browser.

## How It Works

1. User enters a question.
2. Streamlit sends the question to the Hugging Face Inference API.
3. The selected AI model processes the question.
4. The generated response is displayed on the webpage.

## Project Structure

```text
AI-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

## Use Cases

This chatbot can be used for:

* Programming questions
* Python and Java learning
* AI concepts
* DBMS topics
* General student queries

## Author

**Akshaya K**

BSc Computer Science with Artificial Intelligence
