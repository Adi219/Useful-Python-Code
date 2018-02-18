import random


## Returns either a or b
def between2(a, b):
    return min(a, b) + (random.randint(0, 1) * (max(a, b) - min(a, b)))

## Returns a random number between +a and -a except 0
def plusminusset(a):
    return random.randint(1, a) * ((random.randint(0, 1) * 2) - 1)

## Returns either +a or -a
def plusminusnum(a):
    return a * ((random.randint(0, 1) * 2) - 1)

## Returns either a, b or c when b-a = c-b
def between3equallyspaced(a, b, c):
    return a + (random.randint(0, 2) * (b-a))
