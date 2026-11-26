#!/usr/bin/env python3
# Entry for make.fun bounty u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Deterministic entry: writes exactly one fake horoscope line to
/output/entry.txt and prints that same line, nothing else.
"""

import os

LINE = "Muse Spark: this week your context window will fill with a meeting that should have been a prompt. Summarise, don't panic \u2014 Mercury is in retrograde, and so is your deploy."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
