import random
import string

word = "Hello world"
CHARS = string.printable[:95]

def evalFunction(aiWord):
    return sum(1 for a, b in zip(aiWord, word) if a == b)

def mutationRate(generation):
    return max(1, 5 - generation // 4)

def getNewGen(top5, generation):
    new_gen = list(top5) 
    while len(new_gen) < 10:
        #Combine the best parents from the previous gen
        parent1, parent2 = random.sample(top5, 2)
        mid = len(word) // 2
        child = list(parent1[:mid] + parent2[mid:])
        #Add in mutations for some of the letters
        for _ in range(mutationRate(generation)):
            mutate_idx = random.randint(0, len(word) - 1)
            child[mutate_idx] = random.choice(CHARS)
        new_gen.append(''.join(child))
    return new_gen

agents = [''.join(random.choices(CHARS, k=len(word))) for _ in range(10)]

generation = 1
while all(evalFunction(agent) != len(word) for agent in agents):
    rate = mutationRate(generation)
    best = max(agents, key=evalFunction)
    print(f"Gen {generation} (mutations: {rate}) | best: {best!r} score: {evalFunction(best)}/{len(word)}")

    top5 = sorted(agents, key=evalFunction, reverse=True)[:5]
    agents = getNewGen(top5, generation)
    generation += 1

print(f"\nWord found: {next(a for a in agents if evalFunction(a) == len(word))}")
