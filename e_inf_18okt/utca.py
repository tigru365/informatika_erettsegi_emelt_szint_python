""" Kerítés (2018.10.25)
"""

from pathlib import Path
import random
from io import StringIO

# 1. feladat
telkek: list[dict[str, bool | int | str]] = []

fajl = Path.cwd() / "forras" / "kerites.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    hsz_paratlan = 1
    hsz_paros = 2
    for sor in forrasfajl:
        adatok = sor.strip().split()

        if paratlan := bool(int(adatok[0])):
            hazszam = hsz_paratlan
            hsz_paratlan += 2
        else:
            hazszam = hsz_paros
            hsz_paros += 2

        telek: dict[str, bool | int | str] = {
            'paratlan': paratlan,
            'hossz': int(adatok[1]),
            'kerites': adatok[2],
            'hazszam': hazszam,
        }
        telkek.append(telek)
# print(f"{telkek = }")

# 2. feladat
print("2. feladat")

print(f"Az eladott telkek száma: {len(telkek)}\n")

# 3. feladat
print("3. feladat")

utolso_telek = telkek[-1]

# 3.a) feladat
print(f"A {'páratlan' if utolso_telek['paratlan'] else 'páros'} "
      + "oldalon adták el az utolsó telket.")

# 3.b) feladat
print(f"Az utolsó telek házszáma: {utolso_telek['hazszam']}\n")

# 4. feladat
print("4. feladat")

paratlan_oldal = [t for t in telkek if t['paratlan']]

for i in range(len(paratlan_oldal) - 1):
    if paratlan_oldal[i]['kerites'] not in ("#", ":"):
        if paratlan_oldal[i]['kerites'] == paratlan_oldal[i + 1]['kerites']:
            print("A szomszédossal egyezik a kerítés színe: "
                  + f"{paratlan_oldal[i]['hazszam']}\n")
            break

# 5. feladat
print("5. feladat")

hazszam = int(input("Adjon meg egy házszámot! "))
# hazszam = 83

# 5.a) feladat
telek = [t for t in telkek if t['hazszam'] == hazszam][0]
print(f"A kerítés színe / állapota: {telek['kerites']}")

# 5.b) feladat
random.seed()

szomszedok = [t['kerites'] for t in telkek
              if t['hazszam'] == hazszam - 2 or t['hazszam'] == hazszam + 2]
szomszedok.append(telek['kerites'])

szinek = [szin for sz in range(ord('A'), ord('Z') + 1)
          if (szin := chr(sz)) not in szomszedok]
# # VAGY a string könyvtár segítségével:
# from string import ascii_uppercase
# szinek = [szin for szin in ascii_uppercase if szin not in szomszedok]

print(f"Egy lehetséges festési szín: {random.choice(szinek)}")

# 6. feladat
utcakep = StringIO()
hazszamok = StringIO()

for telek in paratlan_oldal:
    utcakep.write(telek['kerites'] * telek['hossz'])
    hazszamok.write(str(telek['hazszam']).ljust(telek['hossz']))

utcakep.write("\n")
hazszamok.write("\n")

fajl = Path.cwd() / "utcakep.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    celfajl.write(utcakep.getvalue())
    celfajl.write(hazszamok.getvalue())
