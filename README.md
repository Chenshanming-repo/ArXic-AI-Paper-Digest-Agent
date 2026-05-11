# ArXiv AI Paper Digest Bot

An automated daily digest of new ArXiv papers in your favourite categories,
summarised by an OpenAI model and committed straight back to this repository.

The whole thing runs on GitHub Actions. There is no server to host, no
database to maintain, and no infrastructure to pay for beyond a small
OpenAI API bill.

## What it does

Every day at **09:00 UTC**, a scheduled GitHub Action:

1. Queries the [ArXiv API](https://info.arxiv.org/help/api/index.html) for
   the most recent papers in the configured categories
   (defaults: `cs.AI`, `cs.LG`, `cs.CL`).
2. Filters down to papers submitted in the last 24 hours.
3. Sends each abstract to OpenAI (`gpt-4o-mini` by default) to produce a
   concise 2–3 sentence plain-English summary.
4. Appends the day's digest to [`digest/digest.md`](digest/digest.md), a
   running log you can read like a journal.
5. Overwrites [`digest/latest.md`](digest/latest.md) with just today's
   entries. Useful for any external consumer that wants a small,
   stable file to pull from.
6. Commits and pushes the changes back to `main`. If there is nothing new
   (e.g. quiet weekends, ArXiv outage), the run exits cleanly and creates
   no commit.

## Setup

1. **Fork or clone** this repository into your own GitHub account.
2. **Add your OpenAI API key** as a repository secret:
   - Go to **Settings → Secrets and variables → Actions → New repository secret**.
   - Name: `OPENAI_API_KEY`
   - Value: your key from <https://platform.openai.com/api-keys>
3. **Enable GitHub Actions** for the fork (Settings → Actions → General →
   *Allow all actions*). Forks have Actions disabled by default.
4. Make sure the workflow has write access. With the default setting
   `permissions: contents: write` already in the workflow file, the
   built-in `GITHUB_TOKEN` is sufficient (no PAT required).
5. (Optional) Trigger a first run manually: **Actions → Daily ArXiv Digest
   → Run workflow**.

That's it. The Action will run every day at 09:00 UTC and update the digest
files in place.

## Running locally

If you want to test changes or generate a digest on demand:

```bash
git clone https://github.com/<you>/arxiv-digest.git
cd arxiv-digest

python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# edit .env and paste your OPENAI_API_KEY

python main.py
```

The local run writes to the same files (`digest/digest.md` and
`digest/latest.md`) the Action does.

## Configuration

All tuneable values live in [`config.py`](config.py) and may be overridden
by environment variables (see `.env.example`):

| Setting              | Default                  | Description                                       |
| -------------------- | ------------------------ | ------------------------------------------------- |
| `CATEGORIES`         | `cs.AI, cs.LG, cs.CL`    | ArXiv categories to monitor.                      |
| `MAX_PAPERS`         | `10`                     | Maximum papers summarised per day.                |
| `LOOKBACK_HOURS`     | `24`                     | Only include papers submitted within this window. |
| `ARXIV_PAGE_SIZE`    | `50`                     | How many results to pull from ArXiv per query.    |
| `OPENAI_MODEL`       | `gpt-4o-mini`            | OpenAI model used for summaries.                  |
| `OPENAI_MAX_TOKENS`  | `300`                    | Max tokens per summary.                           |

## Example output

A daily entry in `digest/digest.md` looks like this:

```markdown
---
## 2026-05-11

### 1. Scalable Tool-Use Reasoning with Self-Improving Agents
**Authors:** Jane Doe, John Smith, Wei Chen
**Link:** https://arxiv.org/abs/2605.01234v1
**Summary:** This paper tackles the difficulty of teaching language model agents to chain together many tool calls reliably. The authors introduce a self-improvement loop where an agent critiques and edits its own trajectories before retraining, leading to a 14-point gain on a multi-step benchmark over a strong baseline.

### 2. Sparse Mixture-of-Depths for Efficient Long-Context Inference
**Authors:** Aiden Park, Maya Iyer
**Link:** https://arxiv.org/abs/2605.01345v1
**Summary:** Long-context transformers waste compute on tokens that do not need deep processing. The authors propose a sparse mixture-of-depths router that skips most layers for "easy" tokens, achieving comparable perplexity at 40% lower FLOPs on 128k-token sequences.
```

## Cost

At the default of 10 papers/day with `gpt-4o-mini`, this costs roughly
**$0.01–0.02 per day** (approximately $4–7/year). Bumping `MAX_PAPERS` or
switching to a larger model (e.g. `gpt-4o`) will scale costs roughly
linearly. ArXiv API access is free.

## Project structure

```
arxiv-digest/
├── .github/
│   └── workflows/
│       └── daily_digest.yml   # scheduled GitHub Action
├── digest/
│   ├── digest.md              # append-only running log
│   └── latest.md              # today only, overwritten daily
├── src/
│   ├── fetcher.py             # ArXiv API + Atom XML parsing
│   ├── summariser.py          # OpenAI API calls
│   ├── writer.py              # markdown rendering and file I/O
│   └── models.py              # Pydantic models: Paper, DigestEntry, Digest
├── main.py                    # orchestrator entry point
├── config.py                  # tuneable settings
├── requirements.txt
└── .env.example
```

## Error handling

- **No new papers** (e.g. quiet weekend): logs a message and exits cleanly.
  No commit is created.
- **A single OpenAI call fails**: that paper is skipped, the error is
  logged, and the rest of the digest still ships.
- **A fatal error** (missing API key, ArXiv unreachable, malformed XML):
  the script exits with code 1 so the Action shows up red instead of
  silently green.

## License

MIT. See [`LICENSE`](LICENSE) if present, or feel free to add one.
