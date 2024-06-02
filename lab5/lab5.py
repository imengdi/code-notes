# Name: Mengdi Zhu
# Lab: Lab5


class UserInterface:
  def __init__(self):
    pass

  def print_menu(self):
    pass

  def read_user_choices(self):
    pass

  def print_receipt(self):
    pass

  def __repr__(self):
    return self.__class__.__name__


class Inventory:
  def __init__(self):
    pass

  def __repr__(self):
    return self.__class__.__name__


class SaleItem:
  def __init__(self):
    pass

  def __repr__(self):
    return self.__class__.__name__


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
main()

b = Inventory()
print(b)
