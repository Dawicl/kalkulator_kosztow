
wybor_zadania = -1

koszty = []
suma = 0

def pokaz_koszty():
    for koszt in koszty:
        print(koszt)

    print("")
    print("Suma kosztów: ", suma, "zł")

def dodaj_koszty():
    global suma
    koszt = input("Podaj koszty, które chcesz dodać: ")
    cena = int(input("Podaj cenę kosztów: "))
    pojedynczy_koszt = [koszt, cena]
    koszty.append(pojedynczy_koszt)
    suma = suma + cena
    plik = open("lista_kosztow.txt", "w")
    for koszt in koszty:
        plik.write(str(koszt[0] + koszt[1] + "\n"))
    plik.write(str("Suma wszystkich kosztów: ", suma, "zł"))
    plik.close

while wybor_zadania != 5:
    
    if wybor_zadania == 1:
        pokaz_koszty()
    
    if wybor_zadania == 2:
        dodaj_koszty()

    print("")
    print("1. Pokaż koszty")
    print("2. Dodaj koszty")
    print("3. Usuń koszty")
    print("4. ")
    print("5. Zakończ")
    print("")
    
    wybor_zadania = int(input("Wybierz operację: "))
    print("")