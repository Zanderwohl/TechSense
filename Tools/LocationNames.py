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
    "the"
]


def generate_name():
    syllables_shuffled = syllables.copy()
    random.shuffle(syllables_shuffled)
    return syllables_shuffled[0] + syllables_shuffled[1]


def generate_names(n=1):
    names = []
    for i in range(n):
        names.append(generate_name())
    return names


if __name__ == "__main__":
    print(generate_names(10))
