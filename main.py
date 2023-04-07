from funciones import parse_yalex, generate_automata, automata_to_state_diagram

def main():
    input_file = "EjemploBasico.txt"
    regular_definitions = parse_yalex(input_file)
    automata = generate_automata(regular_definitions)
    state_diagrams = automata_to_state_diagram(automata)

    for token, state_diagram in state_diagrams.items():
        print(f"Token: {token}")
        print(f"State diagram: {state_diagram}")
        print()

if __name__ == "__main__":
    main()