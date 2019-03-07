import diet_algoritm.diet as diet

dieet = diet.Diet(100, 180, "male")


def test_daily_demand():
    test = dieet.makroelements_demand_for_month()
    print(test)


