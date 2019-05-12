from diet_algoritm.diet import Diet

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
print(sample_diet)
