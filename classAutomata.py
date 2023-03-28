class Automata:
    def __init__(self):
        self.states = set()
        self.transitions = {}
        self.start_state = None
        self.final_states = set()

    def add_state(self, state):
        self.states.add(state)

    def set_start_state(self, state):
        if state not in self.states:
            self.add_state(state)
        self.start_state = state

    def add_final_state(self, state):
        if state not in self.states:
            self.add_state(state)
        self.final_states.add(state)

    def add_transition(self, src, dest, symbol):
        if src not in self.states:
            self.add_state(src)
        if dest not in self.states:
            self.add_state(dest)
        
        if src not in self.transitions:
            self.transitions[src] = {}
        
        self.transitions[src][symbol] = dest

    def __str__(self):
        return (
            f"Automata(states={self.states}, start_state={self.start_state}, "
            f"final_states={self.final_states}, transitions={self.transitions})"
        )

    def __repr__(self):
        return self.__str__()
