from pyformlang.regular_expression import Regex
from graphviz import Digraph

def regex_to_enfa(regex_str):
    regex = Regex(regex_str)
    return regex.to_epsilon_nfa()

def enfa_to_graphviz(enfa, mega_start_state=None):
    graph = Digraph("ENFA", format="png")

    # Creación de los estados del AFN
    graph.attr("node", shape="circle")
    for state in enfa.states:
        graph.node(str(state))

    # Creación del estado inicial
    graph.attr("node", shape="circle", style="filled", fillcolor="lightblue")
    graph.node(str(enfa._start_state))

    # Creación de los estados finales
    graph.attr("node", shape="doublecircle")
    for final_state in enfa.final_states:
        graph.node(str(final_state))

    # Creación de las transiciones
    for from_state, to_dict in enfa._transition_function._transitions.items():
        for symbol, to_states in to_dict.items():
            for to_state in to_states:
                graph.edge(str(from_state), str(to_state), label=str(symbol))

    return graph

def main():
    regex_list = [
        "0|1|2",
        "(0|1|2)((0|1|2))*",
        "a|b|c|A|B|C",
        "(a|b|c|A|B|C)((a|b|c|A|B|C)|(0|1|2))*"
    ]

    enfas = [regex_to_enfa(regex) for regex in regex_list]

    # Graficar y guardar ENFA individuales
    for idx, enfa in enumerate(enfas):
        enfa_graph = enfa_to_graphviz(enfa)
        enfa_graph.render(f"enfa_output_{idx}", view=True)


if __name__ == "__main__":
    main()
