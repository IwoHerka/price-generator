from heap import Heap


class Price:
    def __init__(self, N, init_mass, out_deg):
        self.heap = Heap()
        self.heap.push(0, init_mass)
        self.edges = {}

        for n in range(N):
            for _ in range(out_deg):
                target = self.heap.sample()
                links = self.edges.get(n + 1, set())
                links.add(target.id)
                self.edges[n + 1] = links
                self.heap.add_mass(target.pos, 1)

            self.heap.push(n + 1, init_mass)

    def write(self, path):
        with open(path, 'w') as out:
            for src in self.edges:
                for tgt in self.edges[src]:
                    out.write('{} {}\n'.format(src, tgt))
