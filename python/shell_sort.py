#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from insertion_sort import insertion_sort


def shell_sort(inputs):
    result = list(inputs)
    g = distances(len(inputs))
    for h in reversed(g):
        result = insertion_sort(result, h)
    return result


def distances(max):
    distances = []
    h = 1
    while h <= max:
        distances.append(h)
        h = h * 3 + 1
    return distances


def main():
    numbers = [8, 3, 1, 5, 2, 1]
    print(numbers)
    numbers_result = shell_sort(numbers)
    print("numbers: {0}".format(numbers_result))

    print()

    alphabets = ["C", "B", "A", "Z", "A", "K"]
    alphabets_result = shell_sort(alphabets)
    print("alphabets: {0}".format(alphabets_result))


if __name__ == "__main__":
    main()

# [8, 3, 1, 5, 2, 1]
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
