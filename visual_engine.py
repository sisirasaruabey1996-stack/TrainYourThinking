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