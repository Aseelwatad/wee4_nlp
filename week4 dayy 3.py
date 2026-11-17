
import re
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")


#  Clean text using Regular Expressions
def clean_with_regex(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


#  Tokenization
def tokenize_text(text):
    doc = nlp(text)
    return [token.text for token in doc]


#  Remove stop words
def remove_stopwords(text):
    doc = nlp(text)
    return [
        token.text for token in doc
        if not token.is_stop
    ]


#  Lemmatization
def lemmatize_text(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc]


#  Complete text cleaning
def clean_text(text):
    text = clean_with_regex(text)
    doc = nlp(text)

    cleaned_words = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_space
    ]

    return " ".join(cleaned_words)


# Sample customer reviews
reviews = [
    "The customers are RUNNING!!!",
    "I really loved the products!!!",
    "The delivery was very SLOW!!!",
    "These phones are working perfectly.",
    "Visit https://shop.com for more details!"
]


# Display results
for review in reviews:
    print("\nOriginal Text:", review)
    print("After Regex:", clean_with_regex(review))
    print("Tokens:", tokenize_text(clean_with_regex(review)))
    print("Without Stop Words:", remove_stopwords(clean_with_regex(review)))
    print("Lemmatization:", lemmatize_text(clean_with_regex(review)))
    print("Final Cleaned Text:", clean_text(review))
    print("-" * 50)
