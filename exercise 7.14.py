class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern

    def isCompatible(self, guesses, scores):
        for guess, score in zip(guesses, scores):
            if self.calculateScore(guess) != score:
                return False
        return True

    def calculateScore(self, guess):
        return 1 if self.pattern == guess else 0

# Pattern sınıfını oluşturun
pattern = Pattern("abc")

# Tahminler ve skorlar listesini oluşturun
guesses = ["abc", "def", "abc"]
scores = [1, 0, 1]

# isCompatible metodunu çağırın
result = pattern.isCompatible(guesses, scores)

# Sonucu yazdırın
print(result)
