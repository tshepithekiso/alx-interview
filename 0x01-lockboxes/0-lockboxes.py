#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    keys = set()

    def dfs(box):
        if box == 0:
            visited[0] = True
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                dfs(key)

    dfs(0)
    return all(visited)
