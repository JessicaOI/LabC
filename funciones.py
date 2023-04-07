import regex


def parse_yalex(file_path):
    regular_definitions = {}

    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("let"):
                definition, expression = line.strip().split(" = ")
                definition = definition[4:]
                regular_definitions[definition] = expression

    return regular_definitions


def generate_automata(regular_definitions):
    automata = {}
    for token, definition in regular_definitions.items():
        automata[token] = regex.compile(definition)

    return automata


def automata_to_state_diagram(automata):
    state_diagrams = {}
    for token, pattern in automata.items():
        state_diagrams[token] = pattern.pattern

    return state_diagrams

