""" Bányató (2021-05-17-id.ny.)
"""

from pathlib import Path

# 1. feladat
melysegek: list[list[int]] = []

fajl = Path.cwd() / "forras" / "melyseg.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    sorok_szama = int(forrasfajl.readline().strip())
    oszlopok_szama = int(forrasfajl.readline().strip())

    for sor in forrasfajl:
        melysegek.append(list(map(int, sor.strip().split())))
# print(f"{melysegek = }")

# 2. feladat
print("2. feladat")

sor_azon = int(input("A mérés sorának azonosítója="))
oszl_azon = int(input("A mérés oszlopának azonosítója="))
# sor_azon = 12
# oszl_azon = 6

print("A mért mélység az adott helyen "
      + f"{melysegek[sor_azon - 1][oszl_azon - 1]} dm")

# 3. feladat
print("3. feladat")

# flatten, filter
to_melysegei = [melyseg for sor in melysegek for melyseg in sor if melyseg]
cellak_szama = len(to_melysegei)
osszesen = sum(to_melysegei) / 10  # méterben

print(f"A tó felszíne: {cellak_szama} m2, "
      + f"átlagos mélysége: {osszesen / cellak_szama:.2f} m")

# 4. feladat
print("4. feladat")

max_melyseg = max(to_melysegei)
print(f"A tó legnagyobb mélysége: {max_melyseg} dm")

koordinatak = []
for i in range(sorok_szama):
    for j in range(oszlopok_szama):
        if melysegek[i][j] == max_melyseg:
            koordinatak.append(f"({i + 1}; {j + 1})")

print("A legmélyebb helyek sor-oszlop koordinátái:")
print("\t".join(koordinatak))

# 5. feladat
print("5. feladat")

hossz = 0
for i in range(1, sorok_szama - 1):
    for j in range(1, oszlopok_szama - 1):
        if melysegek[i][j]:
            if not melysegek[i][j - 1]:  # balra lévő érték
                hossz += 1
            if not melysegek[i][j + 1]:  # jobbra lévő érték
                hossz += 1
            if not melysegek[i - 1][j]:  # felette lévő érték
                hossz += 1
            if not melysegek[i + 1][j]:  # alatta lévő érték
                hossz += 1

print(f"A tó partvonala {hossz} m hosszú")

# 6. feladat
print("6. feladat")

oszlop = int(input("A vizsgált szelvény oszlopának azonosítója=")) - 1
# oszlop = 5

fajl = Path.cwd() / "diagram.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for azon, sor in enumerate(melysegek, start=1):
        celfajl.write(f"{azon:02d}{'*' * round(sor[oszlop] / 10)}\n")
