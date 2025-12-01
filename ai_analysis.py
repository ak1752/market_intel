from transformers import pipeline
import spacy

# Load models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
ner = spacy.load("en_core_web_lg")

def summarize_article(text):
    """Summarize article text."""
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def extract_entities(text):
    """Extract entities (companies, dates, etc.)."""
    doc = ner(text)
    entities = []
    for ent in doc.ents:
        entities.append({"text": ent.text, "label": ent.label_})
    return entities

def categorize_article(text):
    """Categorize article (e.g., M&A, PESTEL)."""
    # Mockup: Use keyword matching for simplicity
    keywords = {
        "M&A": ["acquire", "merger", "acquisition"],
        "PESTEL": ["regulation", "policy", "funding"],
        "Product Launch": ["launch", "release", "new product"]
    }
    for category, terms in keywords.items():
        if any(term in text.lower() for term in terms):
            return category
    return "Other"
