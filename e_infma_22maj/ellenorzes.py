""" Szakaszsebesség-ellenőrzés (2022.05.16-id.ny.)
"""

from pathlib import Path

# 1. feladat


def ido_masodpercben(i_ora: int, i_perc: int, i_mperc: int, i_tized: int) \
        -> float:
    """ A föggvény visszaadja a megadott időt másodpercben
    """
    return i_ora * 3600 + i_perc * 60 + i_mperc + i_tized / 1000


meresek: list[dict[str, str | float]] = []

fajl = Path.cwd() / "forras" / "meresek.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()

        meres: dict[str, str | float] = {
            'rendszam': adatok[0],
            'belepes': ido_masodpercben(
                int(adatok[1]),
                int(adatok[2]),
                int(adatok[3]),
                int(adatok[4]),
            ),
            'kilepes': ido_masodpercben(
                int(adatok[5]),
                int(adatok[6]),
                int(adatok[7]),
                int(adatok[8]),
            ),
        }
        meresek.append(meres)
# print(f"{meresek = }")

# 2. feladat
print("2. feladat")

print(f"A mérés során {len(meresek)} jármű adatait rögzítették.\n")

# 3. feladat
print("3. feladat")

kilenc_elott = len(
    [meres for meres in meresek if meres['kilepes'] // 3600 < 9])
print(f"9 óra előtt {kilenc_elott} jármű haladt el a végponti mérőnél.\n")

# 4. feladat
print("4. feladat")

ora_perc = input("Adjon meg egy óra és perc értéket! ").split()
# ora_perc = "8 20"
ora = int(ora_perc[0])
perc = int(ora_perc[1])

ido_be = ido_masodpercben(ora, perc, 0, 0)
ido_ki = ido_masodpercben(ora, perc + 1, 0, 0)

szamlalo = 0
for meres in meresek:
    if ido_be <= meres['belepes'] < ido_ki:
        szamlalo += 1

print(f"\ta. A kezdeti méréspontnál elhaladt járművek száma: {szamlalo}")

szamlalo = 0
for meres in meresek:
    if meres['belepes'] < ido_ki and meres['kilepes'] > ido_be:
        szamlalo += 1
print(f"\tb. A forgalomsűrűség: {szamlalo / 10:.1f}\n")

# 5. feladat
print("5. feladat")

for meres in meresek:
    meres['atlag'] = 10 / ((meres['kilepes'] - meres['belepes']) / 3600)

leggyorsabb = max(meresek, key=lambda m: m['atlag'])

szamlalo = 0
for meres in meresek:
    if meres['belepes'] <= leggyorsabb['belepes'] \
            and meres['kilepes'] > leggyorsabb['kilepes']:
        szamlalo += 1

print("A legnagyobb sebességgel haladó jármű")
print(f"\trendszáma: {leggyorsabb['rendszam']}")
print(f"\tátlagsebessége: {int(leggyorsabb['atlag'])} km/h")
print(f"\táltal lehagyott járművek száma: {szamlalo}\n")

# 6. feladat
print("6. feladat")

gyorshajtok = [meres for meres in meresek if meres['atlag'] > 90.0]
print(f"A járművek {len(gyorshajtok) / len(meresek):.2%}-a volt gyorshajtó.\n")

# 7. feladat


def buntetes(atlagsebesseg: float) -> int:
    """ A függvény az átlagsebesség mértékétől függő
    büntetési összeggel tér vissza
    """
    if atlagsebesseg > 151.0:
        return 200_000
    if atlagsebesseg > 136.0:
        return 60_000
    if atlagsebesseg > 121.0:
        return 45_000
    if atlagsebesseg > 104.0:
        return 30_000
    return 0


buntetettek = [meres for meres in gyorshajtok if meres['atlag'] > 104.0]

fajl = Path.cwd() / "buntetes.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for jarmu in buntetettek:
        celfajl.write(
            f"{jarmu['rendszam']}\t{int(jarmu['atlag'])} km/h\t"
            + f"{buntetes(jarmu['atlag'])} Ft\n")

print("A fájl elkészült.")
