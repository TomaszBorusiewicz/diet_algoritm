import diet_algoritm.diet as diet

# dieet = diet.Diet(100, 180, "male")
#
#
# def test_daily_demand():
#     test = dieet.makroelements_demand_for_month()
#     print(test)


waga = input("Podaj swoją wagę: ")
wzrost = input("Podaj swój wzrost: ")
plec = input("podaj swoją płeć: ")

dieta = diet.Diet(int(waga), int(wzrost), plec)
print(dieta.print_monthly_mekroelements_demand())
