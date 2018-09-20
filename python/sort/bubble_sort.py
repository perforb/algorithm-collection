#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(inputs):
    last_index = len(inputs) - 1
    swap_count = 0
    swapped = True
    for i in range(0, last_index):
        if not swapped:
            break
        swapped = False
        for j in range(last_index, i, -1):
            if inputs[j] < inputs[j - 1]:
                inputs[j], inputs[j - 1] = inputs[j - 1], inputs[j]
                swapped = True
                swap_count += 1

            print(inputs)

    return inputs, swap_count


def main():
    numbers = bubble_sort([8, 3, 1, 5, 2, 1])
    print(f'numbers: {numbers[0]}, swap_count: {numbers[1]}\n')

    alphabets = bubble_sort(["C", "B", "A", "Z", "A", "K"])
    print(f'alphabets: {alphabets[0]}, swap_count: {alphabets[1]}')


if __name__ == "__main__":
    main()

# [8, 3, 1, 5, 1, 2]
# [8, 3, 1, 1, 5, 2]
# [8, 3, 1, 1, 5, 2]
# [8, 1, 3, 1, 5, 2]
# [1, 8, 3, 1, 5, 2]
# [1, 8, 3, 1, 2, 5]
# [1, 8, 3, 1, 2, 5]
# [1, 8, 1, 3, 2, 5]
# [1, 1, 8, 3, 2, 5]
# [1, 1, 8, 3, 2, 5]
# [1, 1, 8, 2, 3, 5]
# [1, 1, 2, 8, 3, 5]
# [1, 1, 2, 8, 3, 5]
# [1, 1, 2, 3, 8, 5]
# [1, 1, 2, 3, 5, 8]
# numbers: [1, 1, 2, 3, 5, 8], swap_count: 11

# ['C', 'B', 'A', 'Z', 'A', 'K']
# ['C', 'B', 'A', 'A', 'Z', 'K']
# ['C', 'B', 'A', 'A', 'Z', 'K']
# ['C', 'A', 'B', 'A', 'Z', 'K']
# ['A', 'C', 'B', 'A', 'Z', 'K']
# ['A', 'C', 'B', 'A', 'K', 'Z']
# ['A', 'C', 'B', 'A', 'K', 'Z']
# ['A', 'C', 'A', 'B', 'K', 'Z']
# ['A', 'A', 'C', 'B', 'K', 'Z']
# ['A', 'A', 'C', 'B', 'K', 'Z']
# ['A', 'A', 'C', 'B', 'K', 'Z']
# ['A', 'A', 'B', 'C', 'K', 'Z']
# ['A', 'A', 'B', 'C', 'K', 'Z']
# ['A', 'A', 'B', 'C', 'K', 'Z']
# alphabets: ['A', 'A', 'B', 'C', 'K', 'Z'], swap_count: 7
