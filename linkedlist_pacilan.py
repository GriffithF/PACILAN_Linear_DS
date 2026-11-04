class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_from_front(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def display(self):
        if self.head is None:
            return "empty"
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result) + " → null"


def main():
    print("=" * 50)
    print("SINGLY LINKED LIST ALGORITHM - PACILAN")
    print("=" * 50)

    LL = LinkedList()
    letters = ["P", "A", "C", "I", "L", "A", "N"]

    print("\n--- ADD PHASE (Insert at the end) ---")
    for letter in letters:
        LL.insert_at_end(letter)
        print(f"After inserting '{letter}': {LL.display()}")

    print(f"\nAfter inserting all letters: {LL.display()}")

    print("\n--- REMOVE PHASE (Delete from the front / head) ---")
    while not LL.is_empty():
        removed = LL.delete_from_front()
        print(f"Deleted '{removed}': {LL.display()}")

    print("\nLinked List is now empty")
    print("=" * 50)


if __name__ == "__main__":
    main()