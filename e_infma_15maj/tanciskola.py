""" Latin táncok (2015.05.12-id.ny.)
"""

from pathlib import Path

# 1. feladat
tancrend: list[dict[str, str]] = []

fajl = Path.cwd() / "forras" / "tancrend.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    adatok: list[str] = []
    for sor in forrasfajl:
        adatok.append(sor.strip())
        if len(adatok) == 3:
            par = {
                'tanc': adatok[0],
                'lany': adatok[1],
                'fiu': adatok[2],
            }
            tancrend.append(par)
            adatok = []
# print(f"{tancrend = }")

# 2. feladat
print("2. feladat")

print(f"Elsőként bemutatott tánc neve: {tancrend[0]['tanc']}")
print(f"Utolsóként bemutatott tánc neve: {tancrend[-1]['tanc']}\n")

# 3. feladat
print("3. feladat")

osszes_samba = sum(1 for par in tancrend if par['tanc'] == "samba")
print(f"{osszes_samba} pár mutatta be a samba-t.\n")

# 4. feladat
print("4. feladat")

print("Vilma az alábbi táncokban szerepelt:")

vilma_tancai = [par['tanc'] for par in tancrend if par['lany'] == "Vilma"]
print(*vilma_tancai, sep="\n", end="\n\n")

# 5. feladat
print("5. feladat")

be_tanc = input("Adja meg egy tánc nevét! ")
# be_tanc = "samba"

if be_tanc in vilma_tancai:
    vilma_parja = [par['fiu'] for par in tancrend
                   if par['tanc'] == be_tanc and par['lany'] == "Vilma"][0]
    print(f"A {be_tanc} bemutatóján Vilma párja {vilma_parja} volt.\n")
else:
    print(f"Vilma nem táncolt {be_tanc}-t.\n")

# 6. feladat
lanyok: set[str] = {par['lany'] for par in tancrend}
fiuk: set[str] = {par['fiu'] for par in tancrend}

fajl = Path.cwd() / "szereplok.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    celfajl.write(f"Lányok: {', '.join(sorted(lanyok))}\n")
    celfajl.write(f"Fiúk: {', '.join(sorted(fiuk))}\n")

# 7. feladat
print("7. feladat")

tancosok_szereplesei = {
    tancos: sum(1 for par in tancrend if par['fiu'] == tancos)
    for tancos in fiuk}
max_szereples = max(tancosok_szereplesei.values())

max_fiuk = [tancos for tancos, darab in tancosok_szereplesei.items()
            if darab == max_szereples]
print(f"A legtöbbször szerepelt fiú(k): {', '.join(sorted(max_fiuk))}")

tancosok_szereplesei = {
    tancos: sum(1 for par in tancrend if par['lany'] == tancos)
    for tancos in lanyok}
max_szereples = max(tancosok_szereplesei.values())

max_lanyok = [tancos for tancos, darab in tancosok_szereplesei.items()
              if darab == max_szereples]
print(f"A legtöbbször szerepelt lány(ok): {', '.join(sorted(max_lanyok))}")
