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