# Assessment 3.2: Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append("NULL")
        return " -> ".join(elements)

    def traverse_and_clear(self):
        output = []
        print("\n--- TRAVERSING LINKED LIST ---")
        while self.head is not None:
            output.append(self.head.data)
            print(f"Processing Node: {self.head.data}")
            self.head = self.head.next  # Move head to next node
        return output

def main():
    # Dynamic Input
    user_input = input("\nEnter a word/letters (press Enter to use default 'BAQUIRAN'): ").strip()
    if not user_input:
        letters = ['B', 'A', 'Q', 'U', 'I', 'R', 'A', 'N']
    else:
        letters = list(user_input.upper().replace(" ", ""))

    llist = LinkedList()

    for letter in letters:
        llist.append(letter)

    print("\nInitial Linked List:")
    print(llist.display())

    removal_output = llist.traverse_and_clear()

    print(f"\nRemoval Output: {', '.join(removal_output)}")
    print(f"Final Result: The linked list is empty because head = {llist.head}")

if __name__ == "__main__":
    main()