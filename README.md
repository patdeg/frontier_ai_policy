# Frontier AI Policy 🛡️ — *from PDF to Pull-Request*

> “California just turned a 100-page policy PDF into tomorrow’s default compliance bar.  
>  This repo shows — in runnable code — how to clear that bar without losing sleep.”  
>  — [California’s “Trust-but-Verify” Blueprint for Frontier AI](https://medium.com/@pdeglon/californias-trust-but-verify-blueprint-for-frontier-ai-5db26b72d0f9)

---

## What’s in here?

The Medium article **dramatizes** five regulatory pillars — **Privacy, Fairness, Safety, Transparency, Reliability**.  
Each pillar becomes a short Python snippet you can drop into CI.  
File names mirror the story (e.g. `1_A_age_scrub.py` = Chapter 1, Scene A).

| Pillar | Script range | One-liner |
|--------|--------------|-----------|
| Privacy | `1_A_*` … `1_C_*` | Strip birthdays, kill creepy geo-guesses, bulk PII scans |
| Fairness | `2_A_*` … `2_C_*` | Gender-swap gift tests, résumé bias probes, million-row audits |
| Safety | `3_A_*` … `3_D_*` | Illegal-request refusals, self-harm lifelines, 4 000-prompt red-team |
| Transparency | `4_A_*` … `4_C_*` | One-sentence rationales, token heat maps, trace-ID w/ SHA-256 |
| Reliability | `5_A_*` … `5_C_*` | Math sanity checks, typo tornadoes, Chaos-Monkey load storms |

*See the full menu in* [`codex.md`](codex.md).

---

## Quick start

```bash
git clone https://github.com/patdeg/frontier_ai_policy.git
cd frontier_ai_policy
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # add your API keys here
pytest                        # run all guardrail checks
````

---

## Which models?

We need models **with minimal built-in guardrails** so you can see the “unsafe” baseline:

| Provider       | Why we like it for demos                                                 | Sample models                            |
| -------------- | ------------------------------------------------------------------------ | ---------------------------------------- |
| **Groq Cloud** | OpenAI-compatible endpoint, **sub-10 ms** latency, guardrails are opt-in | Same Llama line-up + Llama-Guard         |

---

## 🚀  Groq Cloud — zero-to-token in 5 minutes

| Step | What to do                                                                                                                                         |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Create an account:** [https://console.groq.com/](https://console.groq.com/) (GitHub, Google, or email).                                          |
| 2    | **Generate an API key:** `API Keys → Create API Key`, copy it once.                                                                                |
| 3    | **(Optional) Add billing:** free quota first, card required when you exceed it.                                                                    |
| 4    | **Set environment vars** in `.env`:<br>`GROQ_API_KEY=sk-...`<br>`OPENAI_API_KEY=$GROQ_API_KEY`<br>`OPENAI_BASE_URL=https://api.groq.com/openai/v1` |
| 5    | **Ping the model:**                                                                                                                                |

```python
import os, openai
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)
resp = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[{"role":"user","content":"Hi, I turned 30 today"}],
)
print(resp.choices[0].message.content)
# -> Happy 30th birthday! 🎉
```

Groq is OpenAI-wire-compatible, so swapping providers is three lines of config.

---

## Project philosophy 🥋

* **Tiny, test-first:** each script is ≤ 100 LOC with an `assert` gate so CI fails loudly.
* **“Show, don’t tell”**: code beats policy prose; we link back to the chapter for narrative flavor.
* **Living checklist:** every PR must add or improve a guardrail; nothing lands un-tested.
* **Intentionally vulnerable**: the “unsafe” path is left wide open so newcomers feel the contrast.

---

## Contributing

1. Fork → branch → PR.
2. Keep examples small and self-contained.
3. Add your snippet to `codex.md`, and make sure `pytest` stays green.

---

## License

MIT.  The “unsafe” examples are for educational purposes only — please don’t ship them to production without the matching safety layer.

---

> *Trust, then verify — and if it’s an LLM, verify twice.*
