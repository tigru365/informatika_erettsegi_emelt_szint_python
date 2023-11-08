""" Építményadó (2022.05.16)
"""

from pathlib import Path

# 1. feladat
telkek: list[dict[str, str | int]] = []

fajl = Path.cwd() / "forras" / "utca.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    adatok = forrasfajl.readline().strip().split()
    nm_dij = {
        'A': int(adatok[0]),
        'B': int(adatok[1]),
        'C': int(adatok[2]),
    }

    for sor in forrasfajl:
        adatok = sor.strip().split()
        telek: dict[str, str | int] = {
            'adoszam': adatok[0],
            'utca': adatok[1],
            'hsz': adatok[2],
            'adosav': adatok[3],
            'terulet': int(adatok[4]),
        }
        telkek.append(telek)
# print(f"{telkek = }")

# 2. feladat
print(f"2. feladat. A mintában {len(telkek)} telek szerepel.")

# 3. feladat
adoszam = input("3. feladat. Egy tulajdonos adószáma: ")
# adoszam = "68396"

tulaj_telkei = [t for t in telkek if t['adoszam'] == adoszam]
if tulaj_telkei:
    for telek in tulaj_telkei:
        print(f"{telek['utca']} utca {telek['hsz']}")
else:
    print("Nem szerepel az adatállományban.")

# 4. feladat


def ado(adosavok: dict[str, int], adosav: str, alapterulet: int) -> int:
    """ A függvény megadja egy építmény után fizetendő adót
    az építmény alapterülete és az adósáv függvényében
    """
    telekado = adosavok[adosav] * alapterulet
    if telekado < 10000:
        return 0
    return telekado


# 5. feladat
print("5. feladat")
for sav in nm_dij:
    telekadok = [ado(nm_dij, sav, t['terulet']) for t in telkek
                 if t['adosav'] == sav]
    print(f"{sav} sávba {len(telekadok)} telek esik, "
          + f"az adó {sum(telekadok)} Ft.")

# 6. feladat
print("6. feladat. A több sávba sorolt utcák:")
utcak = {t['utca'] for t in telkek}
for utca in sorted(utcak):
    savok = {t['adosav'] for t in telkek if t['utca'] == utca}
    if len(savok) > 1:
        print(utca)

# 7. feladat
adoszamok = {t['adoszam'] for t in telkek}

fajl = Path.cwd() / "fizetendo.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for adoszam in sorted(adoszamok):
        adok = [ado(nm_dij, t['adosav'], t['terulet']) for t in telkek
                if t['adoszam'] == adoszam]
        celfajl.write(f"{adoszam} {sum(adok)}\n")
