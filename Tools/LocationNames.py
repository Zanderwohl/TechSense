import random


syllables = [
    "od",
    "streth",
    "mish",
    "nori",
    "nod",
    "perth",
    "peth",
    "derth",
    "det",
    "so",
    "slo",
    "hi",
    "ty",
    "kil",
    "fy",
    "aardt",
    "fyn",
    "kar",
    "heid",
    "ho",
    "kel",
    "chel",
    "mod",
    "ral",
    "ear",
    "the",
    "arth",
    "teth",
    "let",
    "dod",
]


def generate_name():
    syllables_shuffled = syllables.copy()
    random.shuffle(syllables_shuffled)
    name = syllables_shuffled[0] + syllables_shuffled[1]
    return name.capitalize()


def generate_names(n=1):
    names = []
    for i in range(n):
        if seed is not None:
            seed = seed + 1
        names.append(generate_name())
    return names


if __name__ == "__main__":
    names = generate_names(10)
    for name in names:
        print(name)
