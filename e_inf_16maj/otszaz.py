""" Ötszáz (2016.05.10)
"""

from pathlib import Path

# 1. feladat
vasarlasok: list[dict[str, int]] = []

fajl = Path.cwd() / "forras" / "penztar.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    kosar: dict[str, int] = {}
    for sor in forrasfajl:
        sor = sor.strip()

        if sor == "F":
            vasarlasok.append(kosar)
            kosar = {}
        else:
            if sor in kosar:
                kosar[sor] += 1
            else:
                kosar[sor] = 1
# print(f"{vasarlasok = }")

# 2. feladat
print("2. feladat")

print(f"A fizetések száma: {len(vasarlasok)}\n")

# 3. feladat
print("3. feladat")

print(f"Az első vásárló {sum(vasarlasok[0].values())} "
      + "darab árucikket vásárolt.\n")

# 4. feladat
print("4. feladat")

sorszam = int(input("Adja meg egy vásárlás sorszámát! "))
arucikk = input("Adja meg egy árucikk nevét! ")
darab = int(input("Adja meg a vásárolt darabszámot! "))
# sorszam = 2
# arucikk = "kefe"
# darab = 2
print()

# 5. feladat
print("5. feladat")

# 5.a) feladat
for i, vasarlas in enumerate(vasarlasok):
    if arucikk in vasarlas:
        print(f"Az első vásárlás sorszáma: {i + 1}")
        break

for i, vasarlas in enumerate(reversed(vasarlasok)):
    if arucikk in vasarlas:
        print(f"Az utolsó vásárlás sorszáma: {len(vasarlasok) - i}")
        break

# 5.b) feladat
hanyszor = sum([1 for v in vasarlasok if arucikk in v])
print(f"{hanyszor} vásárlás során vettek belőle.\n")

# 6. feladat
print("6. feladat")


def ertek(darabszam: int) -> int:
    """ A függvény a darabszámhoz a fizetendő összeget rendeli
    """
    teljes_ar = 0
    if darabszam > 2:
        teljes_ar += (darabszam - 2) * 400
    if darabszam > 1:
        teljes_ar += 450
    if darabszam > 0:
        teljes_ar += 500
    return teljes_ar


print(f"{darab} darab vételekor fizetendő: {ertek(darab)}\n")

# 7. feladat
print("7. feladat")

for aru, db in vasarlasok[sorszam - 1].items():
    print(f"{db} {aru}")

# 8. feladat
fajl = Path.cwd() / "osszeg.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for sorszam, vasarlas in enumerate(vasarlasok, start=1):
        total = sum(map(ertek, vasarlas.values()))
        celfajl.write(f"{sorszam}: {total}\n")
