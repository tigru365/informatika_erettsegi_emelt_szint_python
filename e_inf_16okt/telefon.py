""" Telefonos ügyfélszolgálat (2016.10.21)
"""

from pathlib import Path

# 1. feladat


def mpbe(ora: int, perc: int, mperc: int) -> int:
    """ A függvény az óra, perc, másodperc alakban megadott időpont
    másodpercben kifejezett értékét adja vissza
    """
    return ora * 3600 + perc * 60 + mperc


# 2. feladat
hivasok: list[dict[str, int]] = []

fajl = Path.cwd() / "forras" / "hivas.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = list(map(int, sor.strip().split()))

        k = mpbe(adatok[0], adatok[1], adatok[2])
        v = mpbe(adatok[3], adatok[4], adatok[5])
        hivas = {
            'kezd': k,
            'vege': v,
            'hossz': v - k,
        }
        hivasok.append(hivas)
# print(f"{hivasok = }")

# 3. feladat
print("3. feladat")

elso_ora = hivasok[0]['kezd'] // 3600
utolso_ora = hivasok[-1]['vege'] // 3600

for oraban in range(elso_ora, utolso_ora + 1):
    hivasok_orankent = len(
        [h for h in hivasok
         if mpbe(oraban, 0, 0) <= h['kezd'] < mpbe(oraban + 1, 0, 0)])
    if hivasok_orankent:
        print(f"{oraban} óra: {hivasok_orankent} hívás")
print()

# 4. feladat
print("4. feladat")

max_hivas = max(hivasok, key=lambda h: h['hossz'])
print("A leghosszabb ideig vonalban lévő hívó a(z) "
      + f"{hivasok.index(max_hivas) + 1}. sorban szerepel, "
      + f"a hivás hossza: {max_hivas['hossz']} másodperc.\n")

# 5. feladat
print("5. feladat")

be_ora, be_perc, be_mperc = input(
    "Adjon meg egy időpontot! (óra perc másodperc) ").split()
# be_ora = 10
# be_perc = 11
# be_mperc = 12
idopont = mpbe(int(be_ora), int(be_perc), int(be_mperc))

hivok = [h for h in hivasok if h['kezd'] <= idopont < h['vege']]
if hivok:
    print(f"A várakozók száma: {len(hivok) - 1}, "
          + f"a beszélő a(z) {hivasok.index(hivok[0]) + 1}. hívó.\n")
else:
    print("Nem volt beszélő.\n")


# 6. feladat
print("6. feladat")

beszelok = [h for h in hivasok if h['kezd'] < mpbe(12, 0, 0) < h['vege']]
utolso_beszelo = max(beszelok, key=lambda b: b['vege'])

elotte_hivok = beszelok[:beszelok.index(utolso_beszelo)]
elotte_hivo = max(elotte_hivok, key=lambda eh: eh['vege'])

varakozas = elotte_hivo['vege'] - utolso_beszelo['kezd']
print("Az utolsó telefonáló adatai a(z) "
      + f"{hivasok.index(utolso_beszelo) + 1}. sorban vannak, "
      + f"{varakozas} másodpercig várt.")

# 7. feladat


def opmbe(ido_mp: int) -> str:
    """ A függvény a másodpercben kifejezett értékével megadott időpontot
    adja vissza 'óra perc mperc' alakban
    """
    ora, mperc = divmod(ido_mp, 3600)
    perc, mperc = divmod(mperc, 60)
    return f"{ora} {perc} {mperc}"


fogadhato_hivasok = [h for h in hivasok
                     if h['vege'] > mpbe(8, 0, 0)
                     and h['kezd'] < mpbe(12, 0, 0)]

fajl = Path.cwd() / "sikeres.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    hivas_kezdete = hivasok[0]['kezd']
    hivas_vege = mpbe(8, 0, 0)

    for hivas in fogadhato_hivasok:
        if hivas['kezd'] >= hivas_kezdete and hivas_vege < hivas['vege']:
            sorszam = hivasok.index(hivas) + 1
            celfajl.write(
                f"{sorszam} {opmbe(hivas_vege)} {opmbe(hivas['vege'])}\n")
            hivas_vege = hivas['vege']
            hivas_kezdete = hivas['kezd']
