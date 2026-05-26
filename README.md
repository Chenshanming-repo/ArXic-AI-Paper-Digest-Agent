# ArXiv AI/Bioinformatics Paper Digest Bot

An automated daily digest of new AI, deep learning, and bioinformatics ArXiv
papers, summarised in Chinese by an OpenAI-compatible model and committed
straight back to this repository.

The whole thing runs on GitHub Actions. There is no server to host, no
database to maintain, and no infrastructure to pay for beyond a small model
API bill.

## What it does

Every day at **09:00 UTC**, a scheduled GitHub Action:

1. Queries the [ArXiv API](https://info.arxiv.org/help/api/index.html) for
   the most recent submissions in the configured categories
   (defaults: `cs.AI`, `cs.LG`, `stat.ML`, `q-bio.QM`, `q-bio.GN`), sorted
   newest first.
2. Filters those results by configurable topic keywords for AI, deep learning,
   and bioinformatics.
3. Drops any paper whose ArXiv id already appears in
   [`digest/digest.md`](digest/digest.md), so the same paper is never
   summarised twice.
4. Sends up to `MAX_PAPERS` abstracts (default 10) to an OpenAI-compatible
   chat completions endpoint to produce concise 2-3 sentence Chinese summaries.
5. Appends the day's digest to `digest/digest.md`, a running log you can
   read like a journal.
6. Overwrites [`digest/latest.md`](digest/latest.md) with just today's
   entries. Useful for any external consumer that wants a small,
   stable file to pull from.
7. Archives the daily digest as `digest/archive/daily/YYYY-MM-DD.md`.
8. On Mondays, writes a Chinese summary for the previous completed ISO week to
   `digest/weekly.md` and `digest/latest_weekly.md`.
9. Archives the weekly summary as
   `digest/archive/weekly/YYYY-MM-DD_to_YYYY-MM-DD.md`.
10. On the first day of each month, writes a Chinese summary for the previous
   completed calendar month to `digest/monthly.md` and
   `digest/latest_monthly.md`.
11. Archives the monthly summary as `digest/archive/monthly/YYYY-MM.md`.
12. Commits and pushes the changes back to `main`. If everything in the
   ArXiv response is already digested (e.g. quiet weekends or a re-run
   on the same day), the run exits cleanly and creates no commit.

## Setup

1. **Fork or clone** this repository into your own GitHub account.
2. **Add your API key** as a repository secret:
   - Go to **Settings → Secrets and variables → Actions → New repository secret**.
   - Name: `API_KEY`
   - Value: your OpenAI or third-party OpenAI-compatible API key.
3. **Optional third-party endpoint**: add another repository secret named
   `BASE_URL`, for example `https://api.example.com/v1`. Leave it unset to use
   the OpenAI SDK default endpoint.
4. **Enable GitHub Actions** for the fork (Settings → Actions → General →
   *Allow all actions*). Forks have Actions disabled by default.
5. Make sure the workflow has write access. With the default setting
   `permissions: contents: write` already in the workflow file, the
   built-in `GITHUB_TOKEN` is sufficient (no PAT required).
6. (Optional) Trigger a first run manually: **Actions → Daily ArXiv Digest
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
# edit .env and paste your API_KEY, plus BASE_URL if needed

python main.py
```

The local run writes to the same files (`digest/digest.md`,
`digest/latest.md`, and `digest/archive/daily/`) the Action does.

To generate only a rollup locally, run `python main.py --mode weekly` or
`python main.py --mode monthly`. To force both rollups after a daily run, use
`python main.py --force-rollups`.

To split the existing historical `digest/digest.md` into per-day archive
files, run `python main.py --mode archive`.

## Configuration

All tuneable values live in [`config.py`](config.py) and may be overridden
by environment variables (see `.env.example`):

| Setting              | Default                  | Description                                       |
| -------------------- | ------------------------ | ------------------------------------------------- |
| `ARXIV_CATEGORIES`   | `cs.AI, cs.LG, stat.ML, q-bio.QM, q-bio.GN` | ArXiv categories to monitor. |
| `ARXIV_TOPIC_KEYWORDS` | AI/deep learning/bioinformatics terms | Topic filter applied after fetching. |
| `MAX_PAPERS`         | `10`                     | Maximum papers summarised per run.                |
| `ARXIV_PAGE_SIZE`    | `50`                     | How many results to pull from ArXiv per query.    |
| `OPENAI_MODEL`       | `gpt-4o-mini`            | OpenAI model used for summaries.                  |
| `OPENAI_MAX_TOKENS`  | `300`                    | Max tokens per summary.                           |
| `API_KEY`            | required                 | API key for OpenAI or a compatible provider.      |
| `BASE_URL`           | unset                    | Optional OpenAI-compatible API base URL.          |
| `ROLLUP_MAX_TOKENS`  | `1200`                   | Max tokens for weekly/monthly summaries.          |
| `ENABLE_WEEKLY_SUMMARY` | `true`                | Generate previous-week rollups on Mondays.        |
| `ENABLE_MONTHLY_SUMMARY` | `true`               | Generate previous-month rollups on day 1.         |

The bot picks the top `MAX_PAPERS` papers by ArXiv submission date that it
has not summarised before. `ARXIV_PAGE_SIZE` should be larger than
`MAX_PAPERS` to give the dedup step a healthy pool to choose from on busy
days.

## Example output

A daily entry in `digest/digest.md` looks like this:

```markdown
---
## 2026-05-11

### 1. Scalable Tool-Use Reasoning with Self-Improving Agents
**作者:** Jane Doe, John Smith, Wei Chen
**链接:** https://arxiv.org/abs/2605.01234v1
**摘要:** 这篇论文关注语言模型智能体难以稳定串联多步工具调用的问题。作者提出一种自我改进流程，让智能体先批判并修正自己的执行轨迹，再用改进后的数据继续训练，从而在多步任务基准上显著优于强基线。

### 2. Sparse Mixture-of-Depths for Efficient Long-Context Inference
**作者:** Aiden Park, Maya Iyer
**链接:** https://arxiv.org/abs/2605.01345v1
**摘要:** 这篇论文针对长上下文 Transformer 在简单 token 上浪费计算的问题，提出稀疏的 mixture-of-depths 路由机制。该方法会让容易处理的 token 跳过大部分层，在 128k token 序列上以更低 FLOPs 获得接近的困惑度表现。
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
│   ├── latest.md              # today only, overwritten daily
│   ├── weekly.md              # append-only weekly rollups
│   ├── latest_weekly.md       # latest weekly rollup
│   ├── monthly.md             # append-only monthly rollups
│   ├── latest_monthly.md      # latest monthly rollup
│   └── archive/
│       ├── daily/             # one file per daily digest date
│       ├── weekly/            # one file per weekly summary range
│       └── monthly/           # one file per monthly summary
├── src/
│   ├── fetcher.py             # ArXiv API + Atom XML parsing
│   ├── summariser.py          # OpenAI API calls
│   ├── rollup.py              # weekly/monthly digest history parsing
│   ├── writer.py              # markdown rendering and file I/O
│   └── models.py              # Pydantic models: Paper, DigestEntry, Digest
├── main.py                    # orchestrator entry point
├── config.py                  # tuneable settings
├── requirements.txt
└── .env.example
```

## Error handling

- **No new papers** (e.g. all top-of-feed papers are already digested):
  logs a message and exits cleanly. No commit is created.
- **A single OpenAI call fails**: that paper is skipped, the error is
  logged, and the rest of the digest still ships.
- **A fatal error** (missing API key, ArXiv unreachable, malformed XML):
  the script exits with code 1 so the Action shows up red instead of
  silently green.

## License

MIT. See [`LICENSE`](LICENSE) if present, or feel free to add one.
