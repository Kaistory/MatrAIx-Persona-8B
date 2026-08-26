#!/bin/bash
set -euo pipefail

mkdir -p /app/output

python <<'PY'
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

url = "https://example.com/"
output = Path("/app/output/example_choice.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded", timeout=60_000)
    page.screenshot(path="/app/output/screenshot.png", full_page=True)
    
    heading = page.locator("h1").inner_text().strip()
    more_info_link = page.locator("a").get_attribute("href") or "https://www.iana.org/domains/example"
    browser.close()

payload = {
    "decision_subject_id": "example-domain",
    "decision_subject_label": heading or "Example Domain",
    "decision_outcome": "selected",
    "basis_primary": "fit",
    "exploration_style": "quick_pick",
    "reason": "This example domain accurately demonstrates standard illustrative documentation structure.",
    "task_site_url": "https://example.com/",
    "task_more_info_url": more_info_link,
}
output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
PY
