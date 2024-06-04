class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        return [candidate for candidate in candidates if sorted(candidate) == sorted(self.word)]
    

