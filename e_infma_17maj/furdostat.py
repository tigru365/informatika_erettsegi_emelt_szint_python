""" Fürdő (2017.05.15-id.ny.)
"""

from pathlib import Path

# 1. feladat


def idobol_masodperc(ora: int, perc: int, masodperc: int) -> int:
    """ A függvény az óra, perc, másodperc paraméterekkel megadott idő értékét
    másodpercben adja vissza
    """
    return ora * 3600 + perc * 60 + masodperc


mozgasok: list[dict[str, int | bool]] = []

fajl = Path.cwd() / "forras" / "furdoadat.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = list(map(int, sor.strip().split()))
        mozgas: dict[str, int | bool] = {
            'azon': adatok[0],
            'reszleg': adatok[1],
            'kilep': bool(adatok[2]),
            'ido': idobol_masodperc(adatok[3], adatok[4], adatok[5]),
        }
        mozgasok.append(mozgas)
# print(f"{mozgasok = }")

# 2. feladat
print("2. feladat")


def masodpercbol_ido(masodperc: int) -> str:
    """ A függvény a paraméterként másodpercben megadott idő
    értékét adja vissza 'óó:pp:mm' formában
    """
    h, s = divmod(masodperc, 3600)
    m, s = divmod(s, 60)
    return f"{h}:{m}:{s}"


oltozobol = [m for m in mozgasok if m['kilep'] and m['reszleg'] == 0]

print(f"Az első vendég {masodpercbol_ido(oltozobol[0]['ido'])}"
      + "-kor lépett ki az öltözőből.")
print(f"Az utolsó vendég {masodpercbol_ido(oltozobol[-1]['ido'])}"
      + "-kor lépett ki az öltözőből.\n")

# 3. feladat
print("3. feladat")

vendegek = {m['azon'] for m in mozgasok}
bekilepesek = [len([m for m in mozgasok if m['azon'] == v]) for v in vendegek]
egyet_hasznalt = [bk for bk in bekilepesek if bk == 4]

print(f"A fürdőben {len(egyet_hasznalt)} vendég járt csak egy részlegen.\n")

# 4. feladat
print("4. feladat")

vendeg_bekilepesek = {
    v: [m['ido'] for m in mozgasok if m['azon'] == v and m['reszleg'] == 0]
    for v in vendegek}
vendegidok = [(v, idok[0], idok[1], idok[1] - idok[0])
              for v, idok in vendeg_bekilepesek.items()]
max_ido = max(vendegidok, key=lambda idok: idok[3])

print("A legtöbb időt eltöltő vendég:")
print(f"{max_ido[0]}. vendég {masodpercbol_ido(max_ido[3])}\n")

# 5. feladat
print("5. feladat")

osszesen = len([v for v in vendegidok
                if idobol_masodperc(6, 0, 0) <= v[1]
                < idobol_masodperc(9, 0, 0)])
print(f"6-9 óra között {osszesen} vendég")

osszesen = len([v for v in vendegidok
                if idobol_masodperc(9, 0, 0) <= v[1]
                < idobol_masodperc(16, 0, 0)])
print(f"9-16 óra között {osszesen} vendég")

osszesen = len([v for v in vendegidok
                if idobol_masodperc(16, 0, 0) <= v[1]
                < idobol_masodperc(20, 0, 0)])
print(f"16-20 óra között {osszesen} vendég\n")

# 6. feladat
szauna_vendegek = {
    v: [m['ido'] for m in mozgasok if m['azon'] == v and m['reszleg'] == 2]
    for v in vendegek}

fajl = Path.cwd() / "szauna.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for vendeg, idopont in szauna_vendegek.items():
        if idopont:
            osszesen = 0
            for i in range(0, len(idopont) - 1, 2):
                osszesen += idopont[i + 1] - idopont[i]
            celfajl.write(f"{vendeg} {masodpercbol_ido(osszesen)}\n")

# 7. feladat
print("7. feladat")

osszesen = len({m['azon'] for m in mozgasok if m['reszleg'] == 1})
print(f"Uszoda: {osszesen}")

osszesen = len({m['azon'] for m in mozgasok if m['reszleg'] == 2})
print(f"Szaunák: {osszesen}")

osszesen = len({m['azon'] for m in mozgasok if m['reszleg'] == 3})
print(f"Gyógyvizes medencék: {osszesen}")

osszesen = len({m['azon'] for m in mozgasok if m['reszleg'] == 4})
print(f"Strand: {osszesen}")
