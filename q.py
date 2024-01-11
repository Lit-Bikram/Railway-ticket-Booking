from pqueue import PriorityQueue

details = [
    [
        {'first_name': 'Arijit', 'last_name': 'Singh','age': '50', 'gender': 'male'},
        {'first_name': 'Shreya', 'last_name': 'Ghoshal','age': '40', 'gender': 'female'},
        {'first_name': 'Sonu', 'last_name': 'Nigam', 'age': '55', 'gender': 'male'},
        {'first_name': 'Lata', 'last_name': 'Mangeshkar','age': '70', 'gender': 'female'}
    ],
    [
        {'first_name': 'John', 'last_name': 'Doe', 'age': '25', 'gender': 'male'}
    ],
    [
        {'first_name': 'Alice', 'last_name': 'Smith','age': '30', 'gender': 'female'},
        {'first_name': 'Bob', 'last_name': 'Johnson', 'age': '35', 'gender': 'male'}
    ],
    [
        {'first_name': 'Emma', 'last_name': 'Brown','age': '28', 'gender': 'female'},
    ],
    [
        {'first_name': 'Daniel', 'last_name': 'Williams','age': '40', 'gender': 'male'},
        {'first_name': 'Grace', 'last_name': 'Miller','age': '62', 'gender': 'female'}
    ],
    [
        {'first_name': 'Ryan', 'last_name': 'Davis', 'age': '32', 'gender': 'male'},
        {'first_name': 'Sophia', 'last_name': 'Wilson','age': '29', 'gender': 'female'},
        {'first_name': 'Michael', 'last_name': 'Jones', 'age': '45', 'gender': 'male'}
    ],
    [
        {'first_name': 'Mukesh', 'last_name': 'Ambani', 'age': '65', 'gender': 'male'}
    ],
    [
        {'first_name': 'Ethan', 'last_name': 'Martinez','age': '38', 'gender': 'male'},
        {'first_name': 'Ava', 'last_name': 'Lee', 'age': '26', 'gender': 'female'},
        {'first_name': 'William', 'last_name': 'Taylor','age': '33', 'gender': 'male'}
    ],
    [
        {'first_name': 'Mia', 'last_name': 'Johnson','age': '31', 'gender': 'female'},
        {'first_name': 'James', 'last_name': 'Clark', 'age': '29', 'gender': 'male'},
        {'first_name': 'Noah', 'last_name': 'Ramirez','age': '41', 'gender': 'male'},
        {'first_name': 'Liam', 'last_name': 'Perez', 'age': '67', 'gender': 'male'}
    ],
    [
        {'first_name': 'Emily', 'last_name': 'Anderson','age': '23', 'gender': 'female'},
        {'first_name': 'Abigail', 'last_name': 'Hill','age': '28', 'gender': 'female'},
        {'first_name': 'Isabella', 'last_name': 'Baker','age': '30', 'gender': 'female'},
        {'first_name': 'Logan', 'last_name': 'Garcia','age': '64', 'gender': 'male'},
        {'first_name': 'Olivia', 'last_name': 'Moore','age': '27', 'gender': 'female'}
    ]
]

print(len(details))

class PriorityQueue:
    def __init__(self, max_size=60):
        self.max_size = max_size
        self.heap = []

    def push(self, item, priority, index):
        if len(self.heap) < self.max_size:
            pair = (priority, index, item)
            self.heap.append(pair)
            self._heapify_up()

    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty priority queue")
        if len(self.heap) == 1:
            return self.heap.pop()[2]

        top = self.heap[0][2]
        last_item = self.heap.pop()
        self.heap[0] = last_item
        self._heapify_down()
        return top

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0] or (
                    self.heap[index][0] == self.heap[parent_index][0] and self.heap[index][1] < self.heap[parent_index][1]):
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

            if left_child_index < len(self.heap) and (
                    self.heap[left_child_index][0] < self.heap[smallest][0] or (
                    self.heap[left_child_index][0] == self.heap[smallest][0] and
                    self.heap[left_child_index][1] < self.heap[smallest][1])):
                smallest = left_child_index

            if right_child_index < len(self.heap) and (
                    self.heap[right_child_index][0] < self.heap[smallest][0] or (
                    self.heap[right_child_index][0] == self.heap[smallest][0] and
                    self.heap[right_child_index][1] < self.heap[smallest][1])):
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

# Example usage:
pq = PriorityQueue()

for i in range(len(details)):
    pq.push(details[i], len(details[i]), i)

while pq.heap:
    popped_item = pq.pop()
    print(popped_item, len(popped_item), "\n")
