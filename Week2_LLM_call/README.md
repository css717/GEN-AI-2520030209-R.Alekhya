# Week 2 — Multi-Provider LLM Client 🔀

This week we level up — instead of hardcoding one AI provider, we build a flexible client that can talk to either **Gemini (cloud)** or **Ollama (local)** using the same code.

## What it does

- Asks you to choose a provider — Gemini or Ollama
- Takes your question as input
- Routes it to the right AI and prints the answer
- Includes a **unit test** using a fake provider (so no real API needed to test)

## Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point — picks provider, takes your input, prints response |
| `llm_client.py` | The provider abstraction (GeminiProvider, OllamaProvider, LLMClient) |
| `test-client.py` | Unit test with a fake/mock provider |
| `requirements.txt` | Python packages needed |

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create a .env file
echo GEMINI_API_KEY=your_key_here > .env

# 3. Run it
python main.py
# → Choose provider (gemini/ollama): gemini
# → Enter your question: What is machine learning?

# 4. Run tests
python -m pytest test-client.py
```

> 💡 To use Ollama locally, [install Ollama](https://ollama.com) and run `ollama pull llama3.2` first.

## Dependencies

- `google-genai`, `python-dotenv`, `requests`, `pytest`
