# Basic Chatbot

A conversational chatbot built with [Streamlit](https://streamlit.io/), [LangChain](https://www.langchain.com/), and Hugging Face. It keeps the conversation visible during a browser session and generates replies with the `Qwen/Qwen3.8-27B:ovhcloud` model.

## Features

- Chat-style interface with conversation history
- Hugging Face model inference through LangChain
- One-click button to clear the current chat
- Local environment-variable configuration for the Hugging Face token

## Requirements

- Python 3.10 or newer
- A Hugging Face access token

## Installation

Clone the repository and enter it:

```bash
git clone https://github.com/Akshay-3210/basic-chatbot.git
cd basic-chatbot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Hugging Face token:

```env
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
```

## Run the app

```bash
streamlit run chatbot.py
```

Open the local address Streamlit displays in the terminal, type a message, and press Enter. Use **🗑️ Clear Chat** to start a fresh conversation.

## Project files

- `chatbot.py` — the Streamlit chatbot application
- `prompt_ui.py` — a separate paper-summary interface
- `requirements.txt` — Python dependencies

## Security

Never commit your `.env` file or Hugging Face token. If a token is exposed, revoke it from your Hugging Face account and issue a new one.
