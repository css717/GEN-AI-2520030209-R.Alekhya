import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def inspect_next_token(prompt: str, model_name: str = "distilgpt2", top_k: int = 5):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    next_token_logits = outputs.logits[0, -1, :]
    probabilities = torch.softmax(next_token_logits, dim=-1)
    top_probs, top_indices = torch.topk(probabilities, top_k)

    print(f"Prompt: {repr(prompt)}\n")
    print(f"{'Rank':<6} {'Token':<15} {'Token ID':<10} {'Logit':<10} {'Probability'}")
    print("-" * 55)

    for rank, (prob, idx) in enumerate(zip(top_probs, top_indices), start=1):
        token_str = repr(tokenizer.decode(idx))
        logit_val = next_token_logits[idx].item()
        prob_pct = prob.item() * 100
        print(f"{rank:<6} {token_str:<15} {idx.item():<10} {logit_val:<10.2f} {prob_pct:.2f}%")


if __name__ == "__main__":
    inspect_next_token("The capital of France is", top_k=5)