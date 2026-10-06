"""
CodeAlpha — Task 3: Task Automation
Extracts email addresses from a .txt file and saves them to another file.
Key concepts: re, file handling.
"""

import re
from pathlib import Path

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def extract_emails(source_path, dest_path):
    text = Path(source_path).read_text(encoding="utf-8")
    emails = sorted(set(EMAIL_PATTERN.findall(text)))
    Path(dest_path).write_text("\n".join(emails) + ("\n" if emails else ""), encoding="utf-8")
    return emails


def main():
    source = input("Source .txt file [sample_input.txt]: ").strip() or "sample_input.txt"
    dest = input("Output file [emails.txt]: ").strip() or "emails.txt"
    if not Path(source).exists():
        print(f"File not found: {source}")
        return
    emails = extract_emails(source, dest)
    print(f"Found {len(emails)} unique email(s). Saved to {dest}")
    for email in emails:
        print(" -", email)


if __name__ == "__main__":
    main()
