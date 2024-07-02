#!/usr/bin/python3

"""
Solution to lockboxes problems
"""


def canUnlockAll(boxes):
    """
    Determine if a series of locked boxes can be
    opened based on the keys that can be attained.
    And solution to the lockboxes issues
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # First box is always unlocked

    queue = [0]  # Start with the first box
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
