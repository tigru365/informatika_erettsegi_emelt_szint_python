""" Meteorológiai jelentés (2020.05.18)
"""

from pathlib import Path

# 1. feladat
meresek: list[dict[str, str | int]] = []

fajl = Path.cwd() / "forras" / "tavirathu13.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()

        meres: dict[str, str | int] = {
            'telep': adatok[0],
            'ido': adatok[1],
            'szel': adatok[2],
            'fok': int(adatok[3]),
        }
        meresek.append(meres)
# print(f"{meresek = }")

# 2. feladat
print("2. feladat")


def idopont(ido: str) -> str:
    """A függvény visszaadja az ido parameterben
    kapott szöveget 'óó:pp' formában"""
    return f"{ido[:2]}:{ido[-2:]}"


telepules = input("Adja meg egy település kódját! Település: ")
# telepules = "SM"

utolso_meres_ideje = max(meres['ido'] for meres in meresek
                         if meres['telep'] == telepules)
print("Az utolsó mérési adat a megadott településről "
      + f"{idopont(utolso_meres_ideje)}-kor érkezett.")

# 3. feladat
print("3. feladat")

min_fok = min(meres['fok'] for meres in meresek)
min_meres = [meres for meres in meresek if meres['fok'] == min_fok][0]
telepules = min_meres['telep']
meres_ideje = idopont(min_meres['ido'])
fok = min_meres['fok']
print(f"A legalacsonyabb hőmérséklet: {telepules} {meres_ideje} {fok} fok.")

max_fok = max(meres['fok'] for meres in meresek)
max_meres = [meres for meres in meresek if meres['fok'] == max_fok][0]
telepules = max_meres['telep']
meres_ideje = idopont(max_meres['ido'])
fok = max_meres['fok']
print(f"A legmagasabb hőmérséklet: {telepules} {meres_ideje} {fok} fok.")

# 4. feladat
print("4. feladat")

szelcsend = [meres for meres in meresek if meres['szel'] == "00000"]
if szelcsend:
    for meres in szelcsend:
        print(f"{meres['telep']} {idopont(meres['ido'])}")
else:
    print("Nem volt szélcsend a mérések idején.")

# 5. feladat
print("5. feladat")

telepulesek = {meres['telep'] for meres in meresek}

for telep in telepulesek:
    orak = set()
    osszesen = 0
    darab = 0
    min_fok = 100
    max_fok = -100

    for meres in [m for m in meresek if m['telep'] == telep]:
        ora = int(meres['ido'][:2])
        if ora in (1, 7, 13, 19):
            orak.add(ora)
            osszesen += meres['fok']
            darab += 1
        if meres['fok'] < min_fok:
            min_fok = meres['fok']
        if meres['fok'] > max_fok:
            max_fok = meres['fok']

    ingadozas = max_fok - min_fok
    if len(orak) == 4:
        print(f"{telep} Középhőmérséklet: {round(osszesen / darab)}; "
              + f"Hőmérséklet-ingadozás: {ingadozas}")
    else:
        print(f"{telep} NA; Hőmérséklet-ingadozás: {ingadozas}")

# 6. feladat
print("6. feladat")

for telep in sorted(telepulesek):
    fajl = Path.cwd() / f"{telep}.txt"
    with fajl.open("w", encoding="utf-8") as celfajl:
        celfajl.write(f"{telep}\n")

        for meres in [m for m in meresek if m['telep'] == telep]:
            szel = int(meres['szel'][-2:])
            celfajl.write(f"{idopont(meres['ido'])} {'#' * szel}\n")

print("A fájlok elkészültek.")
