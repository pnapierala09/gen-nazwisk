#! python3

""" Generuje listę z wybraną ilością imion z nazwiskami """

import random
import sys
import imie_i_naz

imie_zenskie = imie_i_naz.i_zenske.split()
imie_meskie = imie_i_naz.i_meskie.split()
naz_zenskie = imie_i_naz.n_zenskie.split()
naz_meskie = imie_i_naz.n_meskie.split()

Imie_zenskie = [imie_zenskie[i].capitalize() for i in range(len(imie_zenskie))]  # 100
Imie_meskie = [imie_meskie[i].capitalize() for i in range(len(imie_meskie))]  # 97
Naz_zenskie = [
    naz_zenskie[i].capitalize() for i in range(len(naz_zenskie)) if i % 5 == 0
]  # 99
Naz_meskie = [
    naz_meskie[i].capitalize() for i in range(len(naz_meskie)) if i % 5 == 0
]  # 100


def generator_nazwisk(ilosc):
    """Generuje listę z wybraną ilością imion z nazwiskami"""
    nazwiska = []
    for i in range(ilosc):
        plec = random.randint(0, 1)
        if plec == 0:
            nazwisko = (
                Imie_meskie[random.randint(0, 96)]
                + " "
                + Naz_meskie[random.randint(0, 99)]
            )
            nazwiska.append(nazwisko)
        if plec == 1:
            nazwisko = (
                Imie_zenskie[random.randint(0, 99)]
                + " "
                + Naz_zenskie[random.randint(0, 98)]
            )
            nazwiska.append(nazwisko)
    return nazwiska


if __name__ == "__main__":
    ilosc_nazwisk = 0
    while ilosc_nazwisk != "w":
        ilosc_nazwisk = input("Ile nazwisk wygererować? (wpisz 'w' aby wyjść): ")
        if ilosc_nazwisk.isnumeric():
            nazwiska = generator_nazwisk(int(ilosc_nazwisk))
            for n in nazwiska:
                print(n)
        elif ilosc_nazwisk == "w":
            sys.exit()
        else:
            print("Podaj liczbę")
