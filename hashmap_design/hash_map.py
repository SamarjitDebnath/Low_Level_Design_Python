"""
Hashing with collision avoidance by using chaining principle
"""

from typing import Generic, TypeVar, Optional


class StaticVar():
    # static variables
    K = TypeVar('K')
    V = TypeVar('V')


class Node(Generic[StaticVar.K, StaticVar.V]):
    def __init__(self, key: StaticVar.K, value: StaticVar.V):
        self.key: StaticVar.K = key  # key
        self.value: StaticVar.V = value  # value
        self.next: Optional[Node[StaticVar.K, StaticVar.V]
                            ] = None  # pointer to next node


class HashMap(Generic[StaticVar.K, StaticVar.V]):
    initial_size: int = 1 << 4
    maximum_capacity: int = 1 << 30

    def __init__(self, capacity: Optional[int] = None):
        if capacity:
            self.tableSize: int = self.get_tableSize(capacity)
            self.hashTable: list[Optional[Node[StaticVar.K, StaticVar.V]]] = [
                None] * self.tableSize
        else:
            self.hashTable: list[Optional[Node[StaticVar.K, StaticVar.V]]] = [
                None] * HashMap.initial_size

    def get_tableSize(self, capacity: int) -> int:
        """
        return next power of 2
        """
        if capacity <= 0:
            return 1
        n = capacity - 1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 16

        return HashMap.maximum_capacity if n >= HashMap.maximum_capacity else n + 1

    def hash_function(self, key: StaticVar.K) -> int:
        return hash(key) % len(self.hashTable)

    def put(self, key: StaticVar.K, value: StaticVar.V):
        hashCode: int = hash(key) % len(self.hashTable)
        node: Optional[Node[StaticVar.K, StaticVar.V]
                       ] = self.hashTable[hashCode]

        if not node:
            # if hashTable is empty, then simply insert
            newNode: Node[StaticVar.K, StaticVar.V] = Node(key, value)
            self.hashTable[hashCode] = newNode
        else:
            # if collision occurs, then using chaining method
            currentNode: Node[StaticVar.K, StaticVar.V] = node
            while currentNode.next:
                # checks for key is present in hashTable if yes then replace with new value
                if currentNode.key == key:
                    currentNode.value = value
                    return
                currentNode = currentNode.next
            new_node: Node[StaticVar.K, StaticVar.V] = Node(key, value)
            currentNode.next = new_node

    def get(self, key: StaticVar.K) -> StaticVar.V | str:
        hashCode: int = self.hash_function(key)
        node: Optional[Node[StaticVar.K, StaticVar.V]
                       ] = self.hashTable[hashCode]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        raise Exception("Invalid Key")

    def delete(self, key: StaticVar.K, statusFlag: Optional[bool] = False) -> str | None:
        status: str = "Not Found"
        hashCode: int = self.hash_function(key)
        currentNode: Optional[Node[StaticVar.K,
                                   StaticVar.V]] = self.hashTable[hashCode]
        prevNode: Optional[Node[StaticVar.K, StaticVar.V]] = None

        while currentNode:
            if currentNode.key == key:
                if prevNode:
                    prevNode.next = currentNode.next
                else:
                    self.hashTable[hashCode] = currentNode.next
                status = f"{key} is deleted"
                return status if statusFlag == True else None
            prevNode = currentNode
            currentNode = currentNode.next
        return status


def main():

    hash_map = HashMap[str, int]()
    hash_map.put("One", 1)
    hash_map.put("Two", 2)
    hash_map.put("Three", 3)
    hash_map.put("Four", 4)

    print(hash_map.get("Three"))
    print(hash_map.delete("One", True))
    print(hash_map.get("One"))


if __name__ == "__main__":
    main()
