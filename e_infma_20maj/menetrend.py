""" Menetrend (2020.05.18-id.ny.)
"""

from pathlib import Path

# 1. feladat

# Adatstruktúra:
# {
#     1: {
#         0: {
#             "erkezes": 0,
#             "indulas": 345
#         },
#         1: {
#             "erkezes": 360,
#             "indulas": 362
#         },
#         ...
#     },
#     2: {
#         0: {
#             "erkezes": 0,
#             "indulas": 405
#         },
#         ...
#     },
#     ...
# }
menetrend: dict[int, dict[int, dict[str, int]]] = {}

fajl = Path.cwd() / "forras" / "vonat.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split("\t")

        v = int(adatok[0])
        a = int(adatok[1])

        if v in menetrend:
            vonat = menetrend[v]
        else:
            vonat: dict[int, dict[str, int]] = {}
            menetrend[v] = vonat

        if a in vonat:
            allomas = vonat[a]
        else:
            allomas = {
                'erkezes': 0,
                'indulas': 0,
            }
            vonat[a] = allomas

        if adatok[4] == 'E':
            irany = 'erkezes'
        else:
            irany = 'indulas'
        allomas[irany] = int(adatok[2]) * 60 + int(adatok[3])
# print(f"{menetrend = }")

# 2. feladat
print("2. feladat")

print(f"Az állomások száma: {len(menetrend[1])}")
print(f"A vonatok száma: {len(menetrend)}\n")

# 3. feladat
print("3. feladat")

max_allas = 0
max_vonat = (-1, -1)
for vonat, allomasok in menetrend.items():
    for allomas, idok in allomasok.items():
        if idok['indulas'] and idok['erkezes']:
            allas = idok['indulas'] - idok['erkezes']
            if allas > max_allas:
                max_allas = allas
                max_vonat = (vonat, allomas)

print(f"A(z) {max_vonat[0]}. vonat a(z) {max_vonat[1]}. állomáson {max_allas} "
      + "percet állt.\n")

# 4. feladat
be_vonat_azon = int(input("Adja meg egy vonat azonosítóját! "))
be_ora, be_perc = list(map(
    int,
    input("Adjon meg egy időpontot (óra perc)! ").split()))
# be_vonat_azon = 2
# be_ora = 7
# be_perc = 16
print()

# 5. feladat
print("5. feladat")

eloirt_menetido = 2 * 60 + 22
indulas = menetrend[be_vonat_azon][0]['indulas']
erkezes = menetrend[be_vonat_azon][10]['erkezes']
elteres = (erkezes - indulas) - eloirt_menetido

if elteres < 0:
    print(f"A(z) {be_vonat_azon}. vonat útja {elteres} "
          + "perccel rövidebb volt az előírtnál.")
elif elteres > 0:
    print(f"A(z) {be_vonat_azon}. vonat útja {elteres} "
          + "perccel hosszabb volt az előírtnál.")
else:
    print(
        f"A(z) {be_vonat_azon}. vonat útja pontosan az előírt ideig tartott.")
print()

# 6. feladat
fajl = Path.cwd() / f"halad{be_vonat_azon}.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for allomas, idok in menetrend[be_vonat_azon].items():
        if idok['erkezes']:
            ora, perc = divmod(idok['erkezes'], 60)
            celfajl.write(f"{allomas}. állomás: {ora}:{perc}\n")

# 7. feladat
print("7. feladat")

idopont = be_ora * 60 + be_perc

for vonat, allomasok in menetrend.items():
    if allomasok[0]['indulas'] < idopont < allomasok[10]['erkezes']:
        for a_azon in range(1, 10):
            if allomasok[a_azon]['erkezes'] <= idopont \
                    < allomasok[a_azon]['indulas']:
                print(f"A(z) {vonat}. vonat a {a_azon}. állomáson állt.")
            if allomasok[a_azon]['indulas'] <= idopont \
                    < allomasok[a_azon + 1]['erkezes']:
                print(f"A(z) {vonat}. vonat a {a_azon}. és a {a_azon + 1}. "
                      + "állomás között járt.")
