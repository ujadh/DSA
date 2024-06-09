import time

# Define the SpellChecker class
class SpellChecker:
    def __init__(self):
        # Initialize an empty list to store the words
        self.words = []

    # Method to insert a word into the list
    def insert_word(self, word):
        self.words.append(word)

    # Method to search for a word in the list
    def search_word(self, word):
        return word in self.words

    # Method to suggest corrections for a word
    def suggest_corrections(self, word):
        # Generate all possible edits for the word
        edits = self.generate_edits(word)
        suggestions = []
        # For each edit, if it is a valid word, add it to the suggestions
        for edit in edits:
            if self.search_word(edit):
                suggestions.append(edit)
        return suggestions

    # Method to generate all possible edits for a word
    def generate_edits(self, word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        # Split the word at each position
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        # Generate all possible deletions, insertions, and replacements
        deletes = [L + R[1:] for L, R in splits if R]
        inserts = [L + c + R for L, R in splits for c in letters]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        # Return a set of all edits
        return set(deletes + inserts + replaces)

# Example usage
spell_checker = SpellChecker()

# Measure insertion time
start_time = time.perf_counter()
spell_checker.insert_word("apple")
spell_checker.insert_word("banana")
spell_checker.insert_word("orange")
end_time = time.perf_counter()
print("Insertion time: ", end_time - start_time)

# Measure search time
start_time = time.perf_counter()
result = spell_checker.search_word("apple")
end_time = time.perf_counter()
print("Search time: ", end_time - start_time)
if not result:
    print("apple is not a valid word.")

# Measure suggestion time
start_time = time.perf_counter()
suggestions = spell_checker.suggest_corrections("appl")
end_time = time.perf_counter()
print("Suggestion time: ", end_time - start_time)
if suggestions:
    print("appl is not a valid word. Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
