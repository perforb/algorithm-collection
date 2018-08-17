#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def selection_sort(inputs):
    size = len(inputs)
    swap_count = 0
    for i in range(0, size):
        min_index = i
        for j in range(i, size):
            if inputs[j] < inputs[min_index]:
                min_index = j
        inputs[i], inputs[min_index] = inputs[min_index], inputs[i]
        if i != min_index:
            swap_count += 1
        print(inputs)

    return inputs, swap_count


def main():
    numbers = selection_sort([8, 3, 1, 5, 2, 1])
    print(f"numbers: {numbers[0]}, swap_count: {numbers[1]}\n")

    alphabets = selection_sort(["C", "B", "A", "Z", "A", "K"])
    print(f"alphabets: {alphabets[0]}, swap_count: {alphabets[1]}")


if __name__ == "__main__":
    main()

# [1, 3, 8, 5, 2, 1]
# [1, 1, 8, 5, 2, 3]
# [1, 1, 2, 5, 8, 3]
# [1, 1, 2, 3, 8, 5]
# [1, 1, 2, 3, 5, 8]
# [1, 1, 2, 3, 5, 8]
# numbers: [1, 1, 2, 3, 5, 8], swap_count: 5

# ['A', 'B', 'C', 'Z', 'A', 'K']
# ['A', 'A', 'C', 'Z', 'B', 'K']
# ['A', 'A', 'B', 'Z', 'C', 'K']
# ['A', 'A', 'B', 'C', 'Z', 'K']
# ['A', 'A', 'B', 'C', 'K', 'Z']
# ['A', 'A', 'B', 'C', 'K', 'Z']
# alphabets: ['A', 'A', 'B', 'C', 'K', 'Z'], swap_count: 5
