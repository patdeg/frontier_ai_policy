# AGENTS — Operating Manual for Repo-Automation Bots 🤖

These notes keep humans and LLM agents in sync while editing **`frontier_ai_policy`**.

* **Workflow summary (humans):**
  1. Add or modify a script.
  2. Update the index block in `codex.md`.
  3. Run `python -m py_compile examples/*.py` **and** `pytest`.
  4. Use a present-tense commit message ≤ 50 chars.
  5. Push PR (CI will rerun tests).

Everything a bot needs to enforce those rules lives between the comment markers below.

---

<!-- BEGIN AGENT PROTOCOL (machine readable, do not reformat) -->
VERSION: 1.0

CHECKS:
  - name: compile
    cmd: "python3 -m py_compile examples/*.py"
  - name: tests
    cmd: "pytest -q"

NAMING_CONVENTION:
  script: "<pillar>_<scene>_<description>.py"       # e.g. 3_B_rate_limit.py
  pillars: ["PRIVACY", "FAIRNESS", "SAFETY", "TRANSPARENCY", "RELIABILITY", "INFRA"]

CODEX_UPDATE:
  file: "codex.md"
  format: "<filename>.py :: <≤80-char description> :: [TAG[,TAG]]"
  tags_required: true

REQUIREMENTS:
  file: "requirements.txt"
  mandate_sync: true                # add new deps the same PR

SECRETS:
  forbid_patterns: ["sk-", "fk-"]   # block obvious API keys
  env_template: ".env.example"

COMMIT_RULES:
  subject_max_len: 50
  style: "imperative_present"       # e.g. "Add age scrub filter"

ENV_SETUP:
  instructions:
    - "cp .env.example .env   # then fill in GROQ_API_KEY or OPENAI_API_KEY"

# End of spec — uncomment fields only with author consensus
<!-- END AGENT PROTOCOL -->
