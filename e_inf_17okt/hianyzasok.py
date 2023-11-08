""" Hiányzások (2017.10.25)
"""

from pathlib import Path

# 1. feladat

# Adatstruktúra:
# {
#     "01.15": {
#         "Galagonya Alfonz": "OXXXXXX"
#     },
#     "01.16": {
#         "Alma Hedvig": "OOOOOIO",
#         "Galagonya Alfonz": "XXXXXXX"
#     },
#     ...
#     "06.15": {
#         "Kumkvat Hunor": "XXOXXXN"
#     }
# }
naplo: dict[str, dict[str, str]] = {}

fajl = Path.cwd() / "forras" / "naplo.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()
        if adatok[0] == "#":
            datum = f"{adatok[1]}.{adatok[2]}"
            naplo[datum] = {}
        else:
            naplo[datum][f"{adatok[0]} {adatok[1]}"] = adatok[2]
# print(f"{naplo = }")

# 2. feladat
print("2. feladat")

osszes_hianyzas = sum((len(h_dict) for h_dict in naplo.values()))
print(f"A naplóban {osszes_hianyzas} bejegyzés van.")

# 3. feladat
print("3. feladat")

orai_hianyzasok = [hianyzas for h_dict in naplo.values()
                   for hianyzas in h_dict.values()]
osszes_igazolt = sum((ora.count("X") for ora in orai_hianyzasok))
osszes_igazolatlan = sum((ora.count("I") for ora in orai_hianyzasok))

print(f"Az igazolt hiányzások száma {osszes_igazolt}, "
      + f"az igazolatlanoké {osszes_igazolatlan} óra.")

# 4. feladat

# Függvény hetnapja(honap:egesz, nap:egesz): szöveg
#     napnev[]:= ("vasarnap", "hetfo", "kedd", "szerda", "csutortok",
#                 "pentek", "szombat")
#     napszam[]:= (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
#     napsorszam:= (napszam[honap-1]+nap) MOD 7
#     hetnapja:= napnev[napsorszam]
# Függvény vége


def hetnapja(honap: int, nap: int) -> str:
    """ A függvény a paraméterként megadott dátumhoz (hónap, nap) megadja,
    hogy az a hét melyik napjára esik (hétfő, kedd...).
    Az alapul szolgáló év nem szökőév és január elseje hétfőre esik.
    """
    napnev = (
        "vasárnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"
    )
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap - 1] + nap) % 7
    return napnev[napsorszam]


# 5. feladat
print("5. feladat")

be_honap = int(input("A hónap sorszáma="))
be_nap = int(input("A nap sorszáma="))
# be_honap = 2
# be_nap = 3

print(f"Azon a napon {hetnapja(be_honap, be_nap)} volt.")

# 6. feladat
print("6. feladat")

nap_neve = input("A nap neve=")
sorszam = int(input("Az óra sorszáma="))
# nap_neve = "szerda"
# sorszam = 3

osszesen = 0
for datum, hianyzasok in naplo.items():
    h, n = int(datum.split(".")[0]), int(datum.split(".")[1])
    if hetnapja(h, n) == nap_neve:
        for orak in hianyzasok.values():
            if orak[sorszam - 1] in ["X", "I"]:
                osszesen += 1

print(f"Ekkor összesen {osszesen} óra hiányzás történt.")

# 7. feladat
print("7. feladat")

hianyzasok = [(nev, orak) for h_dict in naplo.values()
              for nev, orak in h_dict.items()]

tanulok = {}
for nev, orak in hianyzasok:
    if nev not in tanulok:
        tanulok[nev] = 0
    tanulok[nev] += orak.count("X") + orak.count("I")

max_hianyzas = max(tanulok.values())
legtobbet_hianyzok = [nev for nev, szam in tanulok.items()
                      if szam == max_hianyzas]

print("A legtöbbet hiányzó tanulók:", *legtobbet_hianyzok)
