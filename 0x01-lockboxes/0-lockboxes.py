#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
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
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
