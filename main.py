
wybor_zadania = -1

koszty = []

def pokaz_koszty():
    numer_indexu = 0
    for koszt in koszty:
        print(koszt[0] + " - " + str(koszt[1]) + " " + "[" + str(numer_indexu) + "]")
        numer_indexu += 1
    print("")
    print("Suma kosztów: ", suma, "zł")

def dodaj_koszty():
    global suma
    koszt = input("Podaj koszty, które chcesz dodać: ")
    cena = int(input("Podaj cenę kosztów: "))
    pojedynczy_koszt = [koszt, cena]
    koszty.append(pojedynczy_koszt)
    suma = suma + cena

def zapisz_do_pliku():
    plik = open("lista_kosztow.txt", "w", encoding="utf-8")
    for koszt in koszty:
        plik.write(koszt[0]+ " " + str(koszt[1]) + " zł" + "\n")
    plik.write("Suma wszystkich kosztów: " + str(suma) + " zł")
    plik.close

def usun_pozycje():
    global suma
    try:
        pokaz_koszty()
        print("")
        numer_pozycji = int(input("Podaj numer pozycji do usunięcia: "))
        if numer_pozycji < 0 or numer_pozycji > len(koszty) -1:
            print("Brak indexu o danym numerze.")
            return
        koszt_temp = koszty.pop(numer_pozycji)
        suma -= int(koszt_temp[1])
        print("Wybrana pozycja została usunięta.")

    except:
        print("Podawaj tylko numery indeksów!")
        usun_pozycje()

def zaladuj_plik():
    suma = 0
    plik = open("lista_kosztow.txt", "r", encoding="utf-8")
    for koszt in plik.readlines():
        temp_lista = koszt.split()
        koszty.append(temp_lista)
    koszty.remove(koszty[-1])
    for koszt in koszty:
        suma += int(koszt[1])
    plik.close
    return suma

suma = zaladuj_plik()

while wybor_zadania != 5:
    
    if wybor_zadania == 1:
        pokaz_koszty()
    
    if wybor_zadania == 2:
        dodaj_koszty()

    if wybor_zadania == 3:
        usun_pozycje()

    if wybor_zadania == 4:
        zapisz_do_pliku()

    print("")
    print("1. Pokaż koszty")
    print("2. Dodaj koszty")
    print("3. Usuń wybrany koszt")
    print("4. Zapisz do pliku")
    print("5. Zakończ")
    print("")
    
    wybor_zadania = int(input("Wybierz operację: "))
    print("")