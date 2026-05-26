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
4. Sends every fresh matching abstract to an OpenAI-compatible chat completions
   endpoint to produce concise 2-3 sentence Chinese summaries. Set
   `MAX_PAPERS` above `0` only if you want a daily cap.
5. Appends the day's digest to `digest/digest.md`, a running log you can
   read like a journal.
6. Overwrites [`digest/latest.md`](digest/latest.md) with just today's
   entries. Useful for any external consumer that wants a small,
   stable file to pull from.
7. Archives the daily digest as `digest/archive/daily/YYYY-MM-DD.md`.
8. Emails the daily Markdown file to `EMAIL_RECIPIENTS` if email is configured.
9. On Mondays, writes a Chinese summary for the previous completed ISO week to
   `digest/weekly.md` and `digest/latest_weekly.md`.
10. Archives and emails the weekly summary as
   `digest/archive/weekly/YYYY-MM-DD_to_YYYY-MM-DD.md`.
11. On the first day of each month, writes a Chinese summary for the previous
   completed calendar month to `digest/monthly.md` and
   `digest/latest_monthly.md`.
12. Archives and emails the monthly summary as `digest/archive/monthly/YYYY-MM.md`.
13. Commits and pushes the changes back to `main`. If everything in the
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
4. **Optional email delivery**: set these repository secrets:
   - `EMAIL_RECIPIENTS`: comma-separated list such as
     `alice@example.com,bob@example.com`.
   - `EMAIL_FROM`: sender address, for example `ArXiv Digest <digest@example.com>`.
   - `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`.
   - `SMTP_USE_TLS` or `SMTP_USE_SSL` if your provider needs non-default values.
5. **Enable GitHub Actions** for the fork (Settings → Actions → General →
   *Allow all actions*). Forks have Actions disabled by default.
6. Make sure the workflow has write access. With the default setting
   `permissions: contents: write` already in the workflow file, the
   built-in `GITHUB_TOKEN` is sufficient (no PAT required).
7. (Optional) Trigger a first run manually: **Actions → Daily ArXiv Digest
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

To test email delivery with a Chinese sample digest, run:

```bash
python main.py --mode email-test --email-to 1102643651@qq.com
```

To test both the AI endpoint and email delivery, run:

```bash
python main.py --mode ai-email-test --email-to 1102643651@qq.com
```

## Safe arXiv metadata crawling

The crawler uses the official arXiv Atom API through `httpx`; it does not use
the Python `arxiv` package and it does not download PDFs. Metadata is cached in
SQLite at `digest/arxiv_metadata.sqlite3` and de-duplicated by arXiv id.

The arXiv API client is intentionally conservative:

- One HTTP connection is used for arXiv.
- Requests are never parallelized.
- Each arXiv API request waits at least `3.5s` plus random jitter by default.
- HTTP `429`, `500`, `502`, `503`, and `504` are retried.
- `Retry-After` is respected when present.
- Otherwise retries use exponential backoff from `30s` up to `10min`, with
  random `0-10s` jitter.
- Retries are bounded by `ARXIV_MAX_RETRIES`, default `5`.

Fetch metadata for a query:

```bash
python main.py fetch \
  --query "cat:q-bio.* OR cat:cs.LG OR cat:cs.AI" \
  --max-results 100
```

Fetch only recent submitted or updated papers:

```bash
python main.py fetch-daily --days 1
```

Use a custom metadata database:

```bash
python main.py fetch-daily --days 1 --db digest/my_arxiv_cache.sqlite3
```

Run the crawler tests:

```bash
python -m unittest discover -v
```

Set a real contact address in your User-Agent before running on a server:

```env
ARXIV_USER_AGENT=LongReadPaperBot/0.1 (mailto:you@example.com)
ARXIV_RATE_LIMIT_SECONDS=3.5
ARXIV_RATE_LIMIT_JITTER_SECONDS=1.5
ARXIV_MAX_RETRIES=5
```

## Linux server deployment

On a Linux server, install Python and clone the project:

```bash
sudo apt update
sudo apt install -y git python3 python3-venv

cd /opt
sudo git clone https://github.com/<you>/ArXic-AI-Paper-Digest-Agent.git
sudo chown -R "$USER:$USER" ArXic-AI-Paper-Digest-Agent
cd ArXic-AI-Paper-Digest-Agent

python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Create `.env` on the server and keep it private:

```bash
cp .env.example .env
chmod 600 .env
nano .env
```

Required `.env` values:

```env
API_KEY=your-openai-compatible-api-key
BASE_URL=https://your-provider.example/v1
OPENAI_MODEL=auto

ARXIV_CATEGORIES=cs.AI,cs.LG,stat.ML,q-bio.QM,q-bio.GN
ARXIV_TOPIC_KEYWORDS=deep learning,bioinformatics,genomics,protein,foundation model
MAX_PAPERS=0
ARXIV_PAGE_SIZE=300

EMAIL_RECIPIENTS=recipient1@example.com,recipient2@example.com
EMAIL_FROM=your_sender@example.com
SMTP_HOST=smtp.example.com
SMTP_PORT=465
SMTP_USERNAME=your_sender@example.com
SMTP_PASSWORD=your-smtp-app-password
SMTP_USE_SSL=true
SMTP_USE_TLS=false
```

For QQ Mail as the sender, use `smtp.qq.com`, port `465`, SSL enabled, and the
QQ Mail SMTP authorization code rather than your account password.

Run one deployment test that uses AI and sends an email:

```bash
.venv/bin/python main.py --mode ai-email-test --email-to 1102643651@qq.com
```

If the test succeeds, schedule the digest with cron:

```bash
mkdir -p logs
crontab -e
```

Add this entry to run every day at 09:00 UTC:

```cron
CRON_TZ=UTC
0 9 * * * cd /opt/ArXic-AI-Paper-Digest-Agent && .venv/bin/python main.py >> logs/digest.log 2>&1
```

The daily run also creates weekly summaries on Mondays and monthly summaries on
the first day of each month. If GitHub Actions is still enabled for the same
repo, disable either the server cron job or the GitHub schedule to avoid
duplicate emails.

## Configuration

All tuneable values live in [`config.py`](config.py) and may be overridden
by environment variables (see `.env.example`):

| Setting              | Default                  | Description                                       |
| -------------------- | ------------------------ | ------------------------------------------------- |
| `ARXIV_CATEGORIES`   | `cs.AI, cs.LG, stat.ML, q-bio.QM, q-bio.GN` | ArXiv categories to monitor. |
| `ARXIV_TOPIC_KEYWORDS` | AI/deep learning/bioinformatics terms | User-chosen topic filter applied after fetching. |
| `MAX_PAPERS`         | `0`                      | `0` means all fresh matching papers; positive values cap daily summaries. |
| `ARXIV_PAGE_SIZE`    | `200`                    | How many recent ArXiv results to inspect before filtering. |
| `ARXIV_USER_AGENT`   | `LongReadPaperBot/0.1 (mailto:YOUR_EMAIL@example.com)` | Contactable User-Agent for arXiv API requests. |
| `ARXIV_RATE_LIMIT_SECONDS` | `3.5`              | Minimum delay between arXiv API requests.         |
| `ARXIV_RATE_LIMIT_JITTER_SECONDS` | `1.5`       | Random extra delay added to the rate limit.       |
| `ARXIV_MAX_RETRIES`  | `5`                      | Retry count for transient arXiv API failures.     |
| `OPENAI_MODEL`       | `auto`                   | `auto` lists provider models and tries stronger chat models first, e.g. GPT-5.5 before smaller fallbacks. |
| `OPENAI_MAX_TOKENS`  | `300`                    | Max tokens per summary.                           |
| `API_KEY`            | required                 | API key for OpenAI or a compatible provider.      |
| `BASE_URL`           | unset                    | Optional OpenAI-compatible API base URL.          |
| `ROLLUP_MAX_TOKENS`  | `1200`                   | Max tokens for weekly/monthly summaries.          |
| `ENABLE_WEEKLY_SUMMARY` | `true`                | Generate previous-week rollups on Mondays.        |
| `ENABLE_MONTHLY_SUMMARY` | `true`               | Generate previous-month rollups on day 1.         |
| `EMAIL_RECIPIENTS`   | unset                    | Comma-separated email list; empty disables email. |
| `EMAIL_FROM`         | `SMTP_USERNAME`          | Sender address for digest emails.                 |
| `SMTP_HOST`          | unset                    | SMTP server host.                                 |
| `SMTP_PORT`          | `587` or `465`           | SMTP server port.                                 |
| `SMTP_USERNAME`      | unset                    | SMTP login username.                              |
| `SMTP_PASSWORD`      | unset                    | SMTP login password or app password.              |
| `SMTP_USE_TLS`       | `true`                   | Use STARTTLS for SMTP.                            |
| `SMTP_USE_SSL`       | `false`                  | Use SMTP over SSL.                                |
| `EMAIL_SEND_DAILY`   | `true`                   | Send daily digest emails.                         |
| `EMAIL_SEND_WEEKLY`  | `true`                   | Send weekly summary emails.                       |
| `EMAIL_SEND_MONTHLY` | `true`                   | Send monthly summary emails.                      |

The bot first pulls the newest `ARXIV_PAGE_SIZE` records from the configured
ArXiv categories, then keeps records whose title/abstract matches
`ARXIV_TOPIC_KEYWORDS`, then removes papers already present in
`digest/digest.md`. With the default `MAX_PAPERS=0`, every remaining fresh
matching paper is summarised. Increase `ARXIV_PAGE_SIZE` when your chosen
topics are broad, or set `MAX_PAPERS` to a positive number if you want to cap
cost and email length.

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

Cost scales with the number of fresh matching papers. With `MAX_PAPERS=0`, a
broad topic can send many abstracts to the model in one run. To control cost,
use narrower `ARXIV_TOPIC_KEYWORDS`, lower `ARXIV_PAGE_SIZE`, or set a positive
`MAX_PAPERS`. ArXiv API access is free.

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
│   ├── arxiv_client.py        # rate-limited arXiv HTTP client
│   ├── storage.py             # SQLite metadata cache
│   ├── emailer.py             # SMTP delivery for Markdown digests
│   ├── summariser.py          # OpenAI API calls
│   ├── rollup.py              # weekly/monthly digest history parsing
│   ├── writer.py              # markdown rendering and file I/O
│   └── models.py              # Pydantic models: Paper, DigestEntry, Digest
├── main.py                    # orchestrator entry point
├── config.py                  # tuneable settings
├── tests/                     # unit tests for crawler/client/storage
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
