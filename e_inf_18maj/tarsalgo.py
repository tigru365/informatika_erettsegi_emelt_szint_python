""" Társalgó (2018.05.14)
"""

from pathlib import Path

# 1. feladat
forgalom: list[dict[str, int | bool]] = []

fajl = Path.cwd() / "forras" / "ajto.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    jelen = 0
    for sor in forrasfajl:
        adatok = sor.strip().split()

        if bejovo := adatok[3] == "be":
            jelen += 1
        else:
            jelen -= 1

        szemely: dict[str, int | bool] = {
            'ido': int(adatok[0]) * 60 + int(adatok[1]),
            'azon': int(adatok[2]),
            'be': bejovo,
            'jelen': jelen,
        }
        forgalom.append(szemely)
# print(f"{forgalom = }")

# 2. feladat
print("2. feladat")

elso_belepo = [sz['azon'] for sz in forgalom if sz['be']][0]
utolso_kilepo = [sz['azon'] for sz in forgalom if not sz['be']][-1]

print(f"Az első belépő: {elso_belepo}")
print(f"Az utolsó kilépő: {utolso_kilepo}\n")

# 3. feladat
athaladasok = [[sz, 0] for sz in range(1, 101)]

for szemely in forgalom:
    athaladasok[szemely['azon'] - 1][1] += 1

fajl = Path.cwd() / "athaladas.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for szemely, bekilepesek in athaladasok:
        if bekilepesek:
            celfajl.write(f"{szemely} {bekilepesek}\n")

# 4. feladat
print("4. feladat")

jelenlevok = [a[0] for a in athaladasok if a[1] % 2]
print("A végén a társalgóban voltak:", *jelenlevok, end="\n\n")

# 5. feladat
print("5. feladat")

max_bent = max(forgalom, key=lambda sz: sz['jelen'])
ora, perc = divmod(max_bent['ido'], 60)

print(f"Például {ora}:{perc}-kor voltak a legtöbben a társalgóban.\n")

# 6. feladat
print("6. feladat")

azonosito = int(input("Adja meg a személy azonosítóját! "))
# azonosito = 22
print()

# 7. feladat
print("7. feladat")

szemely_mozgasa = [sz for sz in forgalom if sz['azon'] == azonosito]

for szemely in szemely_mozgasa:
    ora, perc = divmod(szemely['ido'], 60)
    if szemely['be']:
        print(f"{ora:02d}:{perc:02d}-", end="")
    else:
        print(f"{ora:02d}:{perc:02d}")

if szemely['be']:
    print()
print()

# 8. feladat
print("8. feladat")

osszesen = 0
ido_be = 0
ido_ki = 0
for szemely in szemely_mozgasa:
    if szemely['be']:
        ido_be = szemely['ido']
    else:
        ido_ki = szemely['ido']
        osszesen += ido_ki - ido_be

if szemely['be']:
    hol_volt = "a társalgóban volt"
    osszesen += 15 * 60 - ido_be
else:
    hol_volt = "nem volt a társalgóban"

print(f"A(z) {azonosito}. személy összesen {osszesen} percet volt bent, "
      + f"a megfigyelés végén {hol_volt}.")
