from pymongo import MongoClient
client = MongoClient("localhost", 27017)

db = client.local
collection = client.products


print(db)

class Diet:

    products = [{"name": "czekolada", "makroelements": {"kilocalories": 527,
                                                        "cabrohydrate": 63,
                                                        "protein": 3.6,
                                                        "fat": 29}}]

    def __init__(self, weight, height, sex):
        self.weight = weight
        self.height = height
        self.sex = sex

    def kilocalorie_demand_for_month(self):
        return int((33 * self.weight) * 30)

    def protein_demand_for_month(self):
        return int((2 * self.weight) * 30)

    def fat_demand_for_month(self):
        return int(((self.kilocalorie_demand_for_month() / 4) / 9) * 30)

    def carbohydrate_demand_for_month(self):
        return int(((self.kilocalorie_demand_for_month() -
                   (self.protein_demand_for_month() + self.fat_demand_for_month())) / 4) * 30)

    def makroelements_demand_for_month(self):
        kilocalories = self.kilocalorie_demand_for_month()
        protein = self.protein_demand_for_month()
        fat = self.fat_demand_for_month()
        carbohydrate = self.carbohydrate_demand_for_month()
        return kilocalories, protein, fat, carbohydrate

    def print_monthly_mekroelements_demand(self):
        makroelements = self.makroelements_demand_for_month()
        print("Twoje miesięczne zapotrzebowanie to {} kcal w tym makroelementy: \n"
              "Węglowodany: {} gram\n"
              "Białko: {} gram\n"
              "Tłuszcze: {} gram".format(makroelements[0],
                                         makroelements[3],
                                         makroelements[1],
                                         makroelements[2]))

    def make_diet(self):
        kilocalories = self.products[0].get("makroelements").get("kilocalories")
        monthly_demand = self.makroelements_demand_for_month()
        kilocalories_demand = monthly_demand[0]
        print(int(kilocalories_demand / kilocalories * 100))
        print(kilocalories)

