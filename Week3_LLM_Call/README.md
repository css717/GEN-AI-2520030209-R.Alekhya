//Week 3 — LLM Monitoring with Usage Logging

This week adds something really useful — every time you call an LLM, we **log the usage details** (tokens, cost, latency) to a **MongoDB database** so you can track it over time.

// What it does

- Same Gemini/Ollama provider choice as Week 2
- After each API call, it logs to MongoDB:
  - Input & output token counts
  - Estimated cost in USD
  - Latency (how fast the response came)
  - Success/failure status + retry attempts
- Has **retry logic** — if a call fails with a temporary error, it automatically retries up to 3 times with a backoff delay
