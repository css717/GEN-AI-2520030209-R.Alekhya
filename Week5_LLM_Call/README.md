// Week 5 — Token Economics & Budget Planning

Before you ship an AI feature, you need to know: *can we afford it?* This week builds a **budget calculator** that estimates token usage and costs — and checks if your design fits within API rate limits and spending caps.

## What it does

Takes your usage assumptions from a `.env` file (requests/day, token counts, pricing) and produces a full report:

- **Token usage** — input/output/total tokens per day
- **Cost estimate** — daily and monthly in USD
- **Rate limit checks** — are you within RPM and TPM limits?
- **Budget checks** — does cost stay under your daily/monthly cap?
- **Safety margin** — applies a configurable buffer (default 20%) to all checks
- **Verdict** — PASS or REVIEW for each constraint


INPUT_PRICE_PER_MILLION=0.075
OUTPUT_PRICE_PER_MILLION=0.30
RPM_LIMIT=60
TPM_LIMIT=100000
MONTHLY_BUDGET_USD=50
DAILY_BUDGET_USD=2
SAFETY_MARGIN_PERCENT=20

# 3. Run the report
python budget.py

# 4. Run tests
python -m pytest test_budget.py
```

## Example Output

```
TOKEN ECONOMICS REPORT:
Input tokens/day:  1,000,000
Output tokens/day: 500,000
Total tokens/day:  1,500,000
Estimated daily cost:   $0.2250
Estimated monthly cost: $6.75

CHECKS
RPM capacity:   PASS
TPM capacity:   PASS
Daily budget:   PASS
Monthly budget: PASS

Recommendation: WITHIN configured planning limits.


