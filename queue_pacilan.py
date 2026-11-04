from collections import deque

def main():
    print("=" * 50)
    print("QUEUE ALGORITHM - PACILAN (FIFO)")
    print("=" * 50)

    Q = deque()
    letters = ["P", "A", "C", "I", "L", "A", "N"]

    print("\n--- ADD PHASE (Enqueue at the rear) ---")
    print("(Front is the leftmost element)")
    for letter in letters:
        Q.append(letter)
        print(f"After enqueuing '{letter}': {list(Q)}   ← front is left")

    print(f"\nAfter enqueuing all letters: Q = {list(Q)}  (P is at front)")

    print("\n--- REMOVE PHASE (Dequeue from the front) ---")
    while Q:
        removed = Q.popleft()
        print(f"Dequeued '{removed}': {list(Q)}")

    print("\nQueue is now empty")
    print("=" * 50)


if __name__ == "__main__":
    main()