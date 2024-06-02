# Name: Mengdi Zhu
# Lab: Lab5

import sys


class UserInterface:
  def __init__(self):
    self.inst = Inventory("items.csv")

    if not self.inst.get_inventory_status():
      print("Program end ...")
      sys.exit(1)
    else:
      print(self.inst)

  def __repr__(self):
    return self.__class__.__name__

  def print_menu(self):
    self.inst.get_inventory_details()

  def read_user_choices(self):
    pass

  def print_receipt(self):
    pass


class Inventory:
  def __init__(self, file_name):
    self.__inventory_valid = True
    self.__inventory_dic = {}
    self.__inventory_summary = None

    try:
      input_file = open(file_name, "r")
    except IOError as exception:
      self.__inventory_valid = False
      print("IO error info: ", str(exception))
      return

    packaged_food_objs = []
    hot_food_objs = []
    drink_objs = []

    self.__inventory_dic["Packaged food"] = packaged_food_objs
    self.__inventory_dic["Hot food"] = hot_food_objs
    self.__inventory_dic["Drink"] = drink_objs

    # Loop through the data in csv file
    for line in input_file:
      items = line.strip().split(',')

      if len(items) != 4:
        print("Error info: Data field is not valid ...")
        continue

      try:
        id_num = int(items[0])
        name = items[1]
        price = float(items[2])
        size = items[3]
      except ValueError as exception:
        print("Value error info: ", str(exception))
        continue

      if 10 <= id_num <= 19:
        packaged_food_objs.append(PackagedFood(name, id_num, price))

      elif 20 <= id_num <= 29:
        hot_food_objs.append(HotFood(name, id_num, price))

      elif 30 <= id_num <= 39:
        if size != "S" and size != "L":
          print("Error info: Size info is not valid ...")
          continue
        drink_objs.append(Drink(name, id_num, price, size))

      else:
        print("Error info: Sale item ID_NUM out of range ...")
        continue

    # Close file and finish obj init
    input_file.close()

  def __repr__(self):
    if self.__inventory_summary is None:
      self.__inventory_summary = self.get_inventory_summary()
    return self.__inventory_summary

  def get_inventory_summary(self):
    disp_info = []

    for item_header in self.__inventory_dic:
      item_num = len(self.__inventory_dic[item_header])
      if item_num > 1:
        item_name = item_header.lower() + "s"
      else:
        item_name = item_header.lower()
      item_info = "{} {}".format(item_num, item_name)
      disp_info.append(item_info)

    return "{}, {}, {}\n".format(disp_info[0], disp_info[1], disp_info[2])

  def get_inventory_status(self):
    return self.__inventory_valid

  def get_inventory_details(self):
    for item_header in self.__inventory_dic:
      print(item_header)
      for item_obj in self.__inventory_dic[item_header]:
        print(item_obj)
        item_price = item_obj.get_final_price()
        if item_price != item_obj.get_input_price():
          print(item_price)


class SaleItem:
  def __init__(self, name, id_num, price):
    self.name = name
    self.id_num = id_num
    self.price = price

  def __repr__(self):
    return "{}({}):{}".format(self.name, self.id_num, self.price)

  def get_input_price(self):
    return self.price


class PackagedFood(SaleItem):
  def __init__(self, name, id_num, price):
    super().__init__(name, id_num, price)

  def __repr__(self):
    return super().__repr__()

  def get_final_price(self):
    return self.price


class HotFood(SaleItem):
  def __init__(self, name, id_num, price):
    super().__init__(name, id_num, price)
    self.tax = 9.13 / 100

  def __repr__(self):
    return super().__repr__() + " - heated"

  def get_final_price(self):
    final_price = self.price * (1 + self.tax)
    return round(final_price, 2)


class Drink(SaleItem):
  def __init__(self, name, id_num, price, size):
    super().__init__(name, id_num, price)
    self.size = size
    self.tax = 9.13 / 100
    self.crv = {'S': 0.05, 'L': 0.10}

  def __repr__(self):
    return super().__repr__()

  def get_final_price(self):
    final_price = (self.price + self.crv[self.size]) * (1 + self.tax)
    return round(final_price, 2)


def main():
  ui = UserInterface()
  ui.print_menu()

  print()
  print(ui)


# Entry point of the program
main()
