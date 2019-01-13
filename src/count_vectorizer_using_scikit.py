from sklearn.feature_extraction.text import CountVectorizer

text = ['An apple a day keeps doctor away.',
        'Parvez likes to eat apples.',
        'Natural Language Processing is Fun.']

vectorizer = CountVectorizer(ngram_range=(1, 2))
vectorizer.fit(text)

print(vectorizer.vocabulary_)

test_example = ['I like apples']
vector = vectorizer.transform(test_example)
print(vector.toarray())