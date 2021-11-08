import os
from nltk import ngrams
from collections import Counter

def test2():
    result = []
    for file in os.listdir("../txtfolder"):
       with open(os.path.join("../txtfolder", file), 'r') as f:
        sentence = f.read().rstrip()

    # Since you are not considering periods and treats words with - as phrases
    sentence = sentence.replace('.', '').replace('-', ' ')

    for n in range(len(sentence.split(' ')), 1, -1):
        phrases = []

        for token in ngrams(sentence.split(), n):
            phrases.append(' '.join(token))

        phrase, freq = Counter(phrases).most_common(1)[0]
        if freq > 1:
            result.append((phrase, n))
            sentence = sentence.replace(phrase, '')

    for phrase, freq in result:
        print('%s: %d' % (phrase, freq))    
    
if __name__ == '__main__':
    
    # test()
    test2()
    # trying()