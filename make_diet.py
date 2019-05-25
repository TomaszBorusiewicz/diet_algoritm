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
    print("4. Stwórz dietę (algorytm zachłanny lepsze dopasowanie do ceny)")
    print("5. Wyjdz z kreatora")


def display_result(diet):
    countered_diet_lists = collections.Counter(diet[0])
    print("==================================================================================")
    print("Makroelementy na miesiąc w znalezionej diecie:\nWęglowodany: {} gram\nBiałko: {} gram"
          "\nTłuszcz: {} gram\nCena diety {} złotych".format(int(diet[1]["carbo"]), int(diet[1]["protein"]),
                                                             int(diet[1]["fat"]), int(diet[1]["price"])))
    for product in countered_diet_lists:
        print("{}  {} gram".format(product, countered_diet_lists[product] * 100))


while True:
    display_menu()
    choice = input("Wybierz co chcesz zrobić 1/2/3/4: ")
    # choice = "3"
    if choice == "5":
        exit(0)
    elif choice == "1" or choice == "2" or choice == "3" or choice == "4":
        # weight = float(input("Podaj swoją wagę[kg]: "))
        # height = input("Podaj swoj wzrost[cm]: ")
        # sex = input("Podaj swoją płeć(wpisz mezczyzna/kobieta): ")
        # diet_price = float(input("Wpisz kwotę którą przeznaczysz na miesięczną dietę[zł]: "))
        weight = 80
        height = 180
        sex = "mezczyzna"
        diet_price = 100
        diet = Diet(weight=weight,
                    height=height,
                    sex=sex,
                    csv_file_with_products="products.csv",
                    price=diet_price
                    )
        diet.print_monthly_mekroelements_demand()
        if choice == "1":
            time_before = time.time()
            choosen_diet = diet.create_diet_random_algorithm()
            time_after = time.time()
            display_result(choosen_diet)
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
                diets_list.sort(key=lambda x: float(x[1]["price"]))
            elif choosen_price == "najdrozsza":
                diets_list.sort(key=lambda x: float(x[1]["price"]), reverse=True)
            else:
                "wpisano złą wartość."
                continue
            choosen_diet = diets_list[0]
            display_result(choosen_diet)
            print("czas szukania: {} sekund".format(math.floor(time_after - time_before)))
        elif choice == "3":
            time_before = time.time()
            choosen_diet = diet.create_diet_greedy_algorithm()
            time_after = time.time()
            display_result(choosen_diet)
            print("czas szukania: {} sekund".format(math.floor(time_after - time_before)))

        elif choice == "4":
            time_before = time.time()
            choosen_diet = diet.create_diet_greedy_algorithm_fit_to_price(diet_price)
            time_after = time.time()
            display_result(choosen_diet)
            print("czas szukania: {} sekund".format(math.floor(time_after - time_before)))
    else:
        print("wpisano nieprawidłową wartość, spróbuj ponownie")
        time.sleep(1)
        continue
