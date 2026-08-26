# Web Example Domain Task

Explore and inspect the public website at https://example.com/ and its documentation reference link.

## Task Overview

- **Target URL**: https://example.com/
- **Runtime**: `application/shared-web-playwright`
- **Output Artifact**: `/app/output/example_choice.json`

## Files

- `task.toml`: Harbor task configuration and metadata.
- `instruction.md`: Prompt instructions and JSON schema for the agent.
- `input/context.md`: Background context for the scenario.
- `input/self_report_schema.yaml`: Schema for persona subjective evaluation feedback.
- `reporting.json`: Reporting distributions and analyses for batch evaluation.
- `persona_strategy.json`: Persona sampling configuration.
- `solution/solve.sh`: Oracle solution script using Playwright.
- `tests/test_state.py`: Verifier test validating the output artifact and recording structured output.
