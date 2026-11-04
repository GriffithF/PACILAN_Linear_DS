def main():
    print("=" * 50)
    print("ARRAY ALGORITHM - PACILAN")
    print("=" * 50)

    Arr = []
    letters = ["P", "A", "C", "I", "L", "A", "N"]

    print("\n--- ADD PHASE (Append at the end) ---")
    for letter in letters:
        Arr.append(letter)
        print(f"After adding '{letter}': {Arr}")

    print(f"\nAfter adding all letters: Arr = {Arr}")

    print("\n--- REMOVE PHASE (Remove at front / index 0) ---")
    while Arr:
        removed = Arr.pop(0)
        print(f"Removed '{removed}': {Arr}")

    print("\nArray is now empty")
    print("=" * 50)


if __name__ == "__main__":
    main()