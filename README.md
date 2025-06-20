# Frontier AI Policy 🛡️ — *from PDF to Pull-Request*

> “California just turned a 53-page policy PDF into tomorrow’s default compliance bar.  
>  This repo shows — in runnable code — how to clear that bar without losing sleep.”  
>  — *California’s “Trust-but-Verify” Blueprint for Frontier AI*

---

## What’s in here?

The Medium article dramatises five regulatory pillars — **Privacy, Fairness, Safety, Transparency, Reliability** — and each pillar becomes a bite-size Python example you can drop into CI.  
File names mirror the narrative (e.g. `1_A_age_scrub.py` = Chapter 1, Scene A).

> **Heads-up:** `codex.md` is a *machine-readable* index for automated agents.  
>  The table below is the *human-friendly* script catalogue.

| Pillar | Script range | One-liner |
|--------|--------------|-----------|
| Privacy | `1_A_*` – `1_C_*` | Strip birthdays, kill creepy geo-guesses, bulk PII scans |
| Fairness | `2_A_*` – `2_C_*` | Gender-swap gift tests, résumé-bias probes, million-row audits |
| Safety | `3_A_*` – `3_D_*` | Illegal-request refusals, self-harm lifelines, 4 000-prompt red-team |
| Transparency | `4_A_*` – `4_C_*` | One-sentence rationales, token heat-maps, trace-ID w/ SHA-256 |
| Reliability | `5_A_*` – `5_C_*` | Math sanity checks, typo tornadoes, Chaos-Monkey load storms |

---

## Quick start

```bash
git clone https://github.com/patdeg/frontier_ai_policy.git
cd frontier_ai_policy

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # add your API keys here

pytest                      # run all guardrail checks
````

---

## Which models?

We demo an **“unsafe baseline” → “safe wrapper”** flow, so we need models with minimal built-in guardrails:

| Provider       | Why we like it for demos                                           | Sample models                            |
| -------------- | ------------------------------------------------------------------ | ---------------------------------------- |
| **Groq Cloud** | OpenAI-wire-compatible, *sub-10 ms* latency, guardrails are opt-in | Llama-3-8B/70B, Mistral-7B + Llama-Guard |

---

## 🚀 Groq Cloud — zero-to-token in 5 minutes

| Step | What to do                                                                                                                               |
| ---: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|    1 | **Create an account:** [https://console.groq.com/](https://console.groq.com/) (GitHub, Google, or email).                                |
|    2 | **Generate an API key:** **API Keys → Create API Key**, copy it once.                                                                    |
|    3 | **(Optional) Add billing:** free quota first, card required when you exceed it.                                                          |
|    4 | **Set env vars** in `.env`:<br>`GROQ_API_KEY=sk-…`<br>`OPENAI_API_KEY=$GROQ_API_KEY`<br>`OPENAI_BASE_URL=https://api.groq.com/openai/v1` |
|    5 | **Ping the model:**                                                                                                                      |

```python
import os, openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

resp = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[{"role": "user", "content": "Hi, I turned 30 today"}],
)

print(resp.choices[0].message.content)
# -> Happy 30th birthday! 🎉
```

Swapping providers later is three lines of config.

---

## Project philosophy 🥋

* **Tiny, test-first** — each script ≤ 100 LOC with an `assert` so CI fails loudly.
* **Show, don’t tell** — runnable code beats policy prose.
* **Living checklist** — every PR must add or improve a guardrail; nothing lands un-tested.
* **Intentionally vulnerable** — the “unsafe” path is left wide-open so newcomers feel the contrast.

---

## Contributing

1. Fork → branch → PR.
2. Keep examples small and self-contained.
3. **Update one line in `codex.md`** using the strict<br>`filename.py :: description :: TAGS` format (see its header).
4. Ensure `pytest` stays green.

---

## License

MIT. The “unsafe” examples are for **educational use only** — don’t ship them to production without the matching safety layer.

---

> *Trust, then verify  — and if it’s an LLM, verify twice.*

