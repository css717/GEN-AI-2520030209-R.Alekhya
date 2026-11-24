# Week 3 — LLM Monitoring with Usage Logging 📊

This week adds something really useful — every time you call an LLM, we **log the usage details** (tokens, cost, latency) to a **MongoDB database** so you can track it over time.

## What it does

- Same Gemini/Ollama provider choice as Week 2
- After each API call, it logs to MongoDB:
  - Input & output token counts
  - Estimated cost in USD
  - Latency (how fast the response came)
  - Success/failure status + retry attempts
- Has **retry logic** — if a call fails with a temporary error, it automatically retries up to 3 times with a backoff delay

## Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point — provider selection + question input |
| `llm_client.py` | Provider abstraction with retry logic + cost calculation |
| `usage_logger.py` | Saves usage records to MongoDB |
| `test_client.py` | Unit tests |
| `requirements.txt` | Python packages needed |

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create a .env file with keys
GEMINI_API_KEY=your_key_here
MONGODB_URI=mongodb+srv://your_connection_string
GEMINI_INPUT_PRICE_PER_MILLION=0.075
GEMINI_OUTPUT_PRICE_PER_MILLION=0.30

# 3. Run it
python main.py

# 4. Run tests
python -m pytest test_client.py
```

> 💡 Get a free MongoDB cluster at [mongodb.com/atlas](https://www.mongodb.com/atlas). Your usage logs go into the `llm_monitoring.api_usage` collection.

## Dependencies

- `google-genai`, `python-dotenv`, `requests`, `pymongo`, `pytest`
