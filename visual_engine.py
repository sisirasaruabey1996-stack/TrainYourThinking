import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_binary_search(arr: list, target: int):
    left, right = 0, len(arr) - 1
    step = 1

    print(f"\nSearching for: {target}")
    print(f"Array: {arr}\n")
    time.sleep(1)

    while left <= right:
        mid = (left + right) // 2

        # Build visual
        visual = []
        for i, val in enumerate(arr):
            if i == mid:
                visual.append(f"[{val}]")  # middle
            elif left <= i <= right:
                visual.append(f" {val} ")  # active range
            else:
                visual.append(f" _ ")      # eliminated

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