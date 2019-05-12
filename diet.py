import random
import csv


class Diet(object):
    def __init__(self, csv_file_with_products, weight, height, sex, price):
        self.file_with_products = csv_file_with_products
        self.weight = weight
        self.height = height
        self.sex = sex
        self.price = price

    def kilocalorie_demand_for_month(self):
        return int((33 * self.weight) * 30)

    def protein_demand_for_month(self):
        return int((2 * self.weight) * 30)

    def fat_demand_for_month(self):
        return int((self.kilocalorie_demand_for_month() / 4) / 9)

    def carbohydrate_demand_for_month(self):
        protein = self.protein_demand_for_month() * 4
        fat = self.fat_demand_for_month() * 9
        return int((self.kilocalorie_demand_for_month() -
                   (protein + fat)) / 4)

    def makroelements_demand_for_month(self):
        kilocalories = self.kilocalorie_demand_for_month()
        protein = self.protein_demand_for_month()
        fat = self.fat_demand_for_month()
        carbohydrate = self.carbohydrate_demand_for_month()
        demands = {"kilokalorie": kilocalories, "weglowodany": carbohydrate,
                   "bialko": protein, "tluszcz": fat}
        return demands

    def print_monthly_mekroelements_demand(self):
        makroelements = self.makroelements_demand_for_month()
        print("Twoje miesięczne zapotrzebowanie to {} kcal w tym makroelementy: \n"
              "Węglowodany: {} gram\n"
              "Białko: {} gram\n"
              "Tłuszcze: {} gram".format(makroelements["kilokalorie"],
                                         makroelements["weglowodany"],
                                         makroelements["bialko"],
                                         makroelements["tluszcz"]))

    def get_product_from_csv(self, id):
        with open(self.file_with_products, encoding="utf8") as file:
            products = csv.reader(file, delimiter=",")
            for counter, row in enumerate(products):
                if int(counter) == int(id):
                    return row[0:]

    def get_random_product_from_csv(self):
        with open(self.file_with_products, encoding="utf8") as file:
            products = csv.reader(file, delimiter=",")
            row_count = sum(1 for row in products)
        random_id = random.randint(0, row_count)
        return self.get_product_from_csv(random_id)

    def create_random_diet(self):
        products_list = []
        actual_price = 0
        actual_carbohydrates = 0
        actual_protein = 0
        actual_fat = 0
        all_demands = self.makroelements_demand_for_month()

        while actual_price < self.price:
            try:
                print(actual_price, actual_carbohydrates, actual_protein, actual_fat)
                random_product = self.get_random_product_from_csv()
                actual_carbohydrates += float(random_product[3])
                actual_protein += float(random_product[1])
                actual_fat += float(random_product[2])
                actual_price += float(random_product[4])
                products_list.append(random_product[0])
            except TypeError:
                continue
        return products_list


