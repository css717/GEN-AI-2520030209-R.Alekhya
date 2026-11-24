# Week 1 — First LLM Call 🚀

Your very first connection to a real AI model! This task is about making a simple call to Google's Gemini API and printing out the response.

## What it does

- Loads your Gemini API key from a `.env` file
- Sends the prompt *"What is Artificial Intelligence? Explain in simple words."* to Gemini
- Prints the AI's answer to your terminal

That's it — no fancy setup, just a clean, single-script introduction to talking with an LLM.

## Files

| File | Purpose |
|------|---------|
| `main.py` | The main script that calls the Gemini API |
| `requirements.txt` | Python packages needed |

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create a .env file with your key
echo GEMINI_API_KEY=your_key_here > .env

# 3. Run it!
python main.py
```

## Dependencies

- `google-genai` — Gemini SDK
- `python-dotenv` — loads the `.env` file
