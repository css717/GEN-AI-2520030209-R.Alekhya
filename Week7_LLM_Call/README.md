Week 7 - LLM Next Token Probability Inspection

Student: R. Alekhya
Roll Number: 2520030209
Course: GEN AI Lab

Overview

This project demonstrates how a Large Language Model generates text by inspecting the next token probability distribution. Given an input prompt, the script loads a pretrained causal language model and displays the top predicted tokens along with their logit scores and probabilities.

The model used is distilgpt2 from HuggingFace Transformers, loaded locally without any API dependency.

Project Structure

Week7_LLM_Call
    next_token_probs.py    Main script to inspect next token probabilities

Setup and Installation

Prerequisites

    Python 3.x
    pip

Install Dependencies

    pip install torch transformers

No additional requirements file is needed. The script uses torch and transformers which can be installed directly.

Running the Script

    python next_token_probs.py

How It Works

The script follows these steps:

    Step 1 - Load the tokenizer and model from HuggingFace using distilgpt2
    Step 2 - Set the model to evaluation mode
    Step 3 - Tokenize the input prompt into tensors
    Step 4 - Run a forward pass through the model with no gradient computation
    Step 5 - Extract logits for the last token position
    Step 6 - Apply softmax to convert logits into probabilities
    Step 7 - Retrieve the top K tokens using torch.topk
    Step 8 - Decode each token and print rank, token string, token ID, logit value, and probability

Key Function

inspect_next_token takes three parameters:

    prompt      - the input text string
    model_name  - the HuggingFace model identifier, default is distilgpt2
    top_k       - number of top predictions to display, default is 5

Sample Output

The script runs with the prompt "The capital of France is" and prints a table showing the top 5 candidate next tokens with their probability scores.

Example output columns:

    Rank
    Token
    Token ID
    Logit
    Probability

Notes

    The venv folder is excluded from version control via gitignore
    The model is downloaded automatically on first run from HuggingFace Hub
    No GPU is required, the script runs on CPU

Release

    Version: v1.0
    Model: distilgpt2
    Task: Next Token Probability Inspection
