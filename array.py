# Assessment 3.2: Array (Fixed-Capacity) Implementation

def main():
    # Dynamic Input
    user_input = input("\nEnter a word/letters (press Enter to use default 'BAQUIRAN'): ").strip()
    if not user_input:
        letters = ['B', 'A', 'Q', 'U', 'I', 'R', 'A', 'N']
    else:
        letters = list(user_input.upper().replace(" ", ""))

    capacity = len(letters)
    my_array = [None] * capacity

    # Insert elements into the array
    for i in range(capacity):
        my_array[i] = letters[i]

    size = capacity
    print(f"\nInitial Array (Capacity: {capacity}):")
    print(my_array)

    # Remove/display from last active position
    print("\n--- REMOVING FROM ARRAY (LAST ACTIVE POSITION) ---")
    removal_output = []
    while size > 0:
        element = my_array[size - 1]
        removal_output.append(element)
        print(f"Accessed index {size - 1}: {element}")
        size -= 1

    print(f"\nRemoval Output: {', '.join(removal_output)}")
    print(f"Final Result: The array has zero active elements (size = {size}).")

if __name__ == "__main__":
    main()