"""
LeetCode #706: Design HashMap

Design a HashMap without using any built-in hash table libraries. Implement the MyHashMap class: MyHashMap() initializes the object, void put(int key, int value) inserts a (key, value) pair, int get(int key) returns the value to which the specified key is mapped, or -1 if no mapping exists, void remove(key) removes the key and its corresponding value.

Constraints:
0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyHashMap:

    def __init__(self):
        self.set = [Node([0, 0]) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        k = key % len(self.set)

        curr = self.set[k]
        while curr.next:
            if curr.next.data[0] == key:
                curr.next.data[1] = value
                return
            curr = curr.next
        curr.next = Node([key, value])

    def get(self, key: int) -> int:
        k = key % len(self.set)

        curr = self.set[k]

        while curr.next:
            if curr.next.data[0] == key:
                return curr.next.data[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        k = key % len(self.set)

        curr = self.set[k]
        while curr.next:
            if curr.next.data[0] == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)       return False

# class MyHashMap:
#     def __init__(self):
#         self.hashmap = [-1] * 1000001
#
#     def put(self, key: int, value: int) -> None:
#         self.hashmap[key] = value
#
#     def get(self, key: int) -> int:
#         return self.hashmap[key]
#
#     def remove(self, key: int) -> None:
#         self.hashmap[key] = -1
