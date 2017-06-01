from heap import Heap


class Price:
    def __init__(self, N, k, c):
        self.heap = Heap()
        self.heap.push(0, k)
        self.edges = {}
        self.nodes = set([0])

        for n in range(N):
            self.nodes.add(n + 1)
            self.heap.push(n + 1, k)

            for i in range(c):
                sample = self.heap.sample()
                self.edges[n + 1] = sample.id
                self.heap.add_mass(sample.pos, 1)
