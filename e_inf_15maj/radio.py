""" Expedíció (2015.05.12)
"""

from pathlib import Path

# 1. feladat

# Adatstruktúra:
# [
#     {
#         "nap": 1,
#         "azon": 13,
#         "uzenet": "#abor# #e#tun###agy#szel#2# #o##h#d#g ##rkasn#o#oka# ..."
#     },
#     ...
#     {
#         "nap": 4,
#         "azon": 18,
#         "uzenet": "hovi##r##i### ##m vo#t#meg##gy#les rend##r#ktuk#a fe#..."
#     }
# ]
vetel: list[dict[str, int | str]] = []

fajl = Path.cwd() / "forras" / "veetel.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    # for k, sor in enumerate(forrasfajl):
    #     if k % 2 == 0:
    #         adatok = sor.strip().split()
    #         adas = {
    #             'nap': int(adatok[0]),
    #             'radios': int(adatok[1]),
    #         }
    #     else:
    #         adas['uzenet'] = sor.strip()
    #         vetel.append(adas)
    adatok: list[str] = []
    for sor in forrasfajl:
        adatok.append(sor.strip())
        if len(adatok) == 2:
            n, r = adatok[0].split()
            adas: dict[str, int | str] = {
                'nap': int(n),
                'radios': int(r),
                'uzenet': adatok[1],
            }
            vetel.append(adas)
            adatok = []
# print(f"{vetel = }")

# 2. feladat
print("2. feladat")

print(f"Az első üzenet rögzítője: {vetel[0]['radios']}")
print(f"Az utolsó üzenet rögzítője: {vetel[-1]['radios']}\n")

# 3. feladat
print("3. feladat")

farkasok = [adas for adas in vetel if "farkas" in adas['uzenet']]
for adas in farkasok:
    print(f"{adas['nap']}. nap {adas['radios']}. rádióamatőr")
print()

# 4. feladat
print("4. feladat")

statisztika = {nap: set() for nap in range(1, 12)}
for adas in vetel:
    statisztika[adas['nap']].add(adas['radios'])

for nap, radiosok in statisztika.items():
    print(f"{nap}. nap: {len(radiosok)} rádióamatőr")
print()

# 5. feladat
fajl = Path.cwd() / "adaas.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for nap in range(1, 12):
        aznapi_adasok = [adas['uzenet'] for adas in vetel
                         if adas['nap'] == nap]
        if aznapi_adasok:
            for k in range(90):
                betu = aznapi_adasok[0][k]
                if betu == "#":
                    for aznapi in aznapi_adasok[1:]:
                        if aznapi[k] != "#":
                            betu = aznapi[k]
                            break
                celfajl.write(betu)
            celfajl.write("\n")
        else:
            celfajl.write("#\n")

# 6. feladat

# Függvény szame(szo:karaktersorozat): logikai
#     valasz:=igaz
#     Ciklus i:=1-től hossz(szo)-ig
#         ha szo[i]<'0' vagy szo[i]>'9' akkor valasz:=hamis
#     Ciklus vége
#     szame:=valasz
# Függvény vége


def szame(szo: str) -> bool:
    """ A függvény egy karaktersorozatról eldönti, hogy szám-e (pozitív egész)
    """
    valasz = True
    for i in range(len(szo)):
        if szo[i] < "0" or szo[i] > "9":
            valasz = False
    return valasz


# 7. feladat
print("7. feladat")

be_nap = int(input("Adja meg a nap sorszámát! "))
be_radios = int(input("Adja meg a rádióamatőr sorszámát! "))
# be_nap = 2
# be_radios = 15

uzenet = ""
for adas in vetel:
    if adas['nap'] == be_nap and adas['radios'] == be_radios:
        uzenet = adas['uzenet']

if uzenet:
    van_info = False
    kifejlett_egyed = 0
    kolyok_egyed = 0

    reszek1 = uzenet.split("/")
    if szame(reszek1[0]):
        kifejlett_egyed = int(reszek1[0])
        if len(reszek1) > 1:
            van_info = True

    if van_info:
        reszek2 = reszek1[1].split(" ")
        if len(reszek2) > 1 and szame(reszek2[0]):
            kolyok_egyed = int(reszek2[0])
        else:
            van_info = False

    if van_info:
        print(f"A megfigyelt egyedek száma: {kifejlett_egyed + kolyok_egyed}")
    else:
        print("Nincs információ")
else:
    print("Nincs ilyen feljegyzés")
