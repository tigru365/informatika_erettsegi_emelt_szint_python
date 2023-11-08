""" RGB színek (2023.05.22)
"""

from pathlib import Path

# 1. feladat

# Adatstruktúra:
# [
#     [
#         {
#             "R": 0,
#             "G": 85,
#             "B": 112
#         },
#         {
#             "R": 0,
#             "G": 86,
#             "B": 113
#         },
#         ...
#     ],
#     ...
#     [
#         ...
#         {
#             "R": 35,
#             "G": 131,
#             "B": 147
#         }
#     ]
# ]
keppontok: list[list[dict[str, int]]] = []

fajl = Path.cwd() / "forras" / "kep.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sz_sor in forrasfajl:
        pontok = sz_sor.split()
        sor: list[dict[str, int]] = []
        for i in range(0, len(pontok), 3):
            pont = {
                'R': int(pontok[i]),
                'G': int(pontok[i + 1]),
                'B': int(pontok[i + 2]),
            }
            sor.append(pont)
        keppontok.append(sor)
# print(f"{keppontok = }")

# 2. feladat
print("2. feladat")

print("Kérem egy képpont adatait!")
be_sor = int(input("Sor:"))
be_oszlop = int(input("Oszlop:"))
# be_sor = 180
# be_oszlop = 320

pont = keppontok[be_sor - 1][be_oszlop - 1]
print(f"A képpont színe RGB({pont['R']},{pont['G']},{pont['B']})")

# 3. feladat
print("3. feladat")
keppontok_list = [pont for sor in keppontok for pont in sor]  # flatten
vilagos_pontok = [pont for pont in keppontok_list if sum(pont.values()) > 600]
print(f"A világos képpontok száma: {len(vilagos_pontok)}")

# 4. feladat
print("4. feladat")
legsotetebb_pont = min(keppontok_list, key=lambda p: sum(p.values()))
legsotetebb_szin = sum(legsotetebb_pont.values())
print(f"A legsötétebb pont RGB összege: {legsotetebb_szin}")
print("A legsötétebb pixelek színe:")
for pont in keppontok_list:
    if sum(pont.values()) == legsotetebb_szin:
        print(f"RGB({pont['R']},{pont['G']},{pont['B']})")

# 5. feladat


def hatar(
        forraskep: list[list[dict[str, int]]],
        sor_szama: int,
        elteres_merteke: int
        ) -> bool:
    """ A függvény megadja, hogy egy adott sorban van-e olyan hely a képen,
    ahol az egymás melletti képpontok kék színösszetevőinek eltérése
    meghalad egy adott értéket
    """
    kep_sora = forraskep[sor_szama - 1]
    for idx in range(len(kep_sora) - 1):
        kek_elteres = kep_sora[idx]['B'] - kep_sora[idx + 1]['B']
        if abs(kek_elteres) > elteres_merteke:
            return True
    return False


# 6. feladat
print("6. feladat")
felho_sorai = []
for sorszam in range(1, len(keppontok) + 1):
    if hatar(keppontok, sorszam, 10):
        felho_sorai.append(sorszam)
print(f"A felhő legfelső sora: {felho_sorai[0]}")
print(f"A felhő legalsó sora: {felho_sorai[-1]}")
