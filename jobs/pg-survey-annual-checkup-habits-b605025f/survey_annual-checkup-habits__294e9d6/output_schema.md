Platform-derived answer envelope (from `questionnaire.yaml`).

```json
{
  "instrument": {"id": "annual_checkup_habits_v1", "title": "Annual Checkup Habits Survey"},
  "answers": [
    {
      "questionId": "q0",
      "value": "<answer value>"
    }
  ]
}
```

Use exact `questionId` values from the questionnaire.
For choice questions, `value` must be the exact choice id (or list of ids for multi-select).
Default surveys emit `questionId` + `value` only (choice / likert / bool).