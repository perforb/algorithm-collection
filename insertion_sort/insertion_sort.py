#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(numbers):
    result = list(numbers)
    for i in range(1, len(result)):
        v = result[i]
        j = (i - 1)
        while j >= 0 and result[j] > v:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = v
        print(result)

    return result


def another_insertion_sort(numbers):
    result = list(numbers)
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
    result = insertion_sort(numbers)
    print("result: {0}".format(result))


if __name__ == "__main__":
    main()

# [3, 8, 1, 5, 2, 1]
# [1, 3, 8, 5, 2, 1]
# [1, 3, 5, 8, 2, 1]
# [1, 2, 3, 5, 8, 1]
# [1, 1, 2, 3, 5, 8]
# result: [1, 1, 2, 3, 5, 8]
