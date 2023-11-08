""" Tantárgyfelosztás (2019.05.13-id.ny.)
"""

from pathlib import Path

# 1. feladat

# Adatstruktúra:
# {
#     "Albatrosz Aladin": [
#         {
#             "targy": "biologia",
#             "osztaly": "9.a",
#             "oraszam": 2
#         },
#         {
#             "targy": "kemia",
#             "osztaly": "9.a",
#             "oraszam": 2
#         },
#         ...
#     ],
#     "Antilop Anett": [
#         {
#             "targy": "testneveles",
#             "osztaly": "9.a",
#             "oraszam": 5
#         },
#         ...
#     ],
#     ...
# }
beosztasok: dict[str, list[dict[str, str | int]]] = {}

fajl = Path.cwd() / "forras" / "beosztas.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    adatok: list[str] = []
    for sor in forrasfajl:
        adatok.append(sor.strip())
        if len(adatok) == 4:
            tanar = adatok[0]
            tanora: dict[str, str | int] = {
                'targy': adatok[1],
                'osztaly': adatok[2],
                'oraszam': int(adatok[3]),
            }
            if tanar not in beosztasok:
                beosztasok[tanar] = []
            beosztasok[tanar].append(tanora)
            adatok = []
# print(f"{beosztasok = }")

# 2. feladat
print("2. feladat")

orak = [ora for tanorak in beosztasok.values() for ora in tanorak]  # flatten
print(f"A fájlban {len(orak)} bejegyzés van.")

# 3. feladat
print("3. feladat")

osszesen = sum(ora['oraszam'] for ora in orak)
print(f"Az iskolában a heti összóraszám: {osszesen}")

# 4. feladat
print("4. feladat")

tanar = input("Egy tanár neve= ")
# tanar = "Albatrosz Aladin"

osszesen = sum(ora['oraszam'] for ora in beosztasok[tanar])
print(f"A tanár heti óraszáma: {osszesen}")

# 5. feladat
fajl = Path.cwd() / "of.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for tanar, tanorak in beosztasok.items():
        for ora in tanorak:
            if ora['targy'] == "osztalyfonoki":
                celfajl.write(f"{ora['osztaly']} - {tanar}\n")

# 6. feladat
print("6. feladat")

osztaly = input("Osztály= ")
tantargy = input("Tantárgy= ")
# osztaly = "10.b"
# tantargy = "kemia"

szamlalo = sum(1 for ora in orak
               if ora['osztaly'] == osztaly and ora['targy'] == tantargy)
if szamlalo == 1:
    print("Osztályszinten tanulják.")
else:
    print("Csoportbontásban tanulják.")

# 7. feladat
print("7. feladat")

print(f"Az iskolában {len(beosztasok)} tanár tanít.")
