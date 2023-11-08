""" Gödrök (2021.05.17)
"""

from pathlib import Path

# 1. feladat
print("1. feladat")

melysegek: list[int] = []

fajl = Path.cwd() / "forras" / "melyseg.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        melysegek.append(int(sor.strip()))
# print(f"{melysegek = }")

print(f"A fájl adatainak száma: {len(melysegek)}\n")

# 2. feladat
print("2. feladat")

tavolsag = int(input("Adjon meg egy távolságértéket! "))
# tavolsag = 9

print(f"Ezen a helyen a felszín {melysegek[tavolsag - 1]} méter mélyen van.\n")

# 3. feladat
print("3. feladat")

print("Az érintetlen terület aránya "
      + f"{melysegek.count(0) / len(melysegek):.2%}.\n")

# 4. feladat
godrok = []

fajl = Path.cwd() / "godrok.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    godor_e = False
    godor = []
    for melyseg in melysegek:
        if melyseg:
            if not godor_e:
                godor_e = True
            godor.append(str(melyseg))
        else:
            if godor_e:
                godor_e = False
                godrok.append(godor)
                celfajl.write(" ".join(godor) + "\n")
                godor = []

# 5. feladat
print("5. feladat")

print(f"A gödrök száma: {len(godrok)}\n")

# 6. feladat
print("6. feladat")

if not melysegek[tavolsag - 1]:
    print("Az adott helyen nincs gödör.")
else:
    # 6.a) feladat
    print("a)")

    i = 0
    idx_kezdete = tavolsag - 1
    for i, melyseg in reversed(list(enumerate(melysegek[:tavolsag]))):
        if not melyseg:
            break
    idx_kezdete = i + 1

    idx_vege = tavolsag - 1
    for i, melyseg in enumerate(melysegek[tavolsag - 1:]):
        if not melyseg:
            break
    idx_vege += i - 1

    print(f"A gödör kezdete: {idx_kezdete + 1} méter, "
          + f"a gödör vége: {idx_vege + 1} méter.")

    # 6.b) feladat
    print("b)")

    godor = melysegek[idx_kezdete:idx_vege + 1]
    idx_max, legmelyebb = max(enumerate(godor), key=lambda x: x[1])

    konvex = True
    for i in range(len(godor) - 1):
        if i < idx_max:
            if godor[i] > godor[i + 1]:
                konvex = False
                break
        elif i >= idx_max:
            if godor[i] < godor[i + 1]:
                konvex = False
                break

    if konvex:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")

    # 6.c) feladat
    print("c)")
    print(f"A legnagyobb mélysége {legmelyebb} méter.")

    # 6.d) feladat
    print("d)")

    terfogat = sum(godor) * 10
    print(f"A térfogata {terfogat} m^3.")

    # 6.e) feladat
    print("e)")

    vizmennyiseg = (sum(godor) - len(godor)) * 10
    print(f"A vízmennyiség {vizmennyiseg} m^3.")
