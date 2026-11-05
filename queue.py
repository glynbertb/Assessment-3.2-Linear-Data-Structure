# Assessment 3.2: Queue Implementation (FIFO - First In, First Out)
from collections import deque

def main():
    # Dynamic Input
    user_input = input("\nEnter a word/letters (press Enter to use default 'BAQUIRAN'): ").strip()
    if not user_input:
        letters = ['B', 'A', 'Q', 'U', 'I', 'R', 'A', 'N']
    else:
        letters = list(user_input.upper().replace(" ", ""))

    my_queue = deque()

    # Enqueue elements
    print("\n--- ENQUEUING TO QUEUE ---")
    for letter in letters:
        my_queue.append(letter)
        print(f"Enqueued: {letter}")

    print(f"\nInitial Queue: {list(my_queue)}")

    # Dequeue elements
    print("\n--- DEQUEUING FROM QUEUE (FIFO) ---")
    removal_output = []
    while len(my_queue) > 0:
        dequeued = my_queue.popleft()
        removal_output.append(dequeued)
        print(f"Dequeued: {dequeued}")

    print(f"\nRemoval Output: {', '.join(removal_output)}")
    print(f"Final Result: The queue is empty. (Current size: {len(my_queue)})")

if __name__ == "__main__":
    main()