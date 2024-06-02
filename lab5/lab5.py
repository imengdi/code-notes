# Name: Mengdi Zhu
# Lab: Lab5


class UserInterface:
  def __init__(self):
    pass

  def __repr__(self):
    return self.__class__.__name__

  def print_menu(self):
    pass

  def read_user_choices(self):
    pass

  def print_receipt(self):
    pass


class Inventory:
  def __init__(self, file_name):
    self.__inventory_valid = True

    try:
      input_file = open(file_name, "r")
    except IOError as exception:
      self.__inventory_valid = False
      print("IO error info: ", str(exception))
      return

    self.__packaged_food = []
    self.__packaged_food_header = "Packaged food"

    self.__hot_food = []
    self.__hot_food_header = "Hot food"

    self.__drink = []
    self.__drink_header = "Drinks"

    # Loop through the rest rest data in text
    for line in input_file:
      items = line.strip().split(',')
      try:
        id_num = int(items[0])
        name = items[1]
        price = float(items[2])
        size = items[3]
      except ValueError as exception:
        print("Value error info: ", str(exception))
        continue

      if 10 <= id_num <= 19:
        self.__packaged_food.append(PackagedFood(name, id_num, price))

      elif 20 <= id_num <= 29:
        self.__hot_food.append(HotFood(name, id_num, price))

      elif 30 <= id_num <= 39:
        self.__drink.append(Drink(name, id_num, price, size))

      else:
        print("Error info: Sale item ID_NUM out of range ...")

    # Close file and return
    input_file.close()

  def __repr__(self):
    pfood_name = "Packaged food"
    pfood_num = len(self.__packaged_food)
    pfood = "{}: {}".format(pfood_name, pfood_num)

    hfood_name = "Hot food"
    hfood_num = len(self.__hot_food)
    hfood = "{}: {}".format(hfood_name, hfood_num)

    drink_name = "Drinks"
    drink_num = len(self.__drink)
    drink = "{}: {}".format(drink_name, drink_num)

    return "{}\n{}\n{}".format(pfood, hfood, drink)

  def inventory_status(self):
    return self.__inventory_valid

  def print_items(self):
    for pf in self.__packaged_food:
      print(pf)

    for hf in self.__hot_food:
      print(hf)

    for dk in self.__drink:
      print(dk)


class SaleItem:
  def __init__(self, name, id_num, price):
    self.name = name
    self.id_num = id_num
    self.price = price

  def __repr__(self):
    return "{}({}): {}".format(self.name, self.id_num, self.price)

  def print_hello(self):
    print("hello world")


class PackagedFood(SaleItem):
  def __init__(self, name, id_num, price):
    super().__init__(name, id_num, price)

  def __repr__(self):
    return super().__repr__()


class HotFood(SaleItem):
  def __init__(self, name, id_num, price):
    super().__init__(name, id_num, price)
    self.tax = 9.13 / 100

  def __repr__(self):
    return super().__repr__() + " - heated"


class Drink(SaleItem):
  def __init__(self, name, id_num, price, size):
    super().__init__(name, id_num, price)
    self.size = size
    self.tax = 9.13 / 100
    self.crv = {'S': 0.05, 'L': 0.10}

  def __repr__(self):
    return super().__repr__() + " - " + self.size


def main():
  b = Inventory("items.csv")
  if b.inventory_status():
    c = SaleItem("Water", "32", "1.5")
    d = HotFood("W", 33, 1.2)
    print(b)
    print(c)
    print(d)

    d.print_hello()

    b.print_items()


# Entry point of the program
main()

big = {1: "hello", 2: "world"}
key = 0

if key in big:
  print(big[key])
