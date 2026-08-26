# Inspect Example Domain

## Your situation

You are a user evaluating reference websites and documentation domains. Read the scenario brief in `input/context.md`, then use the live website to record your assessment.

## Your goal

Browse the live website at `https://example.com/`, inspect the headline and informational content, follow the reference link to IANA's example domain documentation, and record your assessment and choice.

## Constraints on your behavior

- Use only information visible on the live `https://example.com/` web page and its referenced documentation page.
- Do not invent site headings, URLs, or descriptions not present on the live pages.
- Do not attempt unauthorized actions or visit unrelated third-party sites.

## Interaction requirements

Inspect the page content, capture a screenshot of the page to `/app/output/screenshot.png`, verify the header text and the destination link provided for more information, then save your selection to `/app/output/example_choice.json`:

```json
{
  "decision_subject_id": "example-domain",
  "decision_subject_label": "<page title or header text exactly as shown>",
  "decision_outcome": "selected",
  "basis_primary": "<price|quality|features|convenience|taste|trust|familiarity|novelty|fit|other>",
  "basis_secondary": "<optional second value from the same enumeration>",
  "exploration_style": "<quick_pick|compared_multiple|deep_research|hesitant>",
  "reason": "<why this resource satisfies your illustrative or documentation need>",
  "task_site_url": "https://example.com/",
  "task_more_info_url": "<destination URL of the more information link>"
}
```

## Termination criteria

- `decision_subject_id` should be `example-domain`.
- `decision_subject_label` must accurately reflect the title or main heading from the page ("Example Domain").
- `task_site_url` must be `https://example.com/`.
- `task_more_info_url` must be the URL pointed to by the "More information..." link (e.g. `https://www.iana.org/domains/example` or `https://www.iana.org/help/example-domains`).
- `basis_primary` must be one of the standard basis values.
- Finish after saving the completed JSON file.

## Success judgment

The task is successful when the saved JSON follows the required structure and contains accurate header, site URL, and reference link metadata faithful to the live `https://example.com/` website.
