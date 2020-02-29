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
]


def generate_name(n=1):
    syllables_shuffled = syllables.copy()
    random.shuffle(syllables_shuffled)
    return syllables_shuffled[0] + syllables_shuffled[1]


if __name__ == "__main__":
    print(generate_name())
