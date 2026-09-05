# Research Tool

A small Streamlit application that sends a prompt to a Hugging Face-hosted language model and displays its response.

## Prerequisites

- Python 3.10 or later
- A Hugging Face access token

## Run locally

1. Create and activate a virtual environment.

   ```bash
   python -m venv .venv
   # Windows PowerShell
   .venv\\Scripts\\Activate.ps1
   # macOS/Linux
   source .venv/bin/activate
   ```

2. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:

   ```env
   HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
   ```

4. Start the app.

   ```bash
   streamlit run prompt_ui.py
   ```

Open the local URL Streamlit prints in the terminal.

## Deploy to Streamlit Community Cloud

1. Push this repository to GitHub. Do not commit `.env` or `.streamlit/secrets.toml`.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), create an app from this repository.
3. Select `prompt_ui.py` as the main file.
4. In **Advanced settings → Secrets**, add:

   ```toml
   HUGGINGFACEHUB_API_TOKEN = "hf_your_token_here"
   ```

5. Deploy the app.

## Security

Treat your Hugging Face token as a password. If it is ever committed or shared accidentally, revoke it in Hugging Face and create a replacement token.
