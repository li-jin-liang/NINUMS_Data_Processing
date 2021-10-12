
class Cluster:
    # record the cluster at one step
    def __init__(self):
        self._kind = [0, 0, 0, 0]
        self._pos = [0, 0, 0]

    def assign_kind(self, kind):
        self._kind = list(map(int, kind))

    def assign_pos(self, pos):
        self._pos = list(map(float, pos))

    def he_num(self):
        return self._kind[3]

