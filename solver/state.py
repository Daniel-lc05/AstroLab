class State:
    def __init__(self, t, h, v):
        self.t = t
        self.h = h
        self.v = v

    def __repr__(self):
        return f"State(t={self.t}, h={self.h}, v={self.v})"

    def copy(self):
        return State(self.t, self.h, self.v)