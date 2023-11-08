""" Társas (2023.10.25)
"""

from pathlib import Path

# 1. feladat

osvenyek: list[str] = []
fajl = Path.cwd() / "forras" / "osvenyek.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        osvenyek.append(sor.strip())
# print(f"{osvenyek = }\n")

dobasok: list[int] = []
fajl = Path.cwd() / "forras" / "dobasok.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        dobasok = list(map(int, sor.strip().split()))
# print(f"{dobasok = }\n")

# 2. feladat
print("2. feladat")

print(f"A dobások száma: {len(dobasok)}")
print(f"Az ösvények száma: {len(osvenyek)}\n")

# 3. feladat
print("3. feladat")

max_osveny = max(osvenyek, key=lambda s: len(s))
print(f"Az egyik leghosszabb a(z) {osvenyek.index(max_osveny) + 1}. ösvény, "
      + f"hossza: {len(max_osveny)}\n")

# 4. feladat
print("4. feladat")

be_osveny_sorszama = int(input("Adja meg egy ösvény sorszámát! "))
be_jatekosok_szama = int(input("Adja meg a játékosok számát! "))
# be_osveny_sorszama = 9
# be_jatekosok_szama = 5
print()

# 5. feladat
print("5. feladat")

kivalasztott_osveny = osvenyek[be_osveny_sorszama - 1]
if darab := kivalasztott_osveny.count('M'):
    print(f"M: {darab} darab")
if darab := kivalasztott_osveny.count('V'):
    print(f"V: {darab} darab")
if darab := kivalasztott_osveny.count('E'):
    print(f"E: {darab} darab")
print()

# 6. feladat
fajl = Path.cwd() / "kulonleges.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for sorszam, mezo in enumerate(kivalasztott_osveny, start=1):
        if mezo != "M":
            celfajl.write(f"{sorszam}\t{mezo}\n")

# 7. feladat
print("7. feladat")

mezok_szama = len(kivalasztott_osveny)
jatekos_mezok = [0 for _ in range(be_jatekosok_szama)]
jatek_kore = 0
nyertesek = []
for i, dobas in enumerate(dobasok):
    jatekos = i % be_jatekosok_szama
    if not jatekos:
        jatek_kore += 1

    jatekos_mezok[jatekos] += dobas

    if jatekos_mezok[jatekos] >= mezok_szama:
        nyertesek.append(jatekos + 1)

    if nyertesek and jatekos + 1 == be_jatekosok_szama:
        break

print(f"A játék a(z) {jatek_kore}. körben fejeződött be. "
      + "A legtávolabb jutó(k) sorszáma:", *nyertesek, end="\n\n")

# 8. feladat
print("8. feladat")

jatekos_mezok = [0 for _ in range(be_jatekosok_szama)]
jatek_kore = 0
nyertesek = []
for i, dobas in enumerate(dobasok):
    jatekos = i % be_jatekosok_szama
    if not jatekos:
        jatek_kore += 1

    jatekos_mezok[jatekos] += dobas
    if jatekos_mezok[jatekos] <= mezok_szama:
        match kivalasztott_osveny[jatekos_mezok[jatekos] - 1]:
            case "E":
                jatekos_mezok[jatekos] += dobas
            case "V":
                jatekos_mezok[jatekos] -= dobas

    if jatekos_mezok[jatekos] >= mezok_szama:
        nyertesek.append(jatekos + 1)

    if nyertesek and jatekos + 1 == be_jatekosok_szama:
        break

print("Nyertes(ek):", *nyertesek)

print("A többiek pozíciója:")
for jatekos, mezo in enumerate(jatekos_mezok, start=1):
    if jatekos in nyertesek:
        continue
    print(f"{jatekos}. játékos, {mezo}. mező")
