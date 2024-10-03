#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
        boxes (list of list): A list where each element is a list of keys
        that correspond to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Number of boxes
    n = len(boxes)

    # A set to keep track of boxes we can open (start with box 0)
    unlocked = set([0])

    # A stack to track boxes we need to check (start with box 0)
    to_check = [0]

    # Loop while there are boxes to check
    while to_check:
        # Pop a box from the stack
        current_box = to_check.pop()

        # Go through all keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a box we haven't unlocked yet
            if key not in unlocked and key < n:
                # Unlock the box and add it to the set of unlocked boxes
                unlocked.add(key)
                # Add the newly unlocked box to the stack for further exploration
                to_check.append(key)

    # Return True if we've unlocked all boxes, otherwise False
    return len(unlocked) == n


if __name__ == "__main__":
    # Test cases
    boxes_list = [
        [[1], [2], [3], [4], []],  # True
        [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]],  # True
        [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]],  # True
        [[0]],  # True
        [[1], []],  # False
        [list(range(1, 1001)) for _ in range(1000)],  # True
        [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [],
         [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6],
         [9, 5, 8, 8], [6, 2, 8, 6]],  # False
        [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3],
         [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7],
         [4, 2, 9, 6, 6, 5, 5]]  # True
    ]

    for boxes in boxes_list:
        print(f'Boxes: {boxes} => Can Unlock All: {canUnlockAll(boxes)}')
