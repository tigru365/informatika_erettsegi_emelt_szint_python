""" Szállítószalag (2023.05.22-id.ny.)
"""

from pathlib import Path

# 1. feladat
szallitasok: list[dict[str, int]] = []

fajl = Path.cwd() / "forras" / "szallit.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    sz_hossz, sz_ido = [int(x) for x in forrasfajl.readline().split()]
    for sor in forrasfajl:
        adatok = list(map(int, sor.split()))

        rekesz = {
            'indul': adatok[0],
            'honnan': adatok[1],
            'hova': adatok[2],
            'tomeg': adatok[3],
        }
        szallitasok.append(rekesz)
# print(f"{szallitasok = }")

# 2. feladat
print("2. feladat")

adatsor = int(input("Adja meg, melyik adatsorra kíváncsi! "))
# adatsor = 3

print(f"Honnan: {szallitasok[adatsor - 1]['honnan']} "
      + f"Hova: {szallitasok[adatsor - 1]['hova']}\n")

# 3. feladat


def tav(szalaghossz: int, indulashelye: int, erkezeshelye: int) -> int:
    """ A függvény megadja a szállítás távolságát a szalag hosszának,
    valamint az indulási és a célhelynek ismeretében
    """
    if indulashelye > erkezeshelye:
        return szalaghossz - indulashelye + erkezeshelye
    return erkezeshelye - indulashelye


# 4. feladat
print("4. feladat")

for sz in szallitasok:
    sz['tavolsag'] = tav(sz_hossz, sz['honnan'], sz['hova'])

max_tav = max(szallitasok, key=lambda x: x['tavolsag'])['tavolsag']
print(f"A legnagyobb távolság: {max_tav}")

max_tav_sorszamok = [sor for sor, t in enumerate(szallitasok, start=1)
                     if t['tavolsag'] == max_tav]
print("A maximális távolságú szállítások sorszáma:",
      *max_tav_sorszamok, end="\n\n")

# 5. feladat
print("5. feladat")

ossz_tomeg = 0
for sz in szallitasok:
    if sz['honnan'] > sz['hova'] != 0 and sz['honnan'] != 0:
        ossz_tomeg += sz['tomeg']

print(f"A kezdőpont előtt elhaladó rekeszek össztömege: {ossz_tomeg}\n")

# 6. feladat
print("6. feladat")

idopont = int(input("Adja meg a kívánt időpontot! "))
# idopont = 300

sorszamok = []
for sor, sz in enumerate(szallitasok, start=1):
    if sz['indul'] <= idopont < sz['indul'] + sz['tavolsag'] * sz_ido:
        sorszamok.append(str(sor))

print("A szállított rekeszek halmaza: "
      + f"{' '.join(sorszamok) if sorszamok else 'üres'}")

# 7. feladat
fajl = Path.cwd() / "tomeg.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for hely in range(1, 501):
        tomeg = sum(sz['tomeg'] for sz in szallitasok if sz['honnan'] == hely)
        if tomeg:
            celfajl.write(f"{hely} {tomeg}\n")
