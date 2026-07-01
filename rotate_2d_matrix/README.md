# Rotate 2D Matrix

Étant donné une matrice 2D `n x n`, la tourner de 90 degrés dans le sens
horaire, **en place** (sans créer une nouvelle matrice, sans rien retourner).

## L'idée

Imagine la matrice comme une photo carrée posée sur une table.

1. **Transposer** la photo, c'est la plier le long de sa diagonale
   (du coin en haut à gauche au coin en bas à droite). Chaque case au-dessus
   de la diagonale échange sa place avec sa case miroir en dessous.
2. **Inverser chaque ligne**, c'est comme retourner la photo de gauche à
   droite (un effet miroir horizontal).

Faire ces deux étapes l'une après l'autre revient exactement à faire
pivoter la photo de 90 degrés dans le sens horaire, sans jamais avoir besoin
d'une deuxième matrice pour stocker le résultat.

## Contenu

| Fichier                | Description                          |
| ----------------------- | ------------------------------------ |
| `0-rotate_2d_matrix.py` | Fonction `rotate_2d_matrix(matrix)` |

## Utilisation

```python
#!/usr/bin/python3
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

```console
$ ./test.py
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Prototype

```python
def rotate_2d_matrix(matrix)
```

- **Paramètre** : `matrix`, une matrice carrée (liste de listes).
- **Retour** : rien, la matrice est modifiée en place.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- Style **PEP 8** (version 1.7.x)
- Aucun module importé
- Chaque fichier se termine par une nouvelle ligne
- Première ligne : `#!/usr/bin/python3`
- Fichiers exécutables

## Auteur

David Lengelle — [Holberton School](https://www.holbertonschool.com/)
