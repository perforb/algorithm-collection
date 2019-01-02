# recursive(very heavy)
def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


memo = {
    0: 1,
    1: 1,
}


# memorization(fast)
def fib2(n):
    if n in memo:
        return memo[n]
    memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]


# loop(fast)
def fib3(n):
    if n < 3:
        return 1
    numbers = [0] * n
    numbers[0] = 1
    numbers[1] = 1
    for i in range(2, n):
        numbers[i] = numbers[i - 2] + numbers[i - 1]
    return numbers[-1]


if __name__ == "__main__":
    for n in range(int(input())):
        print(fib2(n))
