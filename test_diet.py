import diet_algoritm.diet
import csv
algoritms = diet_algoritm.diet.Algorithms("products.csv", 1000)


# def test_get_sample_product():
sample_product = algoritms.get_product_from_csv(0)
print(sample_product)
all_ids = algoritms.get_random_product_from_csv()
print(all_ids)

# dieet = diet.Diet(100, 180, "male")
#
#
# def test_daily_demand():
#     test = dieet.makroelements_demand_for_month()
#     print(test)


# waga = input("Podaj swoją wagę: ")
# wzrost = input("Podaj swój wzrost: ")
# plec = input("podaj swoją płeć: ")
#
# dieta = diet.Diet(int(waga), int(wzrost), plec)
# print(dieta.print_monthly_mekroelements_demand())

# def get_product_from_csv(id):
#     with open("products.csv", encoding="utf8") as file:
#         products = csv.reader(file, delimiter=",")
#         for row in products:
#             print(row)
#
#
# dupa = get_product_from_csv(1)
# print(dupa)
