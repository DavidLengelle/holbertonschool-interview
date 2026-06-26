# Star Wars API

Scripts that interact with the [Star Wars API](https://swapi-api.hbtn.io/) using
Node.js and the `request` module.

## Requirements

- Ubuntu 14.04 LTS
- Node.js (version 10.14.x)
- `request` module
- Code is `semistandard` compliant (Standard rules + semicolons)
- All files are executable and start with `#!/usr/bin/node`

## Installation

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Files

| File | Description |
| ---- | ----------- |
| `0-starwars_characters.js` | Prints all characters of a Star Wars movie, one name per line, in the order of the `characters` list of the `/films/` endpoint |

## Usage

The first positional argument is the Movie ID.

```
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Author

- David Lengelle
