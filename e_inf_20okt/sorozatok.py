""" Sorozatok (2020.10.28)
"""

from pathlib import Path

# 1. feladat
sorozatok: list[dict[str, str | int | bool]] = []

fajl = Path.cwd() / "forras" / "lista.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    adatok: list[str] = []
    for sor in forrasfajl:
        adatok.append(sor.strip())
        if len(adatok) == 5:
            sorozat: dict[str, str | int | bool] = {
                'datum': adatok[0],
                'cim': adatok[1],
                'resz': adatok[2],
                'hossz': int(adatok[3]),
                'megnezte': bool(int(adatok[4])),
            }
            sorozatok.append(sorozat)
            adatok = []
# print(f"{sorozatok = }")

# 2. feladat
print("2. feladat")

ismert_sorozatok = [sorozat for sorozat in sorozatok
                    if sorozat['datum'] != "NI"]

print(f"A listában {len(ismert_sorozatok)} db "
      + "vetítési dátummal rendelkező epizód van.\n")

# 3. feladat
print("3. feladat")

megnezett = [sorozat for sorozat in sorozatok if sorozat['megnezte']]

print("A listában lévő epizódok "
      + f"{len(megnezett) / len(sorozatok):.2%}-át látta.\n")

# 4. feladat
print("4. feladat")

osszesen = sum(sorozat['hossz'] for sorozat in megnezett)
szum_nap, maradek = divmod(osszesen, 24 * 60)
szum_ora, szum_perc = divmod(maradek, 60)

print(f"Sorozatnézéssel {szum_nap} napot {szum_ora} órát "
      + f"és {szum_perc} percet töltött.\n")

# 5. feladat
print("5. feladat")

datum = input("Adjon meg egy dátumot! Dátum= ")
# datum = "2017.10.18"

for sorozat in ismert_sorozatok:
    if not sorozat['megnezte'] and sorozat['datum'] <= datum:
        print(f"{sorozat['resz']}\t{sorozat['cim']}")
print()

# 6. feladat

# Függvény hetnapja(ev, ho, nap : Egész) : Szöveg
#     napok: Tömb(0..6: Szöveg)= ("v", "h", "k", "sze", "cs", "p", "szo")
#     honapok: Tömb(0..11: Egész)= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
#     Ha ho < 3 akkor ev := ev -1
#     hetnapja := napok[(ev + ev div 4 - ev div 100 + ev div 400 + honapok[ho-1] + nap) mod 7]
# Függvény vége


def hetnapja(ev: int, ho: int, nap: int) -> str:
    """ A függvény az év, hónap és nap megadása után szöveges
    eredményként visszaadja, hogy az adott nap a hét melyik napja volt.
    """
    napok = ("v", "h", "k", "sze", "cs", "p", "szo")
    honapok = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)

    if ho < 3:
        ev -= 1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400
                  + honapok[ho - 1] + nap) % 7]


# 7. feladat
print("7. feladat")

het_napja = input("Adja meg a hét egy napját (például cs)! Nap= ")
# het_napja = "cs"

cimek = set()
for sorozat in ismert_sorozatok:
    adas_ev, adas_ho, adas_nap = list(map(int, sorozat['datum'].split(".")))
    if hetnapja(adas_ev, adas_ho, adas_nap) == het_napja:
        cimek.add(sorozat['cim'])

if cimek:
    for cim in cimek:
        print(cim)
else:
    print("Az adott napon nem kerül adásba sorozat.")
print()

# 8. feladat
cimek = {sorozat['cim'] for sorozat in sorozatok}

fajl = Path.cwd() / "summa.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for cim in sorted(cimek):
        reszek = [sorozat for sorozat in sorozatok if sorozat['cim'] == cim]
        szum_hossz = sum(resz['hossz'] for resz in reszek)
        celfajl.write(f"{cim} {szum_hossz} {len(reszek)}\n")
