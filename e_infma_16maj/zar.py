""" Zár (2016.05.10-id.ny.)
"""

from pathlib import Path
import random

# 1. feladat
kodok: list[str] = []

fajl = Path.cwd() / "forras" / "ajto.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        kodok.append(sor.strip())
# print(f"{kodok = }")

# 2. feladat
print("2. feladat")

be_kodszam = input("Adja meg, mi nyitja a zárat! ")
# be_kodszam = "239451"

# 3. feladat
print("3. feladat")

sorok = [sor for sor, kod in enumerate(kodok, start=1) if kod == be_kodszam]
print("A nyitó kódszámok sorai:", *sorok, end="...\n")

# 4. feladat
print("4. feladat")

for sor, kod in enumerate(kodok, start=1):
    if len(kod) > len(set(kod)):
        print(f"Az első ismétlődést tartalmazó próbálkozás sorszáma: {sor}")
        break
else:
    print("Nem volt ismétlődő számjegy")

# 5. feladat
print("5. feladat")

random.seed()

random_kod = "".join(random.sample(
    [str(x) for x in range(10)],
    k=len(be_kodszam)))
print(f"Egy {len(random_kod)} hosszú kódszám: {random_kod}")

# 6. feladat

# Függvény nyit(jo, proba:karaktersorozat): logikai érték
#     egyezik:=(hossz(jo)=hossz(proba))
#     Ha egyezik akkor
#         elteres=ascii(jo[1])-ascii(proba[1])
#         Ciklus i:=2-től hossz(jo)
#             Ha ( elteres - (ascii(jo[i])-ascii(proba[i])) ) mod 10 <> 0
#             akkor egyezik:=hamis
#         Ciklus vége
#     Elágazás vége
#     nyit:=egyezik
# Függvény vége


def nyit(jo: str, proba: str) -> bool:
    """ A függvény a neki átadott két kódszámról megállapítja,
    hogy ugyanazt a zárat nyitják-e.
    """
    egyezik = len(jo) == len(proba)
    if egyezik:
        elteres = ord(jo[0]) - ord(proba[0])
        for i in range(1, len(jo)):
            if (elteres - (ord(jo[i]) - ord(proba[i]))) % 10 != 0:
                egyezik = False
    return egyezik


# 7. feladat
fajl = Path.cwd() / "siker.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    for kod in kodok:
        if len(kod) != len(be_kodszam):
            celfajl.write(f"{kod} hibás hossz\n")
        else:
            if nyit(kod, be_kodszam):
                celfajl.write(f"{kod} sikeres\n")
            else:
                celfajl.write(f"{kod} hibás kódszám\n")
