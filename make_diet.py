from diet import Diet
import time
import collections
while True:
    print("========================================================================================")
    print("================================== Kreator Diety =======================================")
    print("1. Stwórz dietę (algorytm losowy)")
    print("2. Wyjdz z kreatora")
    choice = input("Co chcesz zrobić?(wybierz 1/2): ")
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
        diet_price = 2000
        diet = Diet(weight=weight,
                    height=height,
                    sex=sex,
                    csv_file_with_products="products.csv",
                    price=diet_price
                    )
        print(diet.print_monthly_mekroelements_demand())
        sample_diet = diet.create_random_diet()
        dupa = collections.Counter(sample_diet)
        print(type(dupa))

    else:
        print("wpisano nieprawidłową wartość, spróbuj ponownie")
        time.sleep(2)
        continue
