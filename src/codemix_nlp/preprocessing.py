"""Preprocessing utilities for Hindi-English code-mixed text."""

import re


def normalize_text(text: str) -> str:
    """Normalize whitespace and common punctuation without removing script information."""
    text = str(text).strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"([!?.,])\1+", r"\1", text)
    return text


def script_ratio(text: str) -> dict[str, float]:
    """Return approximate Devanagari and Latin character ratios."""
    chars = [c for c in str(text) if c.isalpha()]
    if not chars:
        return {"devanagari": 0.0, "latin": 0.0, "other": 0.0}

    devanagari = sum("\u0900" <= c <= "\u097f" for c in chars)
    latin = sum(("a" <= c.lower() <= "z") for c in chars)
    other = len(chars) - devanagari - latin
    total = len(chars)
    return {
        "devanagari": devanagari / total,
        "latin": latin / total,
        "other": other / total,
    }


if __name__ == "__main__":
    sample = "Aaj movie bahut achhi thi!!!  I really loved it."
    print(normalize_text(sample))
    print(script_ratio(sample))
