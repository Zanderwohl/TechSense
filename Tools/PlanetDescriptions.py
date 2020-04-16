import random
import LocationNames


def create_forest(file_name):
    forest = {}
    lines = None
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()

    current_list = None
    for line in lines:
        if len(line) > 0:
            if line[0] == '-':
                current_list = line[1:]
                if forest.get(current_list) is None:
                    forest[current_list] = []
            elif line[0] == '#':
                pass
            else:
                forest[current_list].append(line)
    return forest


def find_symbol(text):
    for i in range(len(text)):
        char = text[i]
        if char == '[':
            return i
    return None


def find_close(text, index):
    for i in range(index, len(text)):
        char = text[i]
        if char == ']':
            return i
    return None


def find_keyword(paragraph, start, end):
    return paragraph[start+1:end]


def replace_keyword(paragraph, start, end, replacement):
    begin = paragraph[0:start]
    end = paragraph[end+1:]
    return begin + replacement + end


def choose_from_keyword(forest, keyword):
    item_list = forest[keyword]
    return random.choice(item_list)


def describe_planet(forest):
    name = LocationNames.generate_name()
    paragraph = forest['root'][0]
    next_symbol = find_symbol(paragraph)
    while next_symbol is not None:
        end = find_close(paragraph, next_symbol)
        keyword = find_keyword(paragraph, next_symbol, end)
        replacement = choose_from_keyword(forest, keyword)
        paragraph = replace_keyword(paragraph, next_symbol, end, replacement)
        next_symbol = find_symbol(paragraph)
    return name + '\n' + paragraph[0].upper() + paragraph[1:]


def generate(forest, n=1, seed=None):
    if seed is not None:
        random.seed(a=seed)
    if forest.get('root') is None:
        return 'There is no root in the forest given!'
    planets = []
    for i in range(n):
        planets.append(describe_planet(forest))
    return planets


if __name__ == '__main__':
    attribute_forest = create_forest('planet_attributes.txt')
    # print(attribute_forest)
    seed = input('Seed:')
    descriptions = generate(attribute_forest, n=1, seed=seed)
    for description in descriptions:
        print(description)
        print()
