from classAutomata import Automata
from funciones import parse_yalex, generate_automata, automata_to_state_diagram

def main():
    # Leer el archivo de entrada YALex
    input_file = "EjemploBasico.txt"
    
    # Obtener las definiciones regulares del archivo
    regular_definitions = parse_yalex(input_file)
    
    # Construir el autómata a partir de las definiciones regulares
    automata = generate_automata(regular_definitions)
    
    # Obtener el diagrama de transición de estados
    state_diagram = automata_to_state_diagram(automata)
    
    # Guardar o imprimir el diagrama de transición de estados
    print(state_diagram)

if __name__ == "__main__":
    main()