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
    # Use the defualt for raw fmt printing
    self.inst.get_inventory_details()


class UserInterfaceFinal(UserInterface):
  def __init__(self):
    super().__init__()

  def print_menu(self):
    # Set fmt variable to True for fine printing
    self.inst.get_inventory_details(True)

  def read_user_choices(self):
    while True:
      user_in = input("\nEnter your choice numbers: ")
      choices = re.findall(r"[-]{0,1}\d+", user_in)
      self.print_receipt(choices)
      print()

      while True:
        buy_more = input("Buy more? y/n: ")
        if buy_more.lower() == "n" or buy_more.lower() == "y":
          break

      # Exit order loop is input is N or n
      if buy_more.lower() == "n":
        break

      # Let user buy more food or drink
      print()
      self.print_menu()

  def print_receipt(self, choices):
    if len(choices) > 0:
      self.inst.get_order_receipt(choices)


class Inventory:
  # Varible for print line in better format
  __layout_width = 24
  __fixed_width = 8

  def __init__(self, file_name):
    self.__inventory_valid = True
    self.__inventory_dic = {}
    self.__inventory_summary = None
    self.__inventory_order_list = {}

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
    # Init order list with menu choice 1 to 8
    self.init_order_list()

  def __repr__(self):
    if self.__inventory_summary is None:
      self.__inventory_summary = self.init_inventory_summary()
    return self.__inventory_summary

  def init_inventory_summary(self):
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

  def init_order_list(self):
    menu_choice = 0
    for item_header in self.__inventory_dic:
      for item_obj in self.__inventory_dic[item_header]:
        menu_choice += 1
        self.__inventory_order_list[str(menu_choice)] = item_obj

  def get_inventory_status(self):
    return self.__inventory_valid

  def get_inventory_details(self, fmt=False):
    menu_choice = 0
    for item_header in self.__inventory_dic:
      # Show a header for each food / drink type
      if fmt:
        # Print with better format
        self.fine_print_header(item_header)
      else:
        print(item_header)

      for item_obj in self.__inventory_dic[item_header]:
        # Print each item to see that the format of __repr__ of each item
        if fmt:
          menu_choice += 1
          # Name and Price extracted from the __repr__ string of the object
          (item_name, item_price) = self.get_match_pattern(item_obj.__repr__())
          # Check if regular express match successfully
          if item_name is None or item_price is None:
            continue
          # Print with better format
          self.fine_print_item(menu_choice, item_name, item_price)
        else:
          print(item_obj)

        # For item that has tax and CRV, print the final price of the item
        if not fmt:
          item_final_price = item_obj.get_final_price()
          if item_final_price != item_obj.get_item_price():
            print(item_final_price)

  def get_order_receipt(self, choices):
    total_price = 0.0
    invalid_choice = []

    for c in choices:
      if c not in self.__inventory_order_list:
        invalid_choice.append(c)
      else:
        item_obj = self.__inventory_order_list[c]
        final_price = item_obj.get_final_price()
        total_price += final_price
        self.fine_print_item(c + ".", item_obj.get_item_name(), final_price)

    if total_price > 0.0:
      print("Total:", "$", "%.2f" % float(total_price))

    if len(invalid_choice) > 0:
      self.fine_print_invalid(invalid_choice)

  def get_match_pattern(self, repr_str):
    pattern = r"(\w+\s*\w*)\(\d+\):(\d+\.\d+)"
    match_res = re.search(pattern, repr_str)

    if match_res:
      return (match_res.group(1), match_res.group(2))
    else:
      return (None, None)

  def fine_print_header(self, item_header):
    indent_space = (Inventory.__layout_width - len(item_header)) // 2 - 1
    print(" " * indent_space + item_header)

  def fine_print_item(self, menu_choice, item_name, item_price):
    float_width = Inventory.__layout_width - Inventory.__fixed_width
    indent_space = float_width - len(item_name) - 1
    print(menu_choice, item_name + " " * indent_space, "$", "%.2f" % float(item_price))

  def fine_print_invalid(self, invalid_list):
    last_idx = len(invalid_list) - 1

    # Print the start words
    print("Invalid choice: ", end='')
    # Print the middle itmes with pattern "var, var, ..."
    for i in range(last_idx):
      print(invalid_list[i] + ", ", end='')
    # Print the last item of the list
    print(invalid_list[last_idx])


class SaleItem:
  def __init__(self, name, id_num, price):
    self._name = name
    self._id_num = id_num
    self._price = price

  def __repr__(self):
    return "{}({}):{}".format(self._name, self._id_num, self._price)

  def get_item_name(self):
    return self._name

  def get_item_id(self):
    return self._id_num

  def get_item_price(self):
    return self._price


class PackagedFood(SaleItem):
  def __init__(self, name, id_num, price):
    super().__init__(name, id_num, price)

  def __repr__(self):
    return super().__repr__()

  def get_final_price(self):
    return self._price


class HotFood(SaleItem):
  _tax_rate = 9.13 / 100

  def __init__(self, name, id_num, price):
    super().__init__(name, id_num, price)

  def __repr__(self):
    return super().__repr__() + " - heated"

  def get_final_price(self):
    final_price = self._price * (1 + HotFood._tax_rate)
    return round(final_price, 2)


class Drink(SaleItem):
  _tax_rate = 9.13 / 100
  _crv_fee = {'S': 0.05, 'L': 0.10}

  def __init__(self, name, id_num, price, size):
    super().__init__(name, id_num, price)
    self._size = size

  def __repr__(self):
    return super().__repr__()

  def get_final_price(self):
    final_price = (self._price + Drink._crv_fee[self._size]) * (1 + Drink._tax_rate)
    return round(final_price, 2)


def main():
  ui_v1 = UserInterface()
  ui_v1.print_menu()
  print()

  ui_final = UserInterfaceFinal()
  ui_final.print_menu()
  ui_final.read_user_choices()


# Entry point of the program
main()
