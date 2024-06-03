# Name: Mengdi Zhu
# Lab: Lab5

import sys
import re


class UserInterface:
  def __init__(self):
    # Create an Inventory object
    self.inst = Inventory("items.csv")

    if not self.inst.get_inventory_status():
      # End the program if the input file can not be opened
      print("Program end ...")
      sys.exit(1)
    else:
      # Print an instant of the Inventory object
      print(self.inst)

  def __repr__(self):
    return self.__class__.__name__

  def print_menu(self):
    self.inst.get_inventory_details()


class UserInterfaceFinal(UserInterface):
  def __init__(self):
    super().__init__()

  def print_menu(self):
    # Set fmt variable to True for fine printing
    self.inst.get_inventory_details(True)
    # super().print_menu()
    # print(self.inst)
    # print(self.inst.__repr__())

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

  def get_inventory_details(self, fmt=False):
    idx = 0
    line_width = 24
    fixed_width = 8
    float_width = line_width - fixed_width

    for item_header in self.__inventory_dic:
      # Show a header for each food / drink type
      if fmt:
        indent_space = (line_width - len(item_header)) // 2 - 1
        print(" " * indent_space + item_header)
      else:
        print(item_header)

      for item_obj in self.__inventory_dic[item_header]:
        # Print each item to see that the format of __repr__ of each item
        if fmt:
          idx += 1
          (item_name, item_price) = self.get_match_pattern(item_obj.__repr__())
          if item_name is None or item_price is None:
            continue
          indent_space = float_width - len(item_name) - 1
          print(idx, item_name + " " * indent_space, "$", "%.2f" % float(item_price))
        else:
          print(item_obj)

        # For item that has tax and CRV, print the final price of the item
        if not fmt:
          item_final_price = item_obj.get_final_price()
          if item_final_price != item_obj.get_item_price():
            print(item_final_price)

  def get_match_pattern(self, repr_str):
    pattern = r"(\w+\s*\w*)\(\d+\):(\d+\.\d+)"
    match_res = re.search(pattern, repr_str)

    if match_res:
      return (match_res.group(1), match_res.group(2))
    else:
      return (None, None)


class SaleItem:
  def __init__(self, name, id_num, price):
    self.name = name
    self.id_num = id_num
    self.price = price

  def __repr__(self):
    return "{}({}):{}".format(self.name, self.id_num, self.price)

  def get_item_price(self):
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
  # ui = UserInterface()
  # ui.print_menu()

  # print()
  # print(ui)

  final_ui = UserInterfaceFinal()
  final_ui.print_menu()
  print()
  print(final_ui)


# Entry point of the program
main()
