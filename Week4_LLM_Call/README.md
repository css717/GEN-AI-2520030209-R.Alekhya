// Week 4 — Tokenizer Comparison

Ever wondered how different AI models "see" the same text? This week we compare three popular tokenizers side by side across English, Telugu, and Hindi text.

// What it does

Loads three tokenizers:
- **BPE** — GPT-2 style (used by OpenAI models)
- **WordPiece** — Multilingual BERT (great for many languages)
- **SentencePiece** — XLM-RoBERTa (strong on non-English scripts)

Then for each language, it shows:
- The list of tokens produced
- Their token IDs
- Total token count

You'll see firsthand why multilingual text costs more tokens and why tokenizer choice matters!
LANGUAGE: English
INPUT TEXT: Artificial intelligence is changing the world.

BPE - GPT-2
Tokens     : ['Art', 'ificial', 'Ġintelligence', ...]
Token count: 8


## Dependencies

HuggingFace tokenizer library
sentences - required for XLM-RoBERTa tokenizer
