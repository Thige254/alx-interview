#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a queue with the first box
    queue = [0]

    # Iterate over the queue
    while queue:
        # Pop the first box from the queue
        current_box = queue.pop(0)

        # If the current box has already been visited, skip it
        if current_box in visited:
            continue

        # Add the current box to the visited set
        visited.add(current_box)

        # Add all keys in the current box to the queue
        for key in boxes[current_box]:
            if key < len(boxes):
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

# My test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
