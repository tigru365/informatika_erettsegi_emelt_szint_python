""" Sudoku (2021.10.26)
"""

from pathlib import Path
from io import StringIO

# 1. feladat
print("1. feladat")

fajlnev = input("Adja meg a bemeneti fájl nevét! ")
sor_szam = int(input("Adja meg egy sor számát! "))
oszlop_szam = int(input("Adja meg egy oszlop számát! "))
# fajlnev = ("konnyu.txt", "kozepes.txt", "nehez.txt")[0]
# sor_szam = 1
# oszlop_szam = 1

# 2. feladat
tablazat: list[list[int]] = []
lepesek: list[list[int]] = []

fajl = Path.cwd() / "forras" / fajlnev
with fajl.open(encoding="ascii") as forrasfajl:
    for _ in range(9):
        sor = forrasfajl.readline().strip().split()
        adatok = list(map(int, sor))
        tablazat.append(adatok)

    for sor in forrasfajl:
        lepes = sor.strip().split()
        lepesek.append(list(map(int, lepes)))
print()

# 3. feladat
print("3. feladat")

szam = tablazat[sor_szam - 1][oszlop_szam - 1]
if szam:
    print(f"Az adott helyen szereplő szám: {szam}")
else:
    print("Az adott helyet még nem töltötték ki.")

resztabla = 1 + ((sor_szam - 1) // 3) * 3 + (oszlop_szam - 1) // 3
print(f"A hely a(z) {resztabla} résztáblázathoz tartozik.\n")

# 4. feladat
print("4. feladat")

szamlalo = 0
for idx_sor in tablazat:
    for szam in idx_sor:
        if not szam:
            szamlalo += 1
print(f"Az üres helyek aránya: {szamlalo / 81:.1%}\n")

# 5. feladat
print("5. feladat")


def resztablaban_van(
        s_tabla: list[list[int]],
        s_szam: int,
        s_sor: int,
        s_oszlop: int,
        ) -> bool:
    """ A függvény megvizsgálja, hogy a sorával és oszlopával
    megadott cellában szereplő szám szerepel-e már
    az adott cellához tartozó résztáblában
    """
    i_min = ((s_sor - 1) // 3) * 3
    i_max = i_min + 3
    j_min = ((s_oszlop - 1) // 3) * 3
    j_max = j_min + 3

    s_resztabla = []
    for i in range(i_min, i_max):
        for j in range(j_min, j_max):
            s_resztabla.append(s_tabla[i][j])
    return s_szam in s_resztabla


for lepes in lepesek:
    print(f"A kiválasztott sor: {lepes[1]}, oszlop: {lepes[2]}, "
          + f"a szám: {lepes[0]}")

    idx_sor = lepes[1] - 1
    idx_oszlop = lepes[2] - 1
    if tablazat[idx_sor][idx_oszlop]:
        print("A helyet már kitöltötték\n")
    elif tablazat[idx_sor].count(lepes[0]):
        print("Az adott sorban már szerepel a szám\n")
    elif [sor[idx_oszlop] for sor in tablazat].count(lepes[0]):
        print("Az adott oszlopban már szerepel a szám\n")
    elif resztablaban_van(tablazat, *lepes):
        print("Az adott résztáblázatban már szerepel a szám\n")
    else:
        print("A lépés megtehető\n")

# Extra
print("6. feladat (szorgalmi)")


def kiir_tablazat() -> None:
    """ A függvény megjeleníti a sudoku táblázatot
    """
    for i, s in enumerate(tablazat):
        if (i % 3) == 0:
            print("*-------*-------*-------*")
        sb = StringIO()
        for j in range(9):
            if (j % 3) == 0:
                sb.write("| ")
            sb.write(f"{s[j] if s[j] else ' '} ")
        sb.write("|")
        print(sb.getvalue())
    print("*-------*-------*-------*")


print("Táblázat:")
kiir_tablazat()
