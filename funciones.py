from classAutomata import Automata


def parse_yalex(file_path):
    regular_definitions = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):  # Ignora líneas vacías y comentarios
                continue

            token, regex = line.split(maxsplit=1)
            regular_definitions.append((token, regex))

    return regular_definitions


def generate_automata(regular_definitions):
    automata = {}

    for token, regex in regular_definitions:
        stack = []

        for char in regex:
            if char not in {'·', '|', '*'}:  # Operando
                new_automata = Automata()
                state1 = len(new_automata.states) + 1
                state2 = state1 + 1
                new_automata.add_state(state1)
                new_automata.add_state(state2)
                new_automata.set_start_state(state1)
                new_automata.add_final_state(state2)
                new_automata.add_transition(state1, state2, char)
                stack.append(new_automata)
            elif char == '·':  # Concatenación
                b = stack.pop()
                a = stack.pop()
                a.add_final_state(a.start_state)
                for s, t in b.transitions.items():
                    if s not in a.states:
                        a.add_state(s)
                    a.transitions[s] = t
                for s in b.final_states:
                    a.add_final_state(s)
                stack.append(a)
            elif char == '|':  # Unión
                b = stack.pop()
                a = stack.pop()
                a.add_final_state(a.start_state)
                for s, t in b.transitions.items():
                    if s not in a.states:
                        a.add_state(s)
                    a.transitions[s] = t
                for s in b.final_states:
                    a.add_final_state(s)
                stack.append(a)
            elif char == '*':  # Cerradura de Kleene
                a = stack.pop()
                a.add_transition(a.start_state, a.start_state, None)
                a.add_final_state(a.start_state)
                stack.append(a)

        automata[token] = stack.pop()

    return automata


def automata_to_state_diagram(automata):
    state_diagram = []

    for token, af in automata.items():
        state_diagram.append(f"Token: {token}\n")
        state_diagram.append(f"Start state: {af.start_state}\n")
        state_diagram.append(f"Final states: {', '.join(map(str, af.final_states))}\n")
        state_diagram.append("Transitions:\n")

        for src, transition in af.transitions.items():
            for symbol, dest in transition.items():
                symbol_repr = repr(symbol) if symbol is not None else 'ε'
                state_diagram.append(f"  {src} --{symbol_repr}--> {dest}\n")

        state_diagram.append("\n")

    return ''.join(state_diagram)
