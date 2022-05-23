class Pracownik: 
    def __init__(self, imie, brutto):
        self.imie = imie
        self.wyn_brutto = brutto

    def __repr__(self):
        return f"{self.imie} {self.wyn_brutto}"

    def wynagrodzenie_netto(self):
        skladki_na_ubez_finansowane_przez_pracownika = self.wyn_brutto*0.0976 + self.wyn_brutto*0.015 + self.wyn_brutto*0.0245
        podstawa_wymiaru_skladek_na_ubez = self.wyn_brutto - round(skladki_na_ubez_finansowane_przez_pracownika, 2)
        skladki_na_ubez_zdrowotne_do_pobrania = round(podstawa_wymiaru_skladek_na_ubez, 2) * 0.09
        koszt_uzyskania_przychodu = 111.25
        skladki_na_ubez_zdrowotne_do_odliczenia = round(podstawa_wymiaru_skladek_na_ubez) * 0.0775
        podstawa_oblczenia_zaliczki_na_pod_doch = int(self.wyn_brutto) - int(koszt_uzyskania_przychodu) - int(skladki_na_ubez_finansowane_przez_pracownika)
        zaliczka_podatek_doch_przed_odliczeniem = (round(podstawa_oblczenia_zaliczki_na_pod_doch, 2) * 0.18) - 46.33
        zaliczka_na_pod_doch_do_pobrania = int(zaliczka_podatek_doch_przed_odliczeniem) - int(skladki_na_ubez_zdrowotne_do_odliczenia)
        self.netto = self.wyn_brutto - round(skladki_na_ubez_finansowane_przez_pracownika, 2) - round(skladki_na_ubez_zdrowotne_do_pobrania, 2) - round(zaliczka_na_pod_doch_do_pobrania, 2)
        return round(self.netto, 2)

    def skladki_pracodawcy(self):
        skladki = self.wyn_brutto*0.0976 + self.wyn_brutto*0.065
        skladka_wypadkowa = self.wyn_brutto*0.0193 + self.wyn_brutto*0.0245
        skladka_na_fgsp = self.wyn_brutto*0.001
        self.skladka_pracodawcy = round(skladki, 2) + round(skladka_wypadkowa,2) + round(skladka_na_fgsp, 2)
        return round(self.skladka_pracodawcy, 2)

    def laczny_koszt_pracodaw(self):
        return round((self.wyn_brutto + self.skladki_pracodawcy()), 2)


liczba_pracownikow = int(input())
pracownicy = []
for i in range (0, liczba_pracownikow):
    temp = input()
    temp = temp.split()
    imie = temp[0]
    brutto = int(temp[1])
    pracownik = Pracownik(imie, brutto)
    pracownicy.append(pracownik)

laczny_koszt_pracodawcy = 0
for i in range(0, liczba_pracownikow):
    imie = pracownicy[i].imie
    brutto = pracownicy[i].wyn_brutto
    laczny_koszt_pracodawcy += pracownicy[i].laczny_koszt_pracodaw()
    print(imie, f"{pracownicy[i].wynagrodzenie_netto():.2f}",
    f"{pracownicy[i].skladki_pracodawcy():.2f}", 
        f"{pracownicy[i].laczny_koszt_pracodaw():.2f}")
print(laczny_koszt_pracodawcy)
