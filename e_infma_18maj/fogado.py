""" Fogadóóra (2018.05.14-id.ny.)
"""

from pathlib import Path

# 1. feladat
foglalasok: list[dict[str, str]] = []

fajl = Path.cwd() / "forras" / "fogado.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()

        f_datum, f_ido = adatok[3].split("-")
        foglalas = {
            'nev': f"{adatok[0]} {adatok[1]}",
            'idopont': adatok[2],
            'f_datum': f_datum,
            'f_ido': f_ido,
        }
        foglalasok.append(foglalas)
# print(f"{foglalasok = }")

# 2. feladat
print("2. feladat")

print(f"Foglalások száma: {len(foglalasok)}\n")

# 3. feladat
print("3. feladat")

nev = input("Adjon meg egy nevet: ")
# nev = "Nagy Ferenc"

foglalasok_szama = len([f for f in foglalasok if f['nev'] == nev])

if foglalasok_szama:
    print(f"{nev} néven {foglalasok_szama} időpontfoglalás van.\n")
else:
    print("A megadott néven nincs időpontfoglalás.\n")

# 4. feladat
print("4. feladat")

idopont = input("Adjon meg egy érvényes időpontot (pl. 17:10): ")
# idopont = "17:40"

tanarok = [f['nev'] for f in foglalasok if f['idopont'] == idopont]

fajl = Path.cwd() / f"{idopont.replace(':', '')}.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for nev in sorted(tanarok):
        print(nev)
        celfajl.write(f"{nev}\n")
print()

# 5. feladat
print("5. feladat")

foglalas = min(foglalasok, key=lambda f: f['f_datum'] + f['f_ido'])

print(f"Tanár neve: {foglalas['nev']}")
print(f"Foglalt időpont: {foglalas['idopont']}")
print(f"Foglalás ideje: {foglalas['f_datum']}-{foglalas['f_ido']}\n")

# 6. feladat
print("6. feladat")

nev = "Barna Eszter"
osszes_idopont = [f"{h:02d}:{m:02d}" for h in range(16, 18)
                  for m in range(0, 60, 10)]

tanar_foglalt = [f['idopont'] for f in foglalasok if f['nev'] == nev]
tanar_szabad = [idopont for idopont in osszes_idopont
                if idopont not in tanar_foglalt]
print("\n".join(tanar_szabad))

szabad = "18:00"
for idopont in reversed(osszes_idopont):
    if idopont in tanar_foglalt:
        break
    szabad = idopont
print(f"{nev} legkorábban távozhat: {szabad}")
