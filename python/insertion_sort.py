#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(inputs, distance):
    for i in range(distance, len(inputs)):
        v = inputs[i]
        j = (i - distance)
        while j >= 0 and inputs[j] > v:
            inputs[j + distance] = inputs[j]
            j -= distance

        inputs[j + distance] = v
        print(inputs)

    return inputs


def insertion_sort2(inputs):
    for i in range(1, len(inputs)):
        v = inputs[i]
        j = (i - 1)
        while j >= 0 and inputs[j] > v:
            inputs[j + 1] = inputs[j]
            j -= 1

        inputs[j + 1] = v
        print(inputs)

    return inputs


def insertion_sort3(inputs):
    for i in range(1, len(inputs)):
        v = inputs[i]
        for j in range((i - 1), -2, -1):
            if j >= 0 and inputs[j] > v:
                inputs[j + 1] = inputs[j]
            else:
                break

        inputs[j + 1] = v
        print(inputs)

    return inputs


def main():
    numbers = insertion_sort([8, 3, 1, 5, 2, 1], 1)
    print(f'numbers: {numbers}\n')

    alphabets = insertion_sort(["C", "B", "A", "Z", "A", "K"], 1)
    print(f'alphabets: {alphabets}')


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
