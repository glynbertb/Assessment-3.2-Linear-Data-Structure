# Assessment 3.2: Stack Implementation (LIFO - Last In, First Out)

def main():
    # Dynamic Input
    user_input = input("\nEnter a word/letters (press Enter to use default 'BAQUIRAN'): ").strip()
    if not user_input:
        letters = ['B', 'A', 'Q', 'U', 'I', 'R', 'A', 'N']
    else:
        letters = list(user_input.upper().replace(" ", ""))

    my_stack = []

    # Push elements onto the stack
    print("\n--- PUSHING TO STACK ---")
    for letter in letters:
        my_stack.append(letter)
        print(f"Pushed: {letter}")

    print(f"\nInitial Stack: {my_stack}")

    # Pop elements from the stack
    print("\n--- POPPING FROM STACK (LIFO) ---")
    removal_output = []
    while len(my_stack) > 0:
        popped = my_stack.pop()
        removal_output.append(popped)
        print(f"Popped: {popped}")

    print(f"\nRemoval Output: {', '.join(removal_output)}")
    print(f"Final Result: The stack is empty. (Current size: {len(my_stack)})")

if __name__ == "__main__":
    main()