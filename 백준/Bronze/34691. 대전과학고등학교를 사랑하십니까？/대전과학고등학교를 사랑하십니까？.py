mapping = {
    "animal": "Panthera tigris",
    "tree": "Pinus densiflora",
    "flower": "Forsythia koreana"
}

while True:
    key = input()
    if key == "end":
        break
    print(mapping[key])