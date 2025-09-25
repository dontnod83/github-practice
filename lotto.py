import random

for i in range(10):
    lotto = random.sample(list(range(1,46)), 6)
    lotto.sort()
    print(lotto)