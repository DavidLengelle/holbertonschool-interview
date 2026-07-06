# Making Change

Given a pile of coins of different values, determine the **fewest number of
coins** needed to meet a given total amount.

## Task

Complete the function `makeChange(coins, total)` that returns the minimum number
of coins required to reach `total`.

- `coins` is a list of the values of the coins in your possession.
- The value of a coin will always be an integer greater than 0.
- You can assume you have an infinite number of each denomination.
- Return `0` if `total` is `0` or less.
- Return `-1` if `total` cannot be met by any combination of the coins.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the `pycodestyle` style (version 1.7.x)
- All files must be executable

## Approach

Bottom-up dynamic programming.

`dp[i]` stores the minimum number of coins needed to make amount `i`. Amounts are
solved from `0` up to `total`, so every smaller amount is already known when a
larger one is computed:

```
dp[0] = 0
dp[i] = min(dp[i - coin] + 1) for every coin <= i
```

If `dp[total]` is never reached, the total is impossible and the function returns
`-1`.

Time complexity: `O(total * len(coins))`.

## Prototype

```python
def makeChange(coins: list, total: int) -> int:
```

## Usage

```python
#!/usr/bin/python3
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
```

Output:

```
7
-1
```

## Files

| File                   | Description                        |
| ---------------------- | ---------------------------------- |
| `0-making_change.py`   | The `makeChange` function          |

## Author

David Lengelle - Holberton School
