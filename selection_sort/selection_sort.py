#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def selection_sort(inputs):
    result = list(inputs)
    size = len(result)
    swap_count = 0
    for i in range(0, size):
        min_index = i
        for j in range(i, size):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
        if i != min_index:
            swap_count += 1
        print(result)

    return result, swap_count


def main():
    numbers = [8, 3, 1, 5, 2, 1]
    print(numbers)
    numbers_result = selection_sort(numbers)
    print("numbers: {0}, swap_count: {1}".format(
        numbers_result[0],
        numbers_result[1]
    ))

    print()

    alphabets = ["C", "B", "A", "Z", "A", "K"]
    alphabets_result = selection_sort(alphabets)
    print("alphabets: {0}, swap_count: {1}".format(
        alphabets_result[0],
        alphabets_result[1]
    ))


if __name__ == "__main__":
    main()

# [8, 3, 1, 5, 2, 1]
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
