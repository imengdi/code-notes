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
    self.__drink_header = "Drink"

    self.__inventory_dic = {}
    self.__inventory_dic[self.__packaged_food_header] = self.__packaged_food
    self.__inventory_dic[self.__hot_food_header] = self.__hot_food
    self.__inventory_dic[self.__drink_header] = self.__drink

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
        if size != "S" and size != "L":
          continue
        self.__drink.append(Drink(name, id_num, price, size))

      else:
        print("Error info: Sale item ID_NUM out of range ...")
        continue

    # Close file and return
    input_file.close()

  def __repr__(self):
    disp_info = []

    for item_header in self.__inventory_dic:
      item_num = len(self.__inventory_dic[item_header])
      if item_num > 1:
        item_name = item_header.lower() + "s"
      else:
        item_name = item_header.lower()
      item_info = "{} {}".format(item_num, item_name)
      disp_info.append(item_info)

    return "{}, {}, {}".format(disp_info[0], disp_info[1], disp_info[2])

  def inventory_status(self):
    return self.__inventory_valid

  def list_inventory_items(self):
    for item_header in self.__inventory_dic:
      print(item_header)
      for item_obj in self.__inventory_dic[item_header]:
        print(item_obj)
        item_obj.print_final_price()


class SaleItem:
  def __init__(self, name, id_num, price):
    self.name = name
    self.id_num = id_num
    self.price = price

  def __repr__(self):
    return "{}({}):{}".format(self.name, self.id_num, self.price)

  def print_final_price(self):
    pass


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

  def print_final_price(self):
    final_price = self.price * (1 + self.tax)
    print(round(final_price, 2))


class Drink(SaleItem):
  def __init__(self, name, id_num, price, size):
    super().__init__(name, id_num, price)
    self.size = size
    self.tax = 9.13 / 100
    self.crv = {'S': 0.05, 'L': 0.10}

  def __repr__(self):
    return super().__repr__()

  def print_final_price(self):
    final_price = (self.price + self.crv[self.size]) * (1 + self.tax)
    print(round(final_price, 2))


def main():
  b = Inventory("items.csv")
  if b.inventory_status():
    # c = SaleItem("Water", "32", "1.5")
    # d = HotFood("W", 33, 1.2)
    print(b)
    # print(c)
    # print(d)

    # d.print_hello()

    b.list_inventory_items()


# Entry point of the program
main()
