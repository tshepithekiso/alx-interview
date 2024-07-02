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

    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
            if boxes_checked is False:
                return boxes_checked
            return True
