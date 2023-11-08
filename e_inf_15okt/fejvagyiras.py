""" Fej vagy írás (2015.10.16)
"""

from pathlib import Path
import random

random.seed()

# 1. feladat
print("1. feladat")


def penzfeldobas() -> str:
    """ A függvény véletlenszerűen fejjel
    vagy írással ("F" vagy "I") tér vissza
    """
    return random.choice('FI')


print(f"A pénzfeldobás eredménye: {penzfeldobas()}")

# 2. feladat
print("2. feladat")

tipp = input("Tippeljen! (F/I)= ")
# tipp = "I"

dobas = penzfeldobas()
print(f"A tipp {tipp}, a dobás eredménye {dobas} volt.")

if dobas == tipp:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")

# 3. feladat
print("3. feladat")

fajl = Path.cwd() / "forras" / "kiserlet.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    dobasok_osszesen = 0

    for sor in forrasfajl:
        dobasok_osszesen += 1

print(f"A kísérlet {dobasok_osszesen} dobásból állt.")

# 4. feladat
print("4. feladat")

with fajl.open(encoding="ascii") as forrasfajl:
    dobasok_osszesen = 0
    fejek_osszesen = 0

    for sor in forrasfajl:
        dobas = sor.strip()
        dobasok_osszesen += 1

        if dobas == "F":
            fejek_osszesen += 1

print("A kísérlet során a fej relatív gyakorisága "
      + f"{fejek_osszesen / dobasok_osszesen:.2%} volt.")

# 5. feladat
print("5. feladat")

with fajl.open(encoding="ascii") as forrasfajl:
    ket_fej = 0
    ket_fej_egymas_utan = list("IFFI")
    negy_dobas = []

    for sor in forrasfajl:
        dobas = sor.strip()
        if len(negy_dobas) == 4:
            negy_dobas.pop(0)
        negy_dobas.append(dobas)

        if negy_dobas == ket_fej_egymas_utan:
            ket_fej += 1

print(f"A kísérlet során {ket_fej} alkalommal dobtak "
      + "pontosan két fejet egymás után.")

# 6. feladat
print("6. feladat")

with fajl.open(encoding="ascii") as forrasfajl:
    max_fejek = 0
    hanyadik_dobas = 0
    fejek = 0

    for i, sor in enumerate(forrasfajl):
        dobas = sor.strip()
        if dobas == "F":
            fejek += 1
            if fejek > max_fejek:
                max_fejek = fejek
                hanyadik_dobas = i + 2 - max_fejek
        else:
            fejek = 0

print(f"A leghosszabb tisztafej sorozat {max_fejek} tagból áll, "
      + f"kezdete a(z) {hanyadik_dobas}. dobás.")

# 7. feladat
sorozat = [''.join([penzfeldobas() for __ in range(4)]) for _ in range(1000)]

tisztafej_fej = sorozat.count("FFFF")
tisztafej_iras = sorozat.count("FFFI")

fajl = Path.cwd() / "dobasok.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    celfajl.write(f"FFFF: {tisztafej_fej}, FFFI: {tisztafej_iras}\n")

    for i, sor in enumerate(sorozat):
        sor += (' ' if i < 999 else '\n')
        celfajl.write(sor)
