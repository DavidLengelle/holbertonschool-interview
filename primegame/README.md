# Prime Game

An interview-style algorithm project: determine the winner of a prime-number
removal game played over several rounds.

## The game

Maria and Ben play with the set of consecutive integers from `1` up to and
including `n`. On each turn a player:

1. chooses a **prime** number still in the set,
2. removes that prime and all of its multiples from the set.

The player who cannot make a move loses the round. Maria always plays first and
both players play optimally.

They play `x` rounds (each round may use a different `n`). The goal is to find
out who wins the most rounds.

## Key insight

Whenever a player picks a prime `p`, the only prime removed from the set is `p`
itself (every other multiple of `p` is a composite number, which was never
choosable). So each turn removes exactly **one** usable prime.

The whole game therefore comes down to the count of primes between `1` and `n`:

- an **odd** number of primes → Maria (she plays first) takes the last one and wins,
- an **even** number of primes → Ben wins.

The primes up to the largest `n` are found once with a **Sieve of
Eratosthenes**, and a cumulative count gives the number of primes `<= n` for
every round in constant time.

## Function

```python
def isWinner(x, nums)
```

- `x`: number of rounds.
- `nums`: list of `n` values, one per round.
- Returns the name of the player who won the most rounds (`"Maria"` or
  `"Ben"`), or `None` if it is a tie / cannot be determined.

## Usage

```
$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

$ ./main_0.py
Winner: Ben
```

## Requirements

- Ubuntu 14.04 LTS, `python3` (version 3.4.3)
- All files end with a new line
- First line of every file: `#!/usr/bin/python3`
- Code follows the PEP 8 style (version 1.7.x)
- All files are executable
- No packages may be imported

## Files

| File | Description |
| ---- | ----------- |
| `0-prime_game.py` | Contains the `isWinner` function |

## Author

David Lengellé
