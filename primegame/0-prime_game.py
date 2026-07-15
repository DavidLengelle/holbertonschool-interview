#!/usr/bin/python3


def isWinner(x, nums):
    if x < 1 or nums is None:
        return None

    n = max(nums)

    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + sieve[i]

    maria = 0
    ben = 0
    for num in nums:
        if prime_count[num] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
