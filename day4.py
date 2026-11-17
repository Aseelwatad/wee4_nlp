
import re


# Simple text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()


# Test 1: Lowercase
def test_lowercase():
    assert clean_text("HELLO") == "hello"


# Test 2: Remove punctuation
def test_punctuation():
    assert clean_text("Hello!!!") == "hello"


# Test 3: Empty text
def test_empty_text():
    assert clean_text("") == ""


# Test 4: Remove numbers
def test_numbers():
    assert clean_text("Python123") == "python"


# Test 5: Normal text
def test_normal_text():
    assert clean_text("Hello World") == "hello world"
