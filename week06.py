class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None
        self.reer = None
        self.size = 0

    def enqueue(self, data):
        self.size += 1
        node = Node(data)
        if self.reer is None:
            self.front = node
            self.reer = node
        else:
            self.reer.link = node
            self.reer = node

q = Queue()
q.enqueue("Data structure")
q.enqueue("Database")
print(q.size, q.front.data, q.reer.data)