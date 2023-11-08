""" eUtazás (2019.10.22)
"""

from pathlib import Path

# 1. feladat
utazasok: list[dict[str, int | str]] = []

fajl = Path.cwd() / "forras" / "utasadat.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()

        d, t = adatok[1].split("-")
        utazas: dict[str, int | str] = {
            'megallo': int(adatok[0]),
            'datum': d,
            'idopont': t,
            'azonosito': int(adatok[2]),
            'tipus': adatok[3],
            'ervenyes': adatok[4],
        }
        utazasok.append(utazas)
# print(f"{utazasok = }")

# 2. feladat
print("2. feladat")

print(f"A buszra {len(utazasok)} utas akart felszállni.")

# 3. feladat
print("3. feladat")

ervenytelen_utazasok = [u for u in utazasok
                        if u['tipus'] == "JGY" and u['ervenyes'] == "0"
                        or u['tipus'] != "JGY" and u['ervenyes'] < u['datum']]

print(f"A buszra {len(ervenytelen_utazasok)} utas nem szállhatott fel.")

# 4. feladat
print("4. feladat")

megallok = [0 for _ in range(30)]
for u in utazasok:
    megallok[u['megallo']] += 1

max_felszallo = max(megallok)
index = megallok.index(max_felszallo)

print(f"A legtöbb utas ({megallok[index]} fő) a {index}. "
      + "megállóban próbált felszállni.")

# 5. feladat
print("5. feladat")

ervenyes_utazasok = [u for u in utazasok
                     if u['tipus'] == "JGY" and u['ervenyes'] != "0"
                     or u['tipus'] != "JGY" and u['ervenyes'] >= u['datum']]

kedvezmenyes_utazasok = [u for u in ervenyes_utazasok
                         if u['tipus'] == "TAB"
                         or u['tipus'] == "NYB"]

ingyenes_utazasok = [u for u in ervenyes_utazasok
                     if u['tipus'] == "NYP"
                     or u['tipus'] == "RVS"
                     or u['tipus'] == "GYK"]

print(f"Ingyenesen utazók száma: {len(ingyenes_utazasok)} fő")
print(f"A kedvezményesen utazók száma: {len(kedvezmenyes_utazasok)} fő")

# 6. feladat

# Függvény napokszama(e1:egész, h1:egész, n1: egész, e2:egész, h2: egész, n2: egész): egész
#     h1 = (h1 + 9) MOD 12
#     e1 = e1 - h1 DIV 10
#     d1= 365*e1 + e1 DIV 4 - e1 DIV 100 + e1 DIV 400 + (h1*306 + 5) DIV 10 + n1 - 1
#     h2 = (h2 + 9) MOD 12
#     e2 = e2 - h2 DIV 10
#     d2= 365*e2 + e2 DIV 4 - e2 DIV 100 + e2 DIV 400 + (h2*306 + 5) DIV 10 + n2 - 1
#     napokszama:= d2-d1
# Függvény vége


def napokszama(e1: int, h1: int, n1: int, e2: int, h2: int, n2: int) -> int:
    """ A függvény a paraméterként megadott két dátumhoz (év, hónap, nap)
    megadja a közöttük eltelt napok számát
    """
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) \
        // 10 + n1 - 1

    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) \
        // 10 + n2 - 1

    return d2 - d1


# 7. feladat


def felbont_datum(datum: str) -> tuple[int, int, int]:
    """ A függvény (ev, ho, nap) tuple-ben visszaadja
    az összefűzött szövegként megadott dátumot
        például: "19990513" -> (1999, 5, 13)
    """
    return int(datum[:-4]), int(datum[-4:-2]), int(datum[-2:])


fajl = Path.cwd() / "figyelmeztetes.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for utazas in ervenyes_utazasok:
        if utazas['tipus'] != "JGY":
            utazas_datuma = felbont_datum(utazas['datum'])
            ervenyes = felbont_datum(utazas['ervenyes'])
            napok = napokszama(*utazas_datuma, *ervenyes)
            if napok <= 3:
                celfajl.write(
                    f"{utazas['azonosito']} {ervenyes[0]:02d}-"
                    + f"{ervenyes[1]:02d}-{ervenyes[2]:02d}\n"
                )
