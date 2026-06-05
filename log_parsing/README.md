# Log Parsing

A Python script that reads logs from standard input line by line and computes
metrics on the fly.

## Input format

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Lines that do not match this format are skipped.

## Output

Every 10 lines, and on a keyboard interruption (`CTRL + C`), the script prints:

- the total file size accumulated so far
- the number of lines for each status code (200, 301, 400, 401, 403, 404, 405,
  500), in ascending order

## Usage

```
./0-generator.py | ./0-stats.py
```

## Files

- `0-stats.py` — the log parsing script
