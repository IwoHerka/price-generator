class Heap:
    class Node:
        def __init__(self, heap, mass=0):
            self.pos = None
            self.heap = heap
            self.mass = mass
            self.subtree_mass = mass

        @property
        def left(self):
            try:
                return self.heap[(self.pos << 1) + 1]
            except IndexError:
                return None

        @property
        def right(self):
            try:
                return self.heap[(self.pos << 1) + 2]
            except IndexError:
                return None

        @property
        def parent(self):
            pos = (self.pos - 1) >> 1
            return self.heap[pos] if pos >= 0 else None

        def __lt__(self, other):
            return self.mass < other.mass

        def __repr__(self):
            return str(self.mass)

    def __init__(self):
        self.heap = []
        self.size = 0

    def sample(self):
        return self._sample(self.heap[0], 0., uni_sample()) if self.heap else None

    def push(self, mass):
        self.size += 1
        item = self.Node(self.heap, mass)
        self.heap.append(item)
        item.pos = len(self.heap) - 1

        # Fix heap.
        old_mass = 0
        while item.parent:
            if item.parent < item:
                old_mass = item.parent.subtree_mass
                self._swap(item, item.parent)
            else:
                item.parent.subtree_mass += item.subtree_mass - old_mass
                break


    def _add_mass(self, pos, change):
        item = self.heap[pos]
        item.mass += change
        item.subtree_mass += change

        # Fix heap.
        while item.parent:
            item.parent.subtree_mass += change

            if item.parent < item:
                self._swap(item, item.parent)
            else:
                item = item.parent


    def _swap(self, first, second):
        self.heap[first.pos] = second
        self.heap[second.pos] = first

        second.pos += first.pos
        first.pos = second.pos - first.pos
        second.pos -= first.pos

        # Fix sub-tree masses.
        second.subtree_mass = second.mass

        left = second.left
        second.subtree_mass += left.subtree_mass if left else 0

        right = second.right
        second.subtree_mass += right.subtree_mass if right else 0

        first.subtree_mass = first.mass

        left = first.left
        first.subtree_mass += left.subtree_mass if left else 0

        right = first.right
        first.subtree_mass += right.subtree_mass if right else 0












































#
