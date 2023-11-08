""" Céges autók (2019.05.13)
"""

from pathlib import Path

# 1. feladat
autok: list[dict[str, int | str | bool]] = []

fajl = Path.cwd() / "forras" / "autok.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()

        auto: dict[str, int | str | bool] = {
            'nap': int(adatok[0]),
            'ido': adatok[1],
            'rendszam': adatok[2],
            'szemely': int(adatok[3]),
            'km': int(adatok[4]),
            'ki': not bool(int(adatok[5])),
        }
        autok.append(auto)
# print(f"{autok = }")

# 2. feladat
print("2. feladat")

utolso_ki = [a for a in autok if a['ki']][-1]

print(f"{utolso_ki['nap']}. nap rendszám: {utolso_ki['rendszam']}")

# 3. feladat
print("3. feladat")

nap = int(input("Nap: "))
# nap = 4
print(f"Forgalom a(z) {nap}. napon:")

for auto in [a for a in autok if a['nap'] == nap]:
    print(f"{auto['ido']} {auto['rendszam']} {auto['szemely']} "
          + f"{'ki' if auto['ki'] else 'be'}")

# 4. feladat
print("4. feladat")

utak = {"CEG30" + str(i): 0 for i in range(10)}
for auto in autok:
    utak[auto['rendszam']] += 1

darab_kint = sum(v % 2 for v in utak.values())
print(f"A hónap végén {darab_kint} autót nem hoztak vissza.")

# 5. feladat
print("5. feladat")

statisztika = {"CEG30" + str(i): 0 for i in range(10)}

for rendszam in statisztika:
    mozgasok = [a for a in autok if a['rendszam'] == rendszam]
    for i in range(len(mozgasok) - 1):
        statisztika[rendszam] += mozgasok[i + 1]['km'] - mozgasok[i]['km']

for k, v in statisztika.items():
    print(f"{k} {v} km")

# 6. feladat
print("6. feladat")

tavok = [[sz, 0] for sz in range(500, 601)]
for tav in tavok:
    utak = [a for a in autok if a['szemely'] == tav[0]]
    for j in range(0, len(utak) - 1, 2):
        if utak[j]['ki'] and not utak[j + 1]['ki']:
            km = utak[j + 1]['km'] - utak[j]['km']
            if km > tav[1]:
                tav[1] = km

max_tav = max(tavok, key=lambda t: t[1])
print(f"Leghosszabb út: {max_tav[1]} km, személy: {max_tav[0]}")

# 7. feladat
print("7. feladat")

rendszam = input("Rendszám: ")
# rendszam = "CEG304"

mozgasok = [a for a in autok if a['rendszam'] == rendszam]

fajl = Path.cwd() / f"{rendszam}_menetlevel.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for m in mozgasok:
        if m['ki']:
            celfajl.write(f"{m['szemely']}\t{m['nap']}. "
                          + f"{m['ido']}\t{m['km']} km")
        else:
            celfajl.write(f"\t{m['nap']}. {m['ido']}\t{m['km']} km\n")

print("Menetlevél kész.")
