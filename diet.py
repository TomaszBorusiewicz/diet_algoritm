import random
import csv


class Diet(object):
    def __init__(self, csv_file_with_products, weight, height, sex, price):
        self.file_with_products = csv_file_with_products
        self.weight = weight
        self.height = height
        self.sex = sex
        self.price = price
        self.max_searching_counter = 100000

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
        print("Twoje miesięczne zapotrzebowanie to {} kcal (dziennie: {}) w tym makroelementy: \n"
              "Węglowodany: {} gram (dziennie: {})\n"
              "Białko: {} gram (dziennie: {})\n"
              "Tłuszcze: {} gram (dziennie: {})".format(makroelements["kilokalorie"],
                                                        makroelements["kilokalorie"] / 30,
                                                        makroelements["weglowodany"],
                                                        makroelements["weglowodany"] / 30,
                                                        makroelements["bialko"],
                                                        makroelements["bialko"] / 30,
                                                        makroelements["tluszcz"],
                                                        makroelements["tluszcz"] / 30))

    def get_all_products_from_csv(self):
        all_products = []
        with open(self.file_with_products, encoding="utf8") as file:
            products = csv.reader(file, delimiter=",")
            for product in products:
                all_products.append(product)
        return all_products

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

    def check_if_actual_price_not_exceed_given_price(self, actual_price):
        if self.max_searching_counter > 0:
            self.max_searching_counter -= 1
            if actual_price < self.price:
                return True
        else:
            print("program nie potrafi znaleść diety dla podanego zakresu cenowego")
            exit(0)

    def get_products_from_csv_where_makroelement_has_value_less_than(self, makroelement_name, value):
        listed_products = []
        flag = 0
        if makroelement_name == "weglowodany":
            flag = 3
        elif makroelement_name == "bialko":
            flag = 1
        elif makroelement_name == "tluszcz":
            flag = 2
        with open(self.file_with_products, encoding="utf8") as file:
            products = csv.reader(file, delimiter=",")
            for row in products:
                if float(row[flag]) < value:
                    listed_products.append(row)
        return listed_products

    def get_product_from_csv_where_catbo_is_less_than(self, less_than_value):
        carbon_products = self.get_products_from_csv_where_makroelement_has_value_less_than("weglowodany",
                                                                                            less_than_value)
        random_number = random.randint(0, len(carbon_products))
        random_product = carbon_products[random_number]
        return random_product

    def get_product_from_csv_where_protein_is_less_than(self, less_than_value):
        protein_products = self.get_products_from_csv_where_makroelement_has_value_less_than("bialko",
                                                                                             less_than_value)
        random_number = random.randint(0, len(protein_products))
        random_product = protein_products[random_number]
        return random_product

    def get_product_from_csv_where_fat_is_less_than(self, less_than_value):
        fat_products = self.get_products_from_csv_where_makroelement_has_value_less_than("tluszcz",
                                                                                         less_than_value)
        random_number = random.randint(0, len(fat_products) - 1)
        random_product = fat_products[random_number]
        return random_product

    def get_product_from_csv_where_catbo_and_protein_is_less_than(self, less_than_value):
        carbon_product = self.get_products_from_csv_where_makroelement_has_value_less_than("weglowodany",
                                                                                           less_than_value)
        protein_product = self.get_products_from_csv_where_makroelement_has_value_less_than("bialko",
                                                                                            less_than_value)
        compared_list = [i for i in carbon_product if i in protein_product]
        random_number = random.randint(0, len(compared_list) - 1)
        random_product = compared_list[random_number]
        return random_product

    def get_product_from_csv_where_carbo_and_fat_is_less_than(self, less_than_value):
        carbon_product = self.get_products_from_csv_where_makroelement_has_value_less_than("weglowodany",
                                                                                           less_than_value)
        fat_product = self.get_products_from_csv_where_makroelement_has_value_less_than("tluszcz",
                                                                                        less_than_value)
        compared_list = [i for i in carbon_product if i in fat_product]
        random_number = random.randint(0, len(compared_list) - 1)
        random_product = compared_list[random_number]
        return random_product

    def get_product_from_csv_where_protein_and_fat_is_less_than(self, less_than_value):
        fat_product = self.get_products_from_csv_where_makroelement_has_value_less_than("tluszcz",
                                                                                        less_than_value)
        protein_product = self.get_products_from_csv_where_makroelement_has_value_less_than("bialko",
                                                                                            less_than_value)
        compared_list = [i for i in fat_product if i in protein_product]
        random_number = random.randint(0, len(compared_list) - 1)
        random_product = compared_list[random_number]
        return random_product

    def create_diet_random_algorithm(self):
        products_list = []
        actual_price = 0
        actual_carbohydrates = 0
        actual_protein = 0
        actual_fat = 0
        all_demands = self.makroelements_demand_for_month()
        while (int(actual_carbohydrates) < int(all_demands["weglowodany"] * 0.99)
               or int(actual_protein) < int(all_demands["bialko"] * 0.99)
               or int(actual_fat) < int(all_demands["tluszcz"] * 0.99)):

            if int(actual_carbohydrates) < int(all_demands["weglowodany"] * 0.99)\
                    and int(actual_protein) < int(all_demands["bialko"] * 0.99)\
                    and int(actual_fat) < int(all_demands["tluszcz"] * 0.99):
                try:
                    random_product = self.get_random_product_from_csv()
                    actual_carbohydrates += float(random_product[3])
                    actual_protein += float(random_product[1])
                    actual_fat += float(random_product[2])
                    actual_price += float(random_product[4])
                    products_list.append(random_product[0])
                except TypeError:
                    continue
                if self.check_if_actual_price_not_exceed_given_price(actual_price):
                    continue
                else:
                    self.create_diet_random_algorithm()
            elif (int(actual_carbohydrates) >= int(all_demands["weglowodany"] * 0.99)
                    and int(actual_protein) < int(all_demands["bialko"] * 0.99)
                    and int(actual_fat) < int(all_demands["tluszcz"] * 0.99)):
                try:
                    random_product = self.get_product_from_csv_where_catbo_is_less_than(2.0)
                    actual_carbohydrates += float(random_product[3])
                    actual_protein += float(random_product[1])
                    actual_fat += float(random_product[2])
                    actual_price += float(random_product[4])
                    products_list.append(random_product[0])
                except TypeError:
                    continue
                if self.check_if_actual_price_not_exceed_given_price(actual_price):
                    continue
                else:
                    self.create_diet_random_algorithm()
            elif (int(actual_carbohydrates) < int(all_demands["weglowodany"] * 0.99)
                    and int(actual_protein) >= int(all_demands["bialko"] * 0.99)
                    and int(actual_fat) < int(all_demands["tluszcz"] * 0.99)):
                try:
                    random_product = self.get_product_from_csv_where_protein_is_less_than(2.0)
                    actual_carbohydrates += float(random_product[3])
                    actual_protein += float(random_product[1])
                    actual_fat += float(random_product[2])
                    actual_price += float(random_product[4])
                    products_list.append(random_product[0])
                except TypeError:
                    continue
                if self.check_if_actual_price_not_exceed_given_price(actual_price):
                    continue
                else:
                    self.create_diet_random_algorithm()
            elif (int(actual_carbohydrates) < int(all_demands["weglowodany"] * 0.99)
                    and int(actual_protein) < int(all_demands["bialko"] * 0.99)
                    and int(actual_fat) >= int(all_demands["tluszcz"] * 0.99)):
                try:
                    random_product = self.get_product_from_csv_where_fat_is_less_than(2.0)
                    actual_carbohydrates += float(random_product[3])
                    actual_protein += float(random_product[1])
                    actual_fat += float(random_product[2])
                    actual_price += float(random_product[4])
                    products_list.append(random_product[0])
                except TypeError:
                    continue
                if self.check_if_actual_price_not_exceed_given_price(actual_price):
                    continue
                else:
                    self.create_diet_random_algorithm()
            elif (int(actual_carbohydrates) >= int(all_demands["weglowodany"] * 0.99)
                    and int(actual_protein) >= int(all_demands["bialko"] * 0.99)
                    and int(actual_fat) < int(all_demands["tluszcz"] * 0.99)):
                try:
                    random_product = self.get_product_from_csv_where_catbo_and_protein_is_less_than(2.0)
                    actual_carbohydrates += float(random_product[3])
                    actual_protein += float(random_product[1])
                    actual_fat += float(random_product[2])
                    actual_price += float(random_product[4])
                    products_list.append(random_product[0])
                except TypeError:
                    continue
                if self.check_if_actual_price_not_exceed_given_price(actual_price):
                    continue
                else:
                    self.create_diet_random_algorithm()
            elif (int(actual_carbohydrates) >= int(all_demands["weglowodany"] * 0.99)
                    and int(actual_protein) < int(all_demands["bialko"] * 0.99)
                    and int(actual_fat) >= int(all_demands["tluszcz"] * 0.99)):
                try:
                    random_product = self.get_product_from_csv_where_carbo_and_fat_is_less_than(2.0)
                    actual_carbohydrates += float(random_product[3])
                    actual_protein += float(random_product[1])
                    actual_fat += float(random_product[2])
                    actual_price += float(random_product[4])
                    products_list.append(random_product[0])
                except TypeError:
                    continue
                if self.check_if_actual_price_not_exceed_given_price(actual_price):
                    continue
                else:
                    self.create_diet_random_algorithm()
            elif (int(actual_carbohydrates) < int(all_demands["weglowodany"] * 0.99)
                    and int(actual_protein) >= int(all_demands["bialko"] * 0.99)
                    and int(actual_fat) >= int(all_demands["tluszcz"] * 0.99)):
                try:
                    random_product = self.get_product_from_csv_where_protein_and_fat_is_less_than(2.0)
                    actual_carbohydrates += float(random_product[3])
                    actual_protein += float(random_product[1])
                    actual_fat += float(random_product[2])
                    actual_price += float(random_product[4])
                    products_list.append(random_product[0])
                except TypeError:
                    continue
                if self.check_if_actual_price_not_exceed_given_price(actual_price):
                    continue
                else:
                    self.create_diet_random_algorithm()
        information = [int(actual_carbohydrates), int(actual_protein), int(actual_fat), int(actual_price)]
        return products_list, information

    def create_diet_greedy_algorithm(self):
        products_list = []
        actual_price, actual_carbohydrates, actual_protein, actual_fat = 0, 0, 0, 0
        carbohydrates_best_ratio, protein_best_ratio, fat_best_ratio = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
        all_demands = self.makroelements_demand_for_month()
        all_products = self.get_all_products_from_csv()
        print(all_products)
        for product in all_products:
            carbohydrates_ratio = float(product[3]) / float(product[4])
            protein_ratio = float(product[1]) / float(product[4])
            fat_ratio = float(product[2]) / float(product[4])
            if float(carbohydrates_ratio) > float(carbohydrates_best_ratio[3]):
                carbohydrates_best_ratio = product
            if float(protein_ratio) > float(protein_best_ratio[1]):
                protein_best_ratio = product
            if float(fat_ratio) > float(fat_best_ratio[2]):
                fat_best_ratio = product
        while int(actual_carbohydrates) < int(all_demands["weglowodany"] * 0.99):
            products_list.append(carbohydrates_best_ratio[0])
            actual_carbohydrates += float(carbohydrates_best_ratio[3])
            actual_protein += float(carbohydrates_best_ratio[1])
            actual_fat += float(carbohydrates_best_ratio[2])
            actual_price += float(carbohydrates_best_ratio[4])
            if self.check_if_actual_price_not_exceed_given_price(actual_price):
                continue
            else:
                self.create_diet_greedy_algorithm()
        while int(actual_protein) < int(all_demands["bialko"] * 0.99):
            protein_best_ratio = self.get_product_from_csv_where_carbo_and_fat_is_less_than(1.0)
            products_list.append(protein_best_ratio[0])
            actual_carbohydrates += float(protein_best_ratio[3])
            actual_protein += float(protein_best_ratio[1])
            actual_fat += float(protein_best_ratio[2])
            actual_price += float(protein_best_ratio[4])
            if self.check_if_actual_price_not_exceed_given_price(actual_price):
                continue
            else:
                self.create_diet_greedy_algorithm()
        while int(actual_fat) < int(all_demands["tluszcz"] * 0.99):
            fat_best_ratio = self.get_product_from_csv_where_catbo_and_protein_is_less_than(1.0)
            products_list.append(fat_best_ratio[0])
            actual_carbohydrates += float(fat_best_ratio[3])
            actual_protein += float(fat_best_ratio[1])
            actual_fat += float(fat_best_ratio[2])
            actual_price += float(fat_best_ratio[4])
            if self.check_if_actual_price_not_exceed_given_price(actual_price):
                continue
            else:
                self.create_diet_greedy_algorithm()
        information = [int(actual_carbohydrates), int(actual_protein), int(actual_fat), int(actual_price)]
        return products_list, information


