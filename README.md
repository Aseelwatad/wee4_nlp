# Week 4 - Text Cleaning and Testing

## Overview
In Week 4, I practiced working with text data using Python. I learned how to clean text and prepare it for analysis. I also practiced using pytest to test simple text cleaning functions.

## Day 3 - Text Cleaning

In Day 3, I worked with sample customer reviews and applied different text cleaning techniques.

I used:
- **Regular Expressions (Regex):** To remove URLs, numbers, and special characters.
- **Tokenization:** To split text into individual words.
- **Stop Words Removal:** To remove common words like "the", "is", and "and".
- **Lemmatization:** To convert words to their base form.
- **spaCy:** To process text and apply tokenization and lemmatization.

The goal was to understand how text cleaning works and compare the text before and after cleaning.

## Day 4 - Testing with pytest

In Day 4, I practiced using pytest to check if a simple text cleaning function works correctly.

I created five tests to check:
- Converting uppercase text to lowercase.
- Removing punctuation.
- Handling empty text.
- Removing numbers.
- Cleaning normal text.

I used `assert` to compare the actual output with the expected output.

## How to Run

Install the required libraries:

```bash
pip install spacy pytest
python -m spacy download en_core_web_sm
```

Run the Day 3 code:

```bash
python "week4 dayy 3.py"
```

Run the Day 4 tests:

```bash
python -m pytest "test_text_cleaning.py" -v
```

## What I Learned

In these two days, I learned how to clean text using Python and spaCy, and how to use pytest to check if functions return the expected results.

I also learned that text cleaning should be done carefully because removing some words can change the meaning of a sentence.
