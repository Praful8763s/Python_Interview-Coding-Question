from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

# Example usage
words = ["tea", "ate", "egg", "up", "own", "now", "pu"]
result = group_anagrams(words)
print(result)