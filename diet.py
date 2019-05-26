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
        demands = {"kilokalorie": kilocalories, "carbo": carbohydrate,
                   "protein": protein, "fat": fat}
        return demands

    def print_monthly_mekroelements_demand(self):
        makroelements = self.makroelements_demand_for_month()
        print("Twoje miesięczne zapotrzebowanie to {} kcal (dziennie: {}) w tym makroelementy: \n"
              "Węglowodany: {} gram (dziennie: {})\n"
              "Białko: {} gram (dziennie: {})\n"
              "Tłuszcze: {} gram (dziennie: {})".format(int(makroelements["kilokalorie"]),
                                                        int(makroelements["kilokalorie"] / 30),
                                                        int(makroelements["carbo"]),
                                                        int(makroelements["carbo"] / 30),
                                                        int(makroelements["protein"]),
                                                        int(makroelements["protein"] / 30),
                                                        int(makroelements["fat"]),
                                                        int(makroelements["fat"] / 30)))

    def split_products_for_3_lists(self, products):
        most_carbo = []
        most_protein = []
        most_fat = []
        dicto = {}
        for product in products:
            if float(product[1]) > float(product[2]) and float(product[1]) > float(product[3]):
                most_protein.append(product)
            elif float(product[2]) > float(product[1]) and float(product[2]) > float(product[3]):
                most_fat.append(product)
            else:
                most_carbo.append(product)
        dicto["carbo"] = most_carbo
        dicto["protein"] = most_protein
        dicto["fat"] = most_fat
        return dicto

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

    def get_makros_info_based_on_name(self, product_name):
        with open(self.file_with_products, encoding="utf8") as file:
            products = csv.reader(file, delimiter=",")
            for row in products:
                if row[0] == product_name:
                    return row[0:]

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

    def get_product_from_csv_with_best_carbo_ratio(self, less_than_value):
        carbo_best_ratio_product = [0, 0, 0, 0, 1]
        fat_product = self.get_products_from_csv_where_makroelement_has_value_less_than("tluszcz",
                                                                                        less_than_value)
        protein_product = self.get_products_from_csv_where_makroelement_has_value_less_than("bialko",
                                                                                            less_than_value)
        compared_list = [i for i in fat_product if i in protein_product]
        for product in compared_list:
            if float(product[2]) / float(product[4]) \
                    > float(carbo_best_ratio_product[2]) / float(carbo_best_ratio_product[4]):
                carbo_best_ratio_product = product
        return carbo_best_ratio_product

    def get_product_from_csv_with_best_protein_ratio(self, less_than_value):
        protein_best_ratio_product = [0, 0, 0, 0, 1]
        carbon_product = self.get_products_from_csv_where_makroelement_has_value_less_than("weglowodany",
                                                                                           less_than_value)
        fat_product = self.get_products_from_csv_where_makroelement_has_value_less_than("tluszcz",
                                                                                        less_than_value)
        compared_list = [i for i in carbon_product if i in fat_product]
        for product in compared_list:
            if float(product[2]) / float(product[4]) \
                    > float(protein_best_ratio_product[2]) / float(protein_best_ratio_product[4]):
                protein_best_ratio_product = product
        return protein_best_ratio_product

    def get_product_from_csv_with_best_fat_ratio(self, less_than_value):
        fat_best_ratio_product = [0, 0, 0, 0, 1]
        carbon_product = self.get_products_from_csv_where_makroelement_has_value_less_than("weglowodany",
                                                                                           less_than_value)
        protein_product = self.get_products_from_csv_where_makroelement_has_value_less_than("bialko",
                                                                                            less_than_value)
        compared_list = [i for i in carbon_product if i in protein_product]
        for product in compared_list:
            if float(product[2]) / float(product[4])\
            > float(fat_best_ratio_product[2]) / float(fat_best_ratio_product[4]):
                fat_best_ratio_product = product
        return fat_best_ratio_product

    def get_product_with_best_ratio(self,product_type, products_list):
        best_product = []
        ratio = 0
        if product_type == "carbo":
            for product in products_list:
                if float(product[3]) / float(product[4]) \
                        > ratio:
                    best_product = product
                    ratio = float(product[3]) / float(product[4])
        if product_type == "protein":
            for product in products_list:
                if float(product[1]) / float(product[4]) \
                        > ratio:
                    best_product = product
                    ratio = float(product[1]) / float(product[4])
        if product_type == "fat":
            for product in products_list:
                if float(product[2]) / float(product[4]) \
                        > ratio:
                    best_product = product
                    ratio = float(product[2]) / float(product[4])
        return best_product

    def get_product_from_given_dict_random(self, dictionary):
        return random.choice(dictionary[random.choice(list(dictionary))])

    def get_product_from_given_dict_greedy(self, dictionary):
        macro_item = random.choice(list(dictionary))
        return self.get_product_with_best_ratio(product_type=macro_item, products_list=dictionary[macro_item])

    def create_diet(self, algorithm):
        products_list = []
        carbo_break_point, protein_break_point, fat_break_point = 10, 10, 10
        actual_macros_and_price = {"carbo": 0, "protein": 0, "fat": 0, "price": 0}
        demands_macros = self.makroelements_demand_for_month()
        all_products = self.get_all_products_from_csv()
        items_to_choose = self.split_products_for_3_lists(products=all_products)
        items_not_to_choose = {}
        while (actual_macros_and_price["price"] < float(self.price)) \
                and (float(actual_macros_and_price["carbo"] < float(demands_macros["carbo"] * 0.999))
                     or float(actual_macros_and_price["protein"] < float(demands_macros["protein"] * 0.999))
                     or float(actual_macros_and_price["fat"] < float(demands_macros["fat"] * 0.999))):
            if len(items_to_choose) == 0:
                items_to_choose["carbo"] = items_not_to_choose["carbo"]
                items_to_choose["protein"] = items_not_to_choose["protein"]
                items_to_choose["fat"] = items_not_to_choose["fat"]
            if algorithm == "random":
                product = self.get_product_from_given_dict_random(items_to_choose)
            elif algorithm == "greedy":
                product = self.get_product_from_given_dict_greedy(items_to_choose)
            if product is None:
                continue
            products_list.append(product[0])
            actual_macros_and_price["carbo"] += float(product[3])
            actual_macros_and_price["protein"] += float(product[1])
            actual_macros_and_price["fat"] += float(product[2])
            actual_macros_and_price["price"] += float(product[4])
            if "carbo" in items_to_choose.keys() \
                    and (int(actual_macros_and_price["carbo"]) > (int(demands_macros["carbo"])
                                                                  * carbo_break_point) / 100):
                del_items = items_to_choose["carbo"]
                items_not_to_choose["carbo"] = del_items
                del items_to_choose["carbo"]
                if carbo_break_point == 100:
                    continue
                else:
                    carbo_break_point += 10
            if "protein" in items_to_choose.keys() \
                    and (int(actual_macros_and_price["protein"]) > (int(demands_macros["protein"])
                                                                    * protein_break_point) / 100):
                del_items = items_to_choose["protein"]
                items_not_to_choose["protein"] = del_items
                del items_to_choose["protein"]
                if protein_break_point == 100:
                    continue
                else:
                    protein_break_point += 10
            if "fat" in items_to_choose.keys() \
                    and (int(actual_macros_and_price["fat"]) > (int(demands_macros["fat"]) * fat_break_point) / 100):
                del_items = items_to_choose["fat"]
                items_not_to_choose["fat"] = del_items
                del items_to_choose["fat"]
                if fat_break_point == 100:
                    continue
                else:
                    fat_break_point += 10

        return products_list, actual_macros_and_price, algorithm

    def create_diet_random_algorithm(self):
        return self.create_diet(algorithm="random")

    def create_diet_greedy_algorithm(self):
        return self.create_diet(algorithm="greedy")

    def create_diet_greedy_algorithm_fit_to_price(self, diet_price):
        greedy_diet = self.create_diet_greedy_algorithm()
        products_list = greedy_diet[0]
        information = greedy_diet[1]
        list_length = len(products_list)
        counter = 0
        actual_carbo, actual_protein, actual_fat, actual_price = 0, 0, 0, 0
        for product in products_list:
            product_makros = self.get_makros_info_based_on_name(product)
            actual_carbo += float(product_makros[3])
            actual_protein += float(product_makros[1])
            actual_fat += float(product_makros[2])
            actual_price += float(product_makros[4])
        for i in range(0, list_length):
            removed_item = products_list.pop(0)
            removed_item_makros = self.get_makros_info_based_on_name(removed_item)
            actual_carbo -= float(removed_item_makros[3])
            actual_protein -= float(removed_item_makros[1])
            actual_fat -= float(removed_item_makros[2])
            actual_price -= float(removed_item_makros[4])
            while actual_carbo < float(information[0]):
                getted_product = self.get_product_from_csv_where_protein_and_fat_is_less_than(1.0)
                products_list.append(getted_product[0])
                actual_carbo += float(getted_product[3])
                actual_protein += float(getted_product[1])
                actual_fat += float(getted_product[2])
                actual_price += float(getted_product[4])
            while actual_protein < float(information[1]):
                getted_product = self.get_product_from_csv_where_carbo_and_fat_is_less_than(1.0)
                products_list.append(getted_product[0])
                actual_carbo += float(getted_product[3])
                actual_protein += float(getted_product[1])
                actual_fat += float(getted_product[2])
                actual_price += float(getted_product[4])
            while actual_fat < float(information[2]):
                getted_product = self.get_product_from_csv_where_catbo_and_protein_is_less_than(1.0)
                products_list.append(getted_product[0])
                actual_carbo += float(getted_product[3])
                actual_protein += float(getted_product[1])
                actual_fat += float(getted_product[2])
                actual_price += float(getted_product[4])
            counter += 1
            if actual_price > diet_price:
                break
            elif counter == int(list_length):
                print("Maksymalna cena jest zbyt wysoka.")
        total_information = [int(actual_carbo), int(actual_protein), int(actual_fat), int(actual_price)]
        return products_list, total_information




