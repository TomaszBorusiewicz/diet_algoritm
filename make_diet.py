from diet import Diet
import time
import collections
import  datetime
while True:
    print("========================================================================================")
    print("================================== Kreator Diety =======================================")
    print("1. Stwórz dietę (algorytm losowy)")
    print("2. Wyjdz z kreatora")
    # choice = input("Wybierz 1/2: ")
    choice = "1"
    if choice == "2":
        exit(0)
    elif choice == "1":
        # weight = input("Podaj swoją wagę[kg]: ")
        # height = input("Podaj swoj wzrost[cm]: ")
        # sex = input("Podaj swoją płeć(wpisz mezczyzna/kobieta): ")
        # diet_price = input("Wpisz kwotę którą przeznaczysz na miesięczną dietę[zł]: ")
        weight = 50
        height = 180
        sex = "mezczyzna"
        diet_price = 1800
        diet = Diet(weight=weight,
                    height=height,
                    sex=sex,
                    csv_file_with_products="products.csv",
                    price=diet_price
                    )
        diet.print_monthly_mekroelements_demand()
        time_before = time.time()
        sample_diet = diet.create_random_diet()
        time_after = time.time()
        dupa = collections.Counter(sample_diet[0])
        print("==================================================================================")
        print("Makroelementy na miesiąc w znalezionej diecie:\nWęglowodany: {} gram\nBiałko: {} gram"
              "\nTłuszcz: {} gram\nCena diety {} złotych".format(sample_diet[1][0], sample_diet[1][1],
                                                               sample_diet[1][2], sample_diet[1][3]))
        for i in dupa:
            print("{}  {} gram".format(i, dupa[i]*100))

        print("czas szukania: {} sekund".format(time_after - time_before))

    else:
        print("wpisano nieprawidłową wartość, spróbuj ponownie")
        time.sleep(2)
        continue
