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
    try:
      input_file = open(file_name, "r")
    except IOError as exception:
      print("IO error info: ", str(exception))
      return

    # Loop through the rest rest data in text
    for line in input_file:
      line = line.strip()
      items = line.split(',')
      print(items)

    # Close file and return
    input_file.close()

  def __repr__(self):
    return self.__class__.__name__


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
  def __init__(self, name, id_num, price):
    super().__init__(name, id_num, price)
    self.tax = 9.13 / 100
    self.crv = {'S': 0.05, 'L': 0.10}

  def __repr__(self):
    return super().__repr__()


def data_reading(file_path, data_list):
  try:
    inputfile = open(file_path, "r")
  except IOError as exception:
    print("IO error info: ", str(exception))
    return False
  except ValueError as exception:
    print("Value error info: ", str(exception))
    return False
  except RuntimeError as exception:
    print("Runtime error info: ", str(exception))
    return False

  # Loop through the rest rest data in text
  for line in inputfile:
    line = line.strip()
    items = line.split(',')
    data_list.append(items)

  # Close file and return
  inputfile.close()
  return True


def main():
  all_data_list = []
  data_reading("items.csv", all_data_list)

  for d in all_data_list:
    print(d)


# Entry point of the program
# main()

b = Inventory("items.csv")
c = SaleItem("Water", "32", "1.5")
d = HotFood("W", 33, 1.2)
print(b)
print(c)
print(d)

d.print_hello()
