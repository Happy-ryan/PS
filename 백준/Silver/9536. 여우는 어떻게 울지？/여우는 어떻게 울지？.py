from collections import Counter

def solution(sounds, animals):
    x = Counter(sounds)
    for animal, sound in animals:
        if sound in x.keys():
            x.pop(sound)

    for s in sounds:
        if s in x.keys():
            print(s, end = ' ')

t = int(input())

for _ in range(t):
    sounds = list(input().split())
    animals = []
    while True:
        animal = input()
        if animal == 'what does the fox say?':
            break
        animal, goes, sound = animal.split()
        animals.append((animal, sound))

    solution(sounds, animals)