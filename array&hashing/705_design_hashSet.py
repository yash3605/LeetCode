class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [Node() for _ in range(10**4)]

    def add(self, key: int) -> None:
        k = key % len(self.set)

        curr = self.set[k]
        while curr.next:
            if curr.next.data == key:
                return
            curr = curr.next
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        k = key % len(self.set)

        curr = self.set[k]

        while curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        k = key % len(self.set)

        curr = self.set[k]

        while curr.next:
            if curr.next.data == key:
                return True
            curr = curr.next
        return False


obj = MyHashSet()
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)
