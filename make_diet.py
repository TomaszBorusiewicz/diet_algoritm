from diet import Diet
import time
import collections
import math


def display_menu():
    print("========================================================================================")
    print("================================== Kreator Diety =======================================")
    print("1. Stwórz dietę (algorytm losowy)")
    print("2. Wyjdz z kreatora")


while True:
    choice = input("Wybierz co chcesz zrobić 1/2: ")
    # choice = "1"
    if choice == "2":
        exit(0)
    elif choice == "1":
        # weight = input("Podaj swoją wagę[kg]: ")
        # height = input("Podaj swoj wzrost[cm]: ")
        # sex = input("Podaj swoją płeć(wpisz mezczyzna/kobieta): ")
        # diet_price = input("Wpisz kwotę którą przeznaczysz na miesięczną dietę[zł]: ")
        weight = 80
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
        number_of_diets = 100
        diets_list = []
        for i in range(0, number_of_diets):
            sample_diet = diet.create_random_diet()
            diets_list.append(sample_diet)
        time_after = time.time()
        diets_list.sort(key=lambda x: x[1][3])
        cheapest_diet = diets_list[0]
        countered_diet_lists = collections.Counter(cheapest_diet[0])
        print("==================================================================================")
        print("Makroelementy na miesiąc w znalezionej diecie:\nWęglowodany: {} gram\nBiałko: {} gram"
              "\nTłuszcz: {} gram\nCena diety {} złotych".format(cheapest_diet[1][0], cheapest_diet[1][1],
                                                                 cheapest_diet[1][2], cheapest_diet[1][3]))
        for i in countered_diet_lists:
            print("{}  {} gram".format(i, countered_diet_lists[i]*100))
        print("czas szukania: {} sekund".format(math.floor(time_after - time_before)))

    else:
        print("wpisano nieprawidłową wartość, spróbuj ponownie")
        time.sleep(1)
        continue
