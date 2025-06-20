# Frontier AI Policy Codex

This codex is a living document for the `frontier_ai_policy` repository.  The repository contains Python examples that accompany the article `article.md`: *California’s "Trust-but-Verify" Blueprint for Frontier AI — Expert Edition*.  Each script demonstrates a lightweight compliance check inspired by the policy.

Whenever new examples are added or existing code changes, update this file so that it accurately reflects the latest logic and history of the project.  The codex should help future contributors understand the purpose of each script and how the pieces fit together.

## Current Scripts

- **age_echo_scrub.py** — regex filter that removes phrases like `"30 years old"` before the model can echo them back.
- **gps_free_cafe.py** — obtains generic café suggestions without exposing or inferring the user’s exact location.
- **presidio_pii_sweep.py** — uses Microsoft Presidio to scan thousands of model replies for leaked PII.
- **arithmetic_pop_quiz.py** — quick smoke test to verify basic arithmetic ability ("What is 2 + 2?").
- **typo_tornado.py** — ensures gibberish input does not crash the assistant.
- **chaos_monkey_load_storm.py** — stress test with hundreds of simultaneous calls while a dependency is down.
- **gift_shop_gender_flip.py** — checks for gender bias in product recommendations.
- **resume_roulette.py** — validates that identical résumés with different names receive the same score.
- **million_profile_audit.py** — large-scale fairness audit using Fairlearn on one million synthetic loan prompts.
- **wifi_hack_refusal.py** — verifies that the model refuses illegal hacking requests.
- **self_harm_lifeline.py** — prompts the assistant to respond to self-harm statements with crisis resources.
- **red_team_gauntlet.py** — overnight batch of jailbreak prompts to ensure consistent refusals.
- **llm_referee.py** — second-model evaluator built with OpenAI Evals to judge safety refusals.
- **opentelemetry_wrapper.py** — example of tracing prompts and answers with OpenTelemetry while redacting PII.
- **rationale_tag.py** — attaches a short explanation or rationale tag to each answer.
- **token_heat_map.py** — toy saliency map showing token importances in a response.
- **chatty.py** — minimal wrapper that now calls Groq's OpenAI-compatible API with optional safety.

## Updating This Codex

1. Reflect any user request or repository change in this file.
2. Summarize the purpose of new scripts or documentation.
3. Keep entries concise, one or two sentences per script.
4. Commit updates alongside code changes so history stays synchronized.
