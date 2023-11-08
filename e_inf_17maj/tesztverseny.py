""" Tesztverseny (2017.05.15)
"""

from pathlib import Path

# 1. feladat
print("1. feladat: Az adatok beolvasása\n")

valaszok: list[list[str]] = []

fajl = Path.cwd() / "forras" / "valaszok.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    helyes_valaszok = forrasfajl.readline().strip()

    for sor in forrasfajl:
        valaszok.append(sor.strip().split())
# print(f"{valaszok = }")

# 2. feladat
print(f"2. feladat: A vetélkedőn {len(valaszok)} versenyző indult.\n")

# 3. feladat
azonosito = input("3. feladat: A versenyző azonosítója = ")
# azonosito = "AB123"

valasz = [v[1] for v in valaszok if v[0] == azonosito][0]
print(f"{valasz}\t(a versenyző válasza)\n")

# 4. feladat
print("4. feladat:")

print(f"{helyes_valaszok}\t(a helyes megoldás)")

for i, v in enumerate(valasz):
    print("+" if v == helyes_valaszok[i] else " ", end="")
print("\t(a versenyző helyes válaszai)\n")

# 5. feladat
sorszam = int(input("5. feladat: A feladat sorszáma = "))
# sorszam = 10

jol_valaszolt = [v[0] for v in valaszok
                 if v[1][sorszam - 1] == helyes_valaszok[sorszam - 1]]
jo_valasz = len(jol_valaszolt)
arany = jo_valasz / len(valaszok)

print(f"A feladatra {jo_valasz} fő, "
      + f"a versenyzők {arany:.2%}-a adott helyes választ.\n")

# 6. feladat
print("6. feladat: A versenyzők pontszámának meghatározása\n")

pontok = (3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6)
pontszamok = []

fajl = Path.cwd() / "pontok.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for azon, valasz in valaszok:
        pont = 0
        for i, v in enumerate(valasz):
            if v == helyes_valaszok[i]:
                pont += pontok[i]
        pontszamok.append((azon, pont))
        celfajl.write(f"{azon} {pont}\n")

# 7. feladat
print("7. feladat: A verseny legjobbjai:")

pont_sorrend = {x[1] for x in pontszamok}
pont_sorrend = sorted(pont_sorrend, reverse=True)

for hely in range(3):
    helyezett = [p for p in pontszamok if p[1] == pont_sorrend[hely]]
    for azon, pont in helyezett:
        print(f"{hely + 1}. díj ({pont} pont): {azon}")
