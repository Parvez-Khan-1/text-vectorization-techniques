import copy
import math

documents = ['this is a sample',
             'this is another example']

# Step 1: Create a vocabulary of all unique words in documents
vocabulary = dict()
for doc in documents:
    unique_words = set(doc.split())
    for word in unique_words:
        vocabulary[word] = 0

# Step 2: Create Word Count Dict for each document
all_word_count_dict = []
for doc in documents:
    word_count_dict = copy.copy(vocabulary)
    word_tokens = doc.split()
    for word in word_tokens:
        word_count_dict[word] +=1
    all_word_count_dict.append(word_count_dict)


# Step 3: Calculate Term Frequency (TF)
# Formula TF = (No.of Times Term t occurred in document / total no.of terms in a document)
all_term_frequencies = list()
for idx, word_count_dict in enumerate(all_word_count_dict):
    tf_dict = dict()
    bag_of_words = documents[idx].split()
    bowCount = len(bag_of_words)
    for word, count in word_count_dict.items():
        tf_dict[word] = count / float(bowCount)
    all_term_frequencies.append(tf_dict)

# Step 4: Calculate Inverse Document Frequencies (IDF)
N = len(all_term_frequencies)
idf_dict = dict.fromkeys(all_term_frequencies[0].keys(), 0.00000001)

for document_frequency in all_term_frequencies:
    for word, count in document_frequency.items():
        if count > 0:
            idf_dict[word] += 1

    for word, val in idf_dict.items():
        idf_dict[word] = math.log10(N / float(val))


# Step 5: Calculate TF-IDF
all_tf_idf = dict()
for idx, term_freq in enumerate(all_term_frequencies):
    tf_idf = dict()
    for word, val in term_freq.items():
        tf_idf[word] = val * idf_dict[word]
    all_tf_idf[documents[idx]] = tf_idf


print(all_tf_idf)