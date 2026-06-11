# UTF-8 Validation

Détermine si une liste d'entiers représente un encodage **UTF-8** valide.

Chaque entier représente **un octet** (byte). Seuls les **8 bits de poids faible**
de chaque entier sont pris en compte. Un caractère UTF-8 occupe **1 à 4 octets**.

## L'idée

Un caractère se lit comme un petit **train** :

- le **premier octet** est la **locomotive** : ses bits de gauche annoncent combien
  d'octets suivent ;
- les octets suivants sont des **wagons** (octets de continuation), qui commencent
  tous par `10`.

| Début de l'octet | Type              | Octets qui suivent |
| ---------------- | ----------------- | ------------------ |
| `0xxxxxxx`       | caractère 1 octet | 0                  |
| `110xxxxx`       | locomotive        | 1                  |
| `1110xxxx`       | locomotive        | 2                  |
| `11110xxx`       | locomotive        | 3                  |
| `10xxxxxx`       | wagon             | —                  |

Le train est valide si :

- un wagon n'apparaît **que** quand une locomotive l'attend ;
- aucune locomotive n'arrive **au milieu** d'un train ;
- à la fin de la liste, **plus aucun wagon n'est attendu**.

## Contenu

| Fichier              | Description                         |
| -------------------- | ----------------------------------- |
| `0-validate_utf8.py` | Fonction `validUTF8(data)`          |
| `0-main.py`          | Fichier de test fourni par l'énoncé |

## Utilisation

```python
#!/usr/bin/python3
validUTF8 = __import__('0-validate_utf8').validUTF8

print(validUTF8([65]))                    # True
print(validUTF8([197, 130]))              # True  (caractère 2 octets)
print(validUTF8([240, 162, 138, 147]))    # True  (caractère 4 octets)
print(validUTF8([229, 65, 127, 256]))     # False
print(validUTF8([235, 140]))              # False (wagon manquant)
```

```console
$ ./0-main.py
True
True
False
```

## Prototype

```python
def validUTF8(data)
```

- **Paramètre** : `data`, une liste d'entiers (un par octet).
- **Retour** : `True` si l'encodage UTF-8 est valide, sinon `False`.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- Style **PEP 8** (version 1.7.x)
- Chaque fichier se termine par une nouvelle ligne
- Première ligne : `#!/usr/bin/python3`
- Fichiers exécutables

## Auteur

David Lengelle — [Holberton School](https://www.holbertonschool.com/)
