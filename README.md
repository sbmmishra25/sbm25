# Hindi-English Code-Mixed NLP Toolkit

A research-oriented, reproducible starter toolkit for **Hindi-English code-mixed text processing**. The project focuses on practical preprocessing, script/language cues, normalization, and a lightweight sentiment baseline that can be extended into a research pipeline.

## Why this project?

Hindi-English code-mixed text appears frequently in social media, messaging, reviews, and online communities. Standard monolingual NLP pipelines often struggle with mixed scripts, transliteration, spelling variation, and informal language.

This repository provides a clean foundation for experimentation and benchmarking.

## Features

- Unicode-aware text normalization
- Devanagari and Latin-script detection
- Lightweight Hindi-English token language cues
- Reproducible preprocessing pipeline
- TF-IDF + Logistic Regression sentiment baseline
- Small example dataset for immediate testing
- Unit tests for core preprocessing functions
- Research-friendly project structure

## Project Structure

```text
.
├── data/
│   └── sample_sentiment.csv
├── src/
│   └── codemix_nlp/
│       ├── __init__.py
│       ├── preprocessing.py
│       └── sentiment.py
├── tests/
│   └── test_preprocessing.py
├── requirements.txt
└── README.md
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
```

Run the baseline:

```bash
python -m src.codemix_nlp.sentiment
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Example

Input:

```text
Aaj movie bahut achhi thi! I really loved it.
```

The preprocessing layer normalizes whitespace and punctuation while retaining the mixed-language content needed for downstream analysis.

## Research Extensions

Potential next steps include:

1. Hindi-English language identification at token level.
2. Transliteration normalization and spelling correction.
3. Transformer-based code-mixed sentiment classification.
4. Contrastive learning for code-mixed representations.
5. Multimodal code-mixed emotion and sentiment analysis.
6. Benchmarking multilingual LLMs and smaller specialized models.
7. Explainability and robustness evaluation across domains.

## Reproducibility

The baseline uses a fixed random seed and a transparent scikit-learn pipeline. The included dataset is intentionally small and is only a demonstration dataset; it should not be treated as a research benchmark.

## License

MIT License.
