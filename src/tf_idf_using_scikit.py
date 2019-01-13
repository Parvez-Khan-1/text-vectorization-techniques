from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

text = ["The quick brown fox jumped over the lazy dog.",
        "The dog.",
        "The fox"]

vectorizer.fit(text)

print(vectorizer.vocabulary_)
print(vectorizer.idf_)

example_text = ['Dogs are very trustworthy animals']

# encode document
vector = vectorizer.transform([text[0]])

# summarize encoded vector
print(vector.shape)
print(vector.toarray())
