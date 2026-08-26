# Price Sensitivity Survey — Hasbro Gaming Candy Land Kingdom

## Task instruction

# Hasbro Gaming Candy Land Kingdom Price Sensitivity Survey

We're gathering reactions to **Hasbro Gaming Candy Land Kingdom** — an Amazon toys & games listing rated 4.8 stars across ~37,485 customer ratings.

One thing to weigh: the listed price recently changed from **$12.99** to **$16.24**. After reading the brief, tell us how the current price sits with you and where it would start to feel like too much.

## How to answer

- Read the brief before you start.
- Answer every required question.
- For multiple-choice, use the listed option ids.
- For rating scales, use a whole number in the given range.
- Give the answer alone unless a question also asks for a short reason or confidence.

## Context

# Product brief — Hasbro Gaming Candy Land Kingdom of Sweet Adventures Board Game for Kids, Easter Gifts for Boys and Girls, Ages 3 & Up (Amazon Exclusive)

**Category:** Toys And Games
**Brand:** None
**Where sold:** Amazon (major online retailer)

## Key details

- **Rating:** 4.8 out of 5 stars
- **Reviews:** ~37,485 customer ratings
- **Genre:** Family
- **Number Of Players:** 2-4
- **Edition:** Standard Edition
- **Sub Brand:** Candy Land
- **Customer Package Type:** Standard Packaging
- **Language:** English

## Pricing & recent change

- **Current listed price: $16.24**
- This is a recent change: it was previously listed at **$12.99**, so the price the shopper now sees is higher (about 25% higher).

## What this survey is probing

How a shopper reacts to this product at its **current** terms — use only the details in this brief and the questionnaire; do not invent other product facts.

## Questionnaire

# Price Sensitivity Survey — Hasbro Gaming Candy Land Kingdom

Use exact `questionId` and valid choice ids.

## q_price_matters

Prompt: The price is the single most important factor in whether I would buy the Hasbro Gaming Candy Land Kingdom.

- Construct: `price_centrality`
- Type: `likert`
- Required: `true`
- Scale: `1`-`5`

Rate with an integer between **1** and **5**.


## q_too_expensive

Prompt: At its current price, the Hasbro Gaming Candy Land Kingdom feels too expensive for me.

- Construct: `price_pain`
- Type: `likert`
- Required: `true`
- Scale: `1`-`5`

Rate with an integer between **1** and **5**.


## q_threshold

Prompt: What best describes your reaction to the current price?

- Construct: `price_threshold`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `cheap_stock_up` | So reasonable I might buy more than one. |
| `fair_buy` | Fair enough that I would just buy it. |
| `hesitate` | High enough that I would hesitate. |
| `only_on_sale` | I would only buy it on sale. |
| `walk_away` | High enough that I would walk away. |

## q_price_vs_quality

Prompt: When you weigh price against quality here, which wins?

- Construct: `price_quality_tradeoff`
- Type: `single_choice`
- Required: `true`
- Ask rationale: `true`

| choice_id | label |
|-----------|-------|
| `price_first` | I prioritize the lowest price. |
| `balance` | I want a balance of price and quality. |
| `quality_first` | I will pay more for quality. |

Include a concise `rationale` specific to this answer.

## Answer envelope

Platform-derived answer envelope (from `questionnaire.yaml`).

```json
{
  "instrument": {"id": "price_sensitivity_v1", "title": "Price Sensitivity Survey — Hasbro Gaming Candy Land Kingdom"},
  "answers": [
    {
      "questionId": "q_price_matters",
      "value": "<answer value>"
    }
  ]
}
```

Use exact `questionId` values from the questionnaire.
For choice questions, `value` must be the exact choice id (or list of ids for multi-select).
Default surveys emit `questionId` + `value` only (choice / likert / bool).