#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(inputs, distance):
    result = list(inputs)
    for i in range(distance, len(result)):
        v = result[i]
        j = (i - distance)
        while j >= 0 and result[j] > v:
            result[j + distance] = result[j]
            j -= distance

        result[j + distance] = v
        print(result)

    return result


def insertion_sort2(inputs):
    result = list(inputs)
    for i in range(1, len(result)):
        v = result[i]
        j = (i - 1)
        while j >= 0 and result[j] > v:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = v
        print(result)

    return result


def insertion_sort3(inputs):
    result = list(inputs)
    for i in range(1, len(result)):
        v = result[i]
        for j in range((i - 1), -2, -1):
            if j >= 0 and result[j] > v:
                result[j + 1] = result[j]
            else:
                break

        result[j + 1] = v
        print(result)

    return result


def main():
    numbers = [8, 3, 1, 5, 2, 1]
    alphabets = ["C", "B", "A", "Z", "A", "K"]

    print(numbers)
    print("numbers: {0}".format(insertion_sort(numbers, 3)))
    print()
    print(alphabets)
    print("alphabets: {0}".format(insertion_sort(alphabets, 1)))


if __name__ == "__main__":
    main()

# [3, 8, 1, 5, 2, 1]
# [1, 3, 8, 5, 2, 1]
# [1, 3, 5, 8, 2, 1]
# [1, 2, 3, 5, 8, 1]
# [1, 1, 2, 3, 5, 8]
# numbers: [1, 1, 2, 3, 5, 8]

# ['B', 'C', 'A', 'Z', 'A', 'K']
# ['A', 'B', 'C', 'Z', 'A', 'K']
# ['A', 'B', 'C', 'Z', 'A', 'K']
# ['A', 'A', 'B', 'C', 'Z', 'K']
# ['A', 'A', 'B', 'C', 'K', 'Z']
# alphabets: ['A', 'A', 'B', 'C', 'K', 'Z']
