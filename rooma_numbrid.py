'''
Programmi üldine loogika.

while True tsükkel juhib kasutaja sisendi küsimist kuni kasutaja sisestab mingil kujul q tähe.
try / except plokk püüab mittearvulised sisendid, väljastab vajadusel veateate ning jätkab tööd.
try plokk sees kontrollime sisestatud arvu suurust ja muudame suurusjärkudeks- tuhandelised, sajalised, kümnelised, ühelised, muudame
need täisarvudeks ja lisame listi [kohad]
Edasi kontrollime listi [kohad] pikkust if tingimusega, millest saame teada sisestatud arvu suurusjärkude arvu.
Seejärel seame suurusjärgu indeksi vastavusse numbriga, mis sel kohal asub- st kolmekohalise numbri [0] koha globaalse muutuja saj indeksiga [0],
kümneliste indeksiga [1] jne. Vastavusse seatud tähekombinatsiooni lisame append funktsiooni abil listi [rooma_numbrid]
'''

tuh = ["", "M"]  # järgnevas blokis defineerime suurusjärkude kombinatsioonid, 0 või 1000
saj = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # sajalised tühi ja 100-900
kym = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # kümnelised tühi ja 10-90
yhe = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # üheliste kombinatsioonid tühi ja 1-9

while True:

    kasutaja_sisend = input("Sisesta araabia number 1-1000 või lõpetamiseks 'q': ")
    if kasutaja_sisend.lower().strip() == 'q':
        print("Programmi lõpp")
        break  # kui kasutaja trükib q , siis lõpetab programmi töö koos vastava teatega

    try:

        if 0 < int(
                kasutaja_sisend) < 1001:  # proovime muuta kasutaja sisendi täisarvuks ja kontrollime, kas on 0 ja 1000 vahel

            kohad = [int(i) for i in
                     str(kasutaja_sisend)]  # itereerime kasutaja sisendi ja teeme iga suurusjärgu täisarvuks ning lisame listi [kohad]
            rooma_number = []  # see on tühi list, millele hakkame rooma numbreid lisama

            if len(kohad) == 4:  # kui sisestatud täisarvu pikkus on 4, siis tuhandeliste koht indeks on [0], sajalistel [1] jne
                rooma_number.append(tuh[kohad[0]] + saj[kohad[1]] + kym[kohad[2]] + yhe[kohad[3]])  # lisame listi rooma_number kombinatsioonid vastavalt iga koha indeksile
            elif len(kohad) == 3:
                rooma_number.append(saj[kohad[0]] + kym[kohad[1]] + yhe[kohad[2]])
            elif len(kohad) == 2:
                rooma_number.append(kym[kohad[0]] + yhe[kohad[1]])
            else:
                rooma_number.append(yhe[kohad[0]])

            print(*rooma_number)  # prindime tulemuse, * operaator eemaldab jutumärgid ja kandilised sulud


        else:
            print("Sisesta sobiv number vahemikus 1-1000")  # kui kasutaja sisestab täisarvu, mis pole 0 ja 1000 vahel

    except ValueError:  # kui kasutaja sisestab midagi, mis pole (täielikult) ainult arv, anname veateate ja küsime uuesti
        print("Ebasobiv sisestus.")
        continue
