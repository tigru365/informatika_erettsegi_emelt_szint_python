""" Jeladó (2022.10.25)
"""

from pathlib import Path
from math import sqrt

# 1. feladat
jelek: list[dict[str, tuple[int, ...]]] = []

fajl = Path.cwd() / "forras" / "jel.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()
        jel = {
            'ido': tuple(map(int, adatok[:3])),
            'poz': tuple(map(int, adatok[3:])),
        }
        jelek.append(jel)
# print(f"{jelek = }")

# 2. feladat
print("2. feladat")
sorszam = int(input("Adja meg a jel sorszámát! "))
# sorszam = 3

print(f"x={jelek[sorszam - 1]['poz'][0]} y={jelek[sorszam - 1]['poz'][1]}\n")

# 3. feladat


def eltelt(ido1: tuple[int, ...], ido2: tuple[int, ...]) -> int:
    """ A függvény megadja, hogy a paraméterként átadott két időpont között
    hány másodperc telik el
    """
    mp_ido1 = 3600 * ido1[0] + 60 * ido1[1] + ido1[2]
    mp_ido2 = 3600 * ido2[0] + 60 * ido2[1] + ido2[2]
    return abs(mp_ido2 - mp_ido1)


# 4. feladat
print("4. feladat")
masodperc = eltelt(jelek[0]['ido'], jelek[-1]['ido'])
ora, masodperc = divmod(masodperc, 3600)
perc, masodperc = divmod(masodperc, 60)
print(f"Időtartam: {ora}:{perc}:{masodperc}\n")

# 5. feladat
print("5. feladat")
min_x = min(jelek, key=lambda j: j['poz'][0])['poz'][0]
min_y = min(jelek, key=lambda j: j['poz'][1])['poz'][1]
max_x = max(jelek, key=lambda j: j['poz'][0])['poz'][0]
max_y = max(jelek, key=lambda j: j['poz'][1])['poz'][1]
print(f"Bal alsó: {min_x} {min_y}, jobb felső: {max_x} {max_y}\n")

# 6. feladat
print("6. feladat")
elmozdulas = 0.0
for i in range(len(jelek) - 1):
    tav = sqrt((jelek[i]['poz'][0] - jelek[i + 1]['poz'][0]) ** 2
               + (jelek[i]['poz'][1] - jelek[i + 1]['poz'][1]) ** 2)
    elmozdulas += tav
print(f"Elmozdulás: {elmozdulas:.3f} egység")

# 7. feladat
fajl = Path.cwd() / "kimaradt.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for i in range(len(jelek) - 1):
        darab_ido = 0
        darab_poz = 0

        ido_elteres = eltelt(jelek[i]['ido'], jelek[i + 1]['ido'])
        if ido_elteres > 300:
            darab_ido, maradek = divmod(ido_elteres, 300)
            if maradek == 0:
                darab_ido -= 1

        x_elteres = abs(jelek[i]['poz'][0] - jelek[i + 1]['poz'][0])
        y_elteres = abs(jelek[i]['poz'][1] - jelek[i + 1]['poz'][1])
        tav_elteres = max(x_elteres, y_elteres)
        if tav_elteres > 10:
            darab_poz, maradek = divmod(tav_elteres, 10)
            if maradek == 0:
                darab_poz -= 1

        if darab_ido or darab_poz:
            sor = f"{jelek[i + 1]['ido'][0]} {jelek[i + 1]['ido'][1]} " \
                + f"{jelek[i + 1]['ido'][2]} "
            if darab_ido >= darab_poz:
                sor += f"időeltérés {darab_ido}\n"
            else:
                sor += f"koordináta-eltérés {darab_poz}\n"
            celfajl.write(sor)
