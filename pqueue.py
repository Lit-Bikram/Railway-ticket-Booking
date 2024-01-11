class PriorityQueue:
    def __init__(self, max_size=60):
        self.max_size = max_size
        self.heap = []

    def push(self, item, priority):
        if len(self.heap) < self.max_size:
            pair = (priority, item)
            self.heap.append(pair)
            self._heapify_up()

    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty priority queue")
        if len(self.heap) == 1:
            return self.heap.pop()[1]

        top = self.heap[0][1]
        last_item = self.heap.pop()
        self.heap[0] = last_item
        self._heapify_down()
        return top

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
