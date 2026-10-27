from collections import deque

def water_jug(cap1, cap2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(a, b)

        if a == target or b == target:
            print("Target reached!")
            return

        states = [
            (cap1, b), (a, cap2),  # Fill jugs
            (0, b), (a, 0),        # Empty jugs
            (a - min(a, cap2-b), b + min(a, cap2-b)),
            (a + min(b, cap1-a), b - min(b, cap1-a))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Solution not possible")

water_jug(4, 3, 2)

#dfs
def water_jug(cap1, cap2, target):
    stack = [(0, 0)]
    visited = set()

    while stack:
        a, b = stack.pop()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(a, b)

        if a == target or b == target:
            print("Target reached!")
            return

        states = [
            (cap1, b), (a, cap2),  # Fill jugs
            (0, b), (a, 0),        # Empty jugs
            (a - min(a, cap2-b), b + min(a, cap2-b)),
            (a + min(b, cap1-a), b - min(b, cap1-a))
        ]

        for state in states:
            if state not in visited:
                stack.append(state)

    print("Solution not possible")

water_jug(4, 3, 2)
