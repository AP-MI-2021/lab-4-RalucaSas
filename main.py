def print_meniu():
    print("1.Citire lista: ")
    print("2.Afișarea tuturor numerelor negative nenule din listă ")
    print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură. ")
    print("4.Afișarea tuturor numerelor din listă care sunt superprime. ")
    print("5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor ")
    print("6.Iesire program.")


def citire_lista():
    list = []
    n = int(input("Cititi numarul de elemente: "))
    for i in range(n):
        list.append(int(input()))
    return list


def afisare_numere_negative(list):
    list = []
    n = int(input("Cititi numarul de elemente: "))
    for i in range(n):
        if i <= -1:
            i -= 1
            print(i)

def ultima_cifra(list, val):
    """
    Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură
    :param val: cifra
    :return val: cel mai mic numar din lista
    """
    min = 999
    ok = 0
    for x in list:
        if abs(x) % 10 == val:
            if min > x:
                min = x
                ok = 1

    if ok == 1:
        return min
    return None



def afisare_numere_superprime(list):
    if a < 2:
        return False
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True

n = int(input("Dati numarul de numere"))
for i in range(n):
    a = int(input("Dati un numar"))
    if superprim(a) == False:
        print("Numarul nu este superprim")
    else:
        print("Numarul este superprim")


def test_numere_superprime():
    assert prim(8) == False
    assert prim(5) == True
test_numere_superprime()


def main():


    test_numere_superprime()
    list = []
    while True:
        print_meniu()
        option = int(input("Alegeti optiunea:"))
        if option == 1:
            list = citire_lista()
        elif option == 2:
            print(afisare_numere_negative(list))
        elif option == 3:
            print()
        elif option == 4:
            print(afisare_numere_superprime(list))
        elif option == 5:
            print(ultima_cifra(list, val))
        elif option == 6:
            break
        else:
            print("optiune invalida ! Reincercati !")


if __name_ == "_main_":
 main()
