// Week 2 — Multi-Provider LLM Client 

This week we level up — instead of hardcoding one AI provider, we build a flexible client that can talk to either **Gemini (cloud)** or **Ollama (local)** using the same code.

## What it does

- Asks you to choose a provider — Gemini or Ollama
- Takes your question as input
- Routes it to the right AI and prints the answer
- Includes a **unit test** using a fake provider (so no real API needed to test)
- 
