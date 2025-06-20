# AGENTS Instructions

These notes apply to the entire repository.

- **Keep `codex.md` updated.** Whenever an example script or related documentation changes, summarise the update in `codex.md`.
- **Check Python syntax.** Before committing, run:
  ```bash
  python3 -m py_compile examples/*.py
  ```
  to ensure all scripts compile.
- **Commit style.** Use short, present-tense commit messages (50 characters or less).
- **No secrets.** Do not commit API keys or other private data. `.env.example` contains placeholders for both `OPENAI_API_KEY` and `GROQ_API_KEY` used by `chatty.py` and the examples.
- **Configure keys.** Copy `.env.example` to `.env` and populate the key values before running `hello_world.py` or `test.py`.
