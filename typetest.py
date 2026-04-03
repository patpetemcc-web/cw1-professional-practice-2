import json
import random

def load_bank(filename="wordbank.json"):
    with open(filename, "r") as f:
        return json.load(f)
    
class SentenceLoader:
    def __init__(self, word_bank, difficulty="Easy"):
        self.word_bank = word_bank
        self.difficulty = difficulty
        self.used = set()
    
    def get_sentence(self):
        available = list(set(self.word_bank[self.difficulty]) - self.used)

        if not available:
            self.used.clear()
            available = self.word_bank[self.difficulty]

        sentence = random.choice(available)
        self.used.add(sentence)
        return sentence

def sentence():
    word_bank = load_bank("wordbank.json")
    manager = SentenceLoader(word_bank, "Easy")
    return manager.get_sentence()