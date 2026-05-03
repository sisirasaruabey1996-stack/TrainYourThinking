import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# 🔹 Binary Search Animation
def animate_binary_search(arr: list, target: int):
    left, right = 0, len(arr) - 1
    step = 1

    print(f"\nSearching for: {target}")
    print(f"Array: {arr}\n")
    time.sleep(1)

    while left <= right:
        mid = (left + right) // 2

        visual = []
        for i, val in enumerate(arr):
            if i == mid:
                visual.append(f"[{val}]")
            elif left <= i <= right:
                visual.append(f" {val} ")
            else:
                visual.append(" _ ")

        print(f"Step {step}: {' '.join(visual)}")
        print(f"         left={left} mid={mid} right={right}")

        if arr[mid] == target:
            print(f"\nFound {target} at index {mid}!")
            return
        elif arr[mid] < target:
            print(f"         {arr[mid]} < {target} → go right\n")
            left = mid + 1
        else:
            print(f"         {arr[mid]} > {target} → go left\n")
            right = mid - 1

        step += 1
        time.sleep(1.2)

    print(f"\n{target} not found.")


# 🔹 Bubble Sort Animation
def animate_bubble_sort(arr: list):
    arr = arr.copy()
    n = len(arr)

    print(f"\nBubble Sort — array size: {n}\n")
    time.sleep(1)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            visual = []
            for k, val in enumerate(arr):
                if k == j:
                    visual.append(f"[{val}]")
                elif k == j + 1:
                    visual.append(f"[{val}]")
                elif k >= n - i:
                    visual.append(f" {val}✓")
                else:
                    visual.append(f" {val} ")

            print(f"  {'  '.join(visual)}")

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print("  swapped!\n")
            else:
                print("  ok\n")

            time.sleep(0.6)

        if not swapped:
            break

    print(f"Sorted: {arr}")


# 🔹 Linear Search Animation
def animate_linear_search(arr: list, target: int):
    print(f"\nLinear Search — target: {target}")
    print(f"Checking every element...\n")
    time.sleep(1)

    for i, val in enumerate(arr):
        visual = []
        for k, v in enumerate(arr):
            if k == i:
                visual.append(f"[{v}]")
            elif k < i:
                visual.append(" ✗ ")
            else:
                visual.append(f" {v} ")

        print(f"Step {i+1}: {'  '.join(visual)}")

        if val == target:
            print(f"\nFound {target} at index {i}!")
            print(f"Steps taken: {i+1}\n")
            return
        time.sleep(0.5)

    print(f"\n{target} not found. Steps taken: {len(arr)}")


# 🔹 Comparison: Linear vs Binary
def compare_search(target: int):
    arr = list(range(2, 22, 2))
    print("=" * 45)
    print("LINEAR SEARCH")
    print("=" * 45)
    animate_linear_search(arr, target)
    time.sleep(1)
    print("=" * 45)
    print("BINARY SEARCH")
    print("=" * 45)
    animate_binary_search(arr, target)


# 🔹 Binary Tree Traversal Animation
def animate_tree():
    tree = {
        0: {"val": 10, "left": 1, "right": 2},
        1: {"val": 5,  "left": 3, "right": 4},
        2: {"val": 15, "left": 5, "right": 6},
        3: {"val": 3,  "left": None, "right": None},
        4: {"val": 7,  "left": None, "right": None},
        5: {"val": 12, "left": None, "right": None},
        6: {"val": 20, "left": None, "right": None},
    }

    def draw(visited: set):
        lines = [
            f"        {'['+str(tree[0]['val'])+']' if 0 in visited else str(tree[0]['val'])}",
            f"       / \\",
            f"     {'['+str(tree[1]['val'])+']' if 1 in visited else str(tree[1]['val'])}     {'['+str(tree[2]['val'])+']' if 2 in visited else str(tree[2]['val'])}",
            f"    / \\   / \\",
            f"  {'['+str(tree[3]['val'])+']' if 3 in visited else str(tree[3]['val'])}  {'['+str(tree[4]['val'])+']' if 4 in visited else str(tree[4]['val'])}  {'['+str(tree[5]['val'])+']' if 5 in visited else str(tree[5]['val'])}  {'['+str(tree[6]['val'])+']' if 6 in visited else str(tree[6]['val'])}",
        ]
        for line in lines:
            print(line)
        print()

    # This order corresponds to preorder in your current code
    order = [0, 1, 3, 4, 2, 5, 6]
    visited = set()

    print("\nTraversal (visual step-by-step)\n")
    time.sleep(1)

    for node in order:
        visited.add(node)
        draw(visited)
        print(f"Visiting: {tree[node]['val']}\n")
        time.sleep(1.2)

    result = [tree[n]["val"] for n in order]
    print(f"Traversal order: {result}")