import random

def generate(length):

    return [random.getrandbits(1) for x in range(length)]

print(generate(5))
print([random.randint(0,1) for x in range(20)])