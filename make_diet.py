from diet import Diet
import time
import collections
import math


def display_menu():
    print("========================================================================================")
    print("================================== Kreator Diety =======================================")
    print("1. Stwórz dietę (algorytm losowy)")
    print("2. Stwórz dietę (algorytm losowy z opcją najtańszej/najdroższej diety)")
    print("3. Stwórz dietę (algorytm zachłanny)")
    print("4. Wyjdz z kreatora")


while True:
    display_menu()
    # choice = input("Wybierz co chcesz zrobić 1/2/3/4: ")
    choice = "3"
    if choice == "4":
        exit(0)
    elif choice == "1" or choice == "2" or choice == "3":
        # weight = input("Podaj swoją wagę[kg]: ")
        # height = input("Podaj swoj wzrost[cm]: ")
        # sex = input("Podaj swoją płeć(wpisz mezczyzna/kobieta): ")
        # diet_price = input("Wpisz kwotę którą przeznaczysz na miesięczną dietę[zł]: ")
        weight = 80
        height = 180
        sex = "mezczyzna"
        diet_price = 10000
        diet = Diet(weight=weight,
                    height=height,
                    sex=sex,
                    csv_file_with_products="products.csv",
                    price=diet_price
                    )
        diet.print_monthly_mekroelements_demand()
        if choice == "1":
            time_before = time.time()
            chosen_diet = diet.create_diet_random_algorithm()
            time_after = time.time()
            countered_diet_lists = collections.Counter(chosen_diet[0])
            print("==================================================================================")
            print("Makroelementy na miesiąc w znalezionej diecie:\nWęglowodany: {} gram\nBiałko: {} gram"
                  "\nTłuszcz: {} gram\nCena diety {} złotych".format(chosen_diet[1][0], chosen_diet[1][1],
                                                                     chosen_diet[1][2], chosen_diet[1][3]))
            for i in countered_diet_lists:
                print("{}  {} gram".format(i, countered_diet_lists[i] * 100))
            print("czas szukania: {} sekund".format(math.floor(time_after - time_before)))
        elif choice == "2":
            number_of_diets = 100
            diets_list = []
            time_before = time.time()
            for i in range(0, number_of_diets):
                sample_diet = diet.create_diet_random_algorithm()
                diets_list.append(sample_diet)
            time_after = time.time()
            choosen_price = input("Którą opcję wybierasz? (wpisz najtansza/najdrozsza): ")
            if choosen_price == "najtansza":
                diets_list.sort(key=lambda x: x[1][3])
            elif choosen_price == "najdrozsza":
                diets_list.sort(key=lambda x: x[1][3], reverse=True)
            else:
                "wpisano złą wartość."
                continue
            cheapest_diet = diets_list[0]
            countered_diet_lists = collections.Counter(cheapest_diet[0])
            print("==================================================================================")
            print("Makroelementy na miesiąc w znalezionej diecie:\nWęglowodany: {} gram\nBiałko: {} gram"
                  "\nTłuszcz: {} gram\nCena diety {} złotych".format(cheapest_diet[1][0], cheapest_diet[1][1],
                                                                     cheapest_diet[1][2], cheapest_diet[1][3]))
            for i in countered_diet_lists:
                print("{}  {} gram".format(i, countered_diet_lists[i]*100))
            print("czas szukania: {} sekund".format(math.floor(time_after - time_before)))
        elif choice == "3":
            time_before = time.time()
            chosen_diet = diet.create_diet_greedy_algorithm()
            time_after = time.time()
            countered_diet_lists = collections.Counter(chosen_diet[0])
            print("==================================================================================")
            print("Makroelementy na miesiąc w znalezionej diecie:\nWęglowodany: {} gram\nBiałko: {} gram"
                  "\nTłuszcz: {} gram\nCena diety {} złotych".format(chosen_diet[1][0], chosen_diet[1][1],
                                                                     chosen_diet[1][2], chosen_diet[1][3]))
            for i in countered_diet_lists:
                print("{}  {} gram".format(i, countered_diet_lists[i] * 100))
            print("czas szukania: {} sekund".format(math.floor(time_after - time_before)))
            exit(0)

    else:
        print("wpisano nieprawidłową wartość, spróbuj ponownie")
        time.sleep(1)
        continue
