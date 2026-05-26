"""SMTP email delivery for generated Markdown digests."""

from __future__ import annotations

import logging
import smtplib
from email.message import EmailMessage
from html import escape
import re

logger = logging.getLogger(__name__)

_LINK_RE = re.compile(r"(https?://\S+)")
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def _inline_markdown_to_html(text: str) -> str:
    escaped = escape(text)
    escaped = _BOLD_RE.sub(r"<strong>\1</strong>", escaped)
    return _LINK_RE.sub(r'<a href="\1">\1</a>', escaped)


def _markdown_to_html(markdown: str) -> str:
    """Render the subset of Markdown used by digest files into email HTML."""
    body: list[str] = []
    in_list = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            body.append("</ul>")
            in_list = False

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line:
            close_list()
            continue
        if line == "---":
            close_list()
            body.append("<hr>")
            continue
        if line.startswith("#### "):
            close_list()
            body.append(f"<h4>{_inline_markdown_to_html(line[5:])}</h4>")
            continue
        if line.startswith("### "):
            close_list()
            body.append(f"<h3>{_inline_markdown_to_html(line[4:])}</h3>")
            continue
        if line.startswith("## "):
            close_list()
            body.append(f"<h2>{_inline_markdown_to_html(line[3:])}</h2>")
            continue
        if line.startswith("# "):
            close_list()
            body.append(f"<h1>{_inline_markdown_to_html(line[2:])}</h1>")
            continue
        if line.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{_inline_markdown_to_html(line[2:])}</li>")
            continue

        close_list()
        body.append(f"<p>{_inline_markdown_to_html(line)}</p>")

    close_list()
    return "\n".join(body)


def _html_document(markdown: str) -> str:
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      margin: 0;
      padding: 24px;
      background: #f6f8fa;
      color: #24292f;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.6;
    }}
    .container {{
      max-width: 860px;
      margin: 0 auto;
      padding: 24px;
      background: #ffffff;
      border: 1px solid #d0d7de;
      border-radius: 8px;
    }}
    h1, h2, h3, h4 {{
      color: #0f172a;
      line-height: 1.3;
    }}
    h1 {{ font-size: 24px; }}
    h2 {{ font-size: 20px; margin-top: 24px; }}
    h3 {{ font-size: 17px; margin-top: 22px; }}
    h4 {{ font-size: 15px; margin-top: 18px; }}
    p {{ margin: 8px 0; }}
    a {{ color: #0969da; }}
    hr {{
      border: 0;
      border-top: 1px solid #d8dee4;
      margin: 24px 0;
    }}
  </style>
</head>
<body>
  <div class="container">
    {_markdown_to_html(markdown)}
  </div>
</body>
</html>"""


def _missing_email_config(
    *,
    recipients: list[str],
    smtp_host: str,
    email_from: str,
) -> list[str]:
    missing: list[str] = []
    if not recipients:
        missing.append("EMAIL_RECIPIENTS")
    if not smtp_host:
        missing.append("SMTP_HOST")
    if not email_from:
        missing.append("EMAIL_FROM or SMTP_USERNAME")
    return missing


def send_markdown_email(
    *,
    subject: str,
    markdown: str,
    attachment_name: str,
    recipients: list[str],
    email_from: str,
    smtp_host: str,
    smtp_port: int,
    smtp_username: str = "",
    smtp_password: str = "",
    use_tls: bool = True,
    use_ssl: bool = False,
) -> bool:
    """Send a Markdown digest as HTML email body plus a Markdown attachment.

    Returns False when email is disabled or configuration is incomplete. SMTP
    exceptions are allowed to propagate so the caller can decide whether they
    should be fatal.
    """
    missing = _missing_email_config(
        recipients=recipients,
        smtp_host=smtp_host,
        email_from=email_from,
    )
    if missing:
        logger.info("Skipping email delivery; missing config: %s", ", ".join(missing))
        return False

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = email_from
    message["To"] = ", ".join(recipients)
    message.set_content(
        "请查看附件中的 Markdown 摘要；支持 HTML 的邮箱客户端会显示格式化正文。\n\n"
        f"{markdown}",
        subtype="plain",
        charset="utf-8",
    )
    message.add_alternative(_html_document(markdown), subtype="html", charset="utf-8")
    message.add_attachment(
        markdown.encode("utf-8"),
        maintype="text",
        subtype="markdown",
        filename=attachment_name,
    )

    if use_ssl:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
            if smtp_username or smtp_password:
                server.login(smtp_username, smtp_password)
            server.send_message(message)
    else:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.ehlo()
            if use_tls:
                server.starttls()
                server.ehlo()
            if smtp_username or smtp_password:
                server.login(smtp_username, smtp_password)
            server.send_message(message)

    logger.info("Sent digest email to %d recipients", len(recipients))
    return True
