"""
This is simple and from scratch implementation of Bag of Words (One hot encoding)
"""


# Get a list of unique words which we call vocabulary
def generate_vocabulary(data_set):
    vocabulary = set()
    for sentence in data_set:
        vocabulary.update(str(sentence).lower().split())
    return vocabulary


# Generate bag_of_words vectors for training_data
def generate_feature_vector(vocabulary, data_set):
    feature_vectors = []
    for sentence in data_set:
        word_tokens = str(sentence).lower().split()
        vector = lambda x: [1 if word_in_vocab in word_tokens else 0 for word_in_vocab in vocabulary]
        feature_vectors.append(vector(vocabulary))
    return feature_vectors


if __name__ == '__main__':
    # Training examples
    training_data = ['My frineds are like apples',
                     'Parvez likes apples',
                     'It was the best time we had',
                     'Almost all peoples likes apples',
                     'Doctor always suggest to eat apples']

    # Test Example
    test_data = ['Apples are very good for health',
                 'An Apple a day keep doctors away']

    vocabulary = generate_vocabulary(training_data)
    print("Length of Vocabulary : ", len(vocabulary))

    train_feature_vectors = generate_feature_vector(vocabulary, training_data)
    test_feature_vectors = generate_feature_vector(vocabulary, test_data)
    print("Training Feature Vectors : \n", train_feature_vectors)
    print("Test Feature Vectors : \n", test_feature_vectors)
