from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
texts = [
    "Breaking news president signs new law",
    "Scientists discovered new species",
    "Aliens landed in India yesterday",
    "Click here to win money now",
]

labels = ["REAL", "REAL", "FAKE", "FAKE"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_news(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    confidence = max(model.predict_proba(text_vector)[0]) * 100
    return prediction, round(confidence, 2)