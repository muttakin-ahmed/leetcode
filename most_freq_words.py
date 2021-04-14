import re
from collections import defaultdict

def most_common_word(paragraph, banned):
    # replacing all punctuations with spaces and put all letters in lower case
    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
    # splitting all the string into words
    words = normalized_str.split()

    # initiating a default dictionary to keep track of which word is occuring how many times
    word_count = defaultdict(int)
    # Making sure that each banned word is only checked once
    banned_words = set(banned)
        
    # counting the appearances of each word excluding the banned words
    for word in words:
        if word not in banned_words:
                word_count[word] += 1
                
    # returning the word with highest frequency
    for key in list(word_count.keys()):
        if word_count[key] == max(list(word_count.values())):
            return key
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)
