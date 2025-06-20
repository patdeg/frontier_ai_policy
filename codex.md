# Frontier AI Policy — Codex Index

This file is primarily for machines.  
Each line inside the index block follows the pattern:

```
<filename>.py :: <≤80-char description> :: \[comma-separated TAGS]
```

`TAGS` map to the five policy pillars:

```
PRIVACY   FAIRNESS   SAFETY   TRANSPARENCY   RELIABILITY   INFRA
```

---

<!-- BEGIN INDEX (do not edit format, one script per line) -->
1A_age_echo_scrub.py       :: Redacts explicit age phrases before model echo            :: PRIVACY
1B_gps_free_cafe.py        :: Suggests cafés without inferring precise GPS              :: PRIVACY
1C_presidio_pii_sweep.py   :: Batch PII scan for 1k personas via Presidio           :: PRIVACY
2A_gift_shop_gender_flip.py :: Detects gender bias in gift recommendations               :: FAIRNESS
2B_resume_roulette.py       :: Verifies identical résumés score the same                 :: FAIRNESS
2C_million_profile_audit.py :: Fairlearn audit over 1k synthetic loan prompts           :: FAIRNESS
3A_wifi_hack_refusal.py     :: Ensures model refuses illegal hacking instructions        :: SAFETY
3B_self_harm_lifeline.py    :: Crisis-line response to self-harm statements              :: SAFETY
3C_red_team_gauntlet.py     :: Jailbreak barrage on 1k prompts + pass/fail log           :: SAFETY
3D_llm_referee.py           :: Second-model judge evaluating 1k safety refusals          :: SAFETY,TRANSPARENCY
5A_arithmetic_pop_quiz.py   :: Sanity-check 2 + 2 math correctness                       :: RELIABILITY
5B_typo_tornado.py          :: Robustness test: gibberish input must not crash           :: RELIABILITY
5C_chaos_monkey_load_storm.py :: Stress test: 100s of calls while dependency down          :: RELIABILITY
4A_rationale_tag.py         :: Appends one-sentence rationale to every answer            :: TRANSPARENCY
4B_token_heat_map.py        :: Simple saliency heat-map for response tokens              :: TRANSPARENCY
4C_opentelemetry_wrapper.py :: Trace prompts/answers via OpenTelemetry (PII redacted)    :: TRANSPARENCY
examples/chatty.py          :: Groq client with safe-mode toggle (demo helper)           :: INFRA
examples/hello_world.py     :: One-liner smoke test printing a Chatty reply              :: INFRA
examples/test.py            :: Shows safe vs unsafe responses for a sample prompt        :: INFRA
<!-- END INDEX -->

---

## Adding or Updating Scripts

1. **One line per script** inside the index block, exact format above.  
2. Keep descriptions ≤ 80 characters; start with a verb.  
3. Include at least one pillar tag; use `INFRA` for helper utilities.  
4. Commit `codex.md` update in the same PR as the code.

*Human-oriented details live in `README.md`; this file stays terse for the bots.*
