"""SMTP email delivery for generated Markdown digests."""

from __future__ import annotations

import logging
import smtplib
from email.message import EmailMessage

logger = logging.getLogger(__name__)


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
    """Send a Markdown digest as both email body text and an attachment.

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
        "请查看下面的 Markdown 摘要，附件中也包含同一份 .md 文件。\n\n"
        f"{markdown}",
        subtype="plain",
        charset="utf-8",
    )
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
