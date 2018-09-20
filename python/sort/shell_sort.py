#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from insertion_sort import insertion_sort


def shell_sort(inputs):
    g = distances(len(inputs))
    for h in reversed(g):
        inputs = insertion_sort(inputs, h)
    return inputs


def distances(max):
    distances = []
    h = 1
    while h <= max:
        distances.append(h)
        h = h * 3 + 1
    return distances


def main():
    numbers = shell_sort([8, 3, 1, 5, 2, 1])
    print(f"numbers: {numbers}\n")

    alphabets = shell_sort(["C", "B", "A", "Z", "A", "K"])
    print(f"alphabets: {alphabets}")


if __name__ == "__main__":
    main()

# [2, 3, 1, 5, 8, 1]
# [2, 1, 1, 5, 8, 3]
# [1, 2, 1, 5, 8, 3]
# [1, 1, 2, 5, 8, 3]
# [1, 1, 2, 5, 8, 3]
# [1, 1, 2, 5, 8, 3]
# [1, 1, 2, 3, 5, 8]
# numbers: [1, 1, 2, 3, 5, 8]

# ['A', 'B', 'A', 'Z', 'C', 'K']
# ['A', 'B', 'A', 'Z', 'C', 'K']
# ['A', 'B', 'A', 'Z', 'C', 'K']
# ['A', 'A', 'B', 'Z', 'C', 'K']
# ['A', 'A', 'B', 'Z', 'C', 'K']
# ['A', 'A', 'B', 'C', 'Z', 'K']
# ['A', 'A', 'B', 'C', 'K', 'Z']
# alphabets: ['A', 'A', 'B', 'C', 'K', 'Z']
