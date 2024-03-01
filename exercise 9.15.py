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

class RobustPattern(Pattern):
    def isCompatible(self, guesses, scores):
        for guess, score in zip(guesses, scores):
            if self.calculateScore(guess) != score:
                return False
        return True




# Ardından, bir tahminler ve puanlar listesi oluşturun
guesses = ["ornek", "yanlis"]
scores = [1, 0]


# Aynı işlemi RobustPattern için de yapabiliriz
rp = RobustPattern("ornek")
print(rp.isCompatible(guesses, scores))  # Bu da True dönmelidir
