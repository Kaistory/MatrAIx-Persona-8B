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