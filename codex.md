# frontier_ai_policy / CODEX INDEX
# ---------------------------------------------------------------------------
# PURPOSE:
#   Machine-readable lookup for LLMs.  Lists every Python script with one
#   short description and the pillar tag(s) it supports.
#
#   Format (one script per line, no wrapping):
#     <filename>.py :: <≤80-char description> :: [comma-separated TAGS]
#
#   TAGS (5 policy pillars):
#     PRIVACY   FAIRNESS   SAFETY   TRANSPARENCY   RELIABILITY
# ---------------------------------------------------------------------------

age_echo_scrub.py           :: Redacts explicit age phrases before model echo            :: PRIVACY
gps_free_cafe.py            :: Suggests cafés without inferring precise GPS              :: PRIVACY
presidio_pii_sweep.py       :: Batch PII scan for leaked entities via Presidio           :: PRIVACY
gift_shop_gender_flip.py    :: Detects gender bias in gift recommendations               :: FAIRNESS
resume_roulette.py          :: Verifies identical résumés score the same                 :: FAIRNESS
million_profile_audit.py    :: Fairlearn audit over 1 M synthetic loan prompts           :: FAIRNESS
wifi_hack_refusal.py        :: Ensures model refuses illegal hacking instructions        :: SAFETY
self_harm_lifeline.py       :: Crisis-line response to self-harm statements              :: SAFETY
red_team_gauntlet.py        :: Overnight jailbreak barrage + pass/fail log               :: SAFETY
llm_referee.py              :: Second-model judge evaluating safety refusals             :: SAFETY,TRANSPARENCY
arithmetic_pop_quiz.py      :: Sanity-check 2+2 math correctness                         :: RELIABILITY
typo_tornado.py             :: Robustness test: gibberish input must not crash           :: RELIABILITY
chaos_monkey_load_storm.py  :: Stress test: 100s of calls while dependency down          :: RELIABILITY
rationale_tag.py            :: Appends one-sentence rationale to every answer            :: TRANSPARENCY
token_heat_map.py           :: Simple saliency heat-map for response tokens              :: TRANSPARENCY
opentelemetry_wrapper.py    :: Trace prompts/answers via OpenTelemetry (PII redacted)    :: TRANSPARENCY
chatty.py                   :: Groq client w/ safe-mode toggle (demo helper)             :: INFRA
hello_world.py              :: One-liner smoke test printing a Chatty reply              :: INFRA
test.py                     :: Shows safe vs unsafe responses for a sample prompt        :: INFRA

# ---------------------------------------------------------------------------
#  ADDING NEW SCRIPTS
# ---------------------------------------------------------------------------
# 1. Keep filename snake_case; avoid spaces.
# 2. Write docstring inside the script; keep entry here ≤80 chars.
# 3. Append new line in the same format; include TAG(S).
# 4. Commit codex.md update in the same PR as the script.
#
# NOTE:
#   Human-oriented explanations live in README.md.  This file stays terse
#   for fast LLM digestion.  Do not add Markdown tables, images, or long
#   paragraphs here.
# ---------------------------------------------------------------------------
