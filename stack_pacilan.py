def main():
    print("=" * 50)
    print("STACK ALGORITHM - PACILAN (LIFO)")
    print("=" * 50)

    S = []
    letters = ["P", "A", "C", "I", "L", "A", "N"]

    print("\n--- ADD PHASE (Push) ---")
    print("(Top is the rightmost element)")
    for letter in letters:
        S.append(letter)
        print(f"After pushing '{letter}': {S}   ← top")

    print(f"\nAfter pushing all letters: S = {S}  (N is on top)")

    print("\n--- REMOVE PHASE (Pop) ---")
    while S:
        removed = S.pop()
        print(f"Popped '{removed}': {S}")

    print("\nStack is now empty")
    print("=" * 50)


if __name__ == "__main__":
    main()