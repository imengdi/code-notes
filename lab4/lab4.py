# Name: Mengdi Zhu
# Lab: Lab4

import random

NUM_OF_TABLE = 5
TABLE_SEATS = 0
TABLE_RESVE = 1

class Restaurant:
  def __init__(self):
    self.__menu = {}
    self.__tables = {}
    self.__orders = {}
    self.__table_num = 0

    # Init the number of seats for each table with a rand number
    # Data structure of tables: [TABLE_SEATS, TABLE_RESVE]
    for table_id in range(1, NUM_OF_TABLE + 1):
      self.__tables[table_id] = [random.randint(1, 10), False]
      self.__table_num += 1


  def add_items(self):
    while True:
      user_enter = input("Enter the item <NAME> and <PRICE>, 'done' to exit: ")
      if user_enter == "done":
        break

      enter_items = user_enter.split()
      if len(enter_items) != 2:
        continue

      try:
        enter_price = float(enter_items[1])
        enter_name = enter_items[0]
      except ValueError:
        continue

      print("Item added to menu!")
      self.__menu[enter_name] = enter_price


  def make_reservation(self):
    # people_num
    pass


  def take_orders(self):
    if len(self.__menu) == 0:
      print("\nNothing to order today ...")
      return

    self.print_menu()
    print("\n*****PLACE your ORDER*****\n")

    while True:
      user_enter = input("Enter the order <NAME> and <NUM>, 'done' to exit: ")
      if user_enter == "done":
        break

      enter_items = user_enter.split()
      if len(enter_items) != 2:
        print("Invalid order input, please enter again ...")
        continue

      try:
        order_num = int(enter_items[1])
        order_name = enter_items[0]
      except ValueError:
        print("Invalid order <NUM>, please enter again ...")
        continue

      if order_name not in self.__menu:
        print("The order <NAME> not in menu, please enter again ...")
        continue

      print("Order placed!")
      if order_name in self.__orders:
        self.__orders[order_name] += order_num
      else:
        self.__orders[order_name] = order_num

    self.print_orders()


  def print_menu(self):
    if len(self.__menu) == 0:
      print("\nNo items in the menu ...")
      return

    print("\n*****MENU to ORDER*****")
    print("\nItem Name\t\tItem Price")
    print("---------\t\t----------")
    for unit_name in self.__menu:
      print("{}\t\t\t{}".format(unit_name, self.__menu[unit_name]))


  def print_reservation(self):
    print("\n*****Available Table List*****")
    print("\nTable NO.\t\tSeats")
    print("---------\t\t-----")

    if self.__table_num == 0:
      print("No available table for reservation!!!\n")
      return

    for table_id in self.__tables:
      if self.__tables[table_id][TABLE_RESVE] is False:
        print("#{}\t\t\t{}".format(table_id, self.__tables[table_id][TABLE_SEATS]))


  def print_orders(self):
    if len(self.__orders) == 0:
      print("\nNo order placed ...")
      return

    print("\n*****YOUR ORDER LIST*****")
    print("\nOrder Items\t\tUnit Price\t\tOrder Num\t\tOrder Price")
    print("-----------\t\t----------\t\t---------\t\t-----------")

    total_price = 0.0
    for unit_name in self.__orders:
      order_num = self.__orders[unit_name]

      # Calc the total price
      unit_price = self.__menu[unit_name]
      order_price = unit_price * order_num
      total_price += order_price

      print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(unit_name, unit_price, order_num, order_price))

    print("\n--------------------")
    print("Total Price: {}\n".format(total_price))


def main():
  r = Restaurant()

  r.add_items()
  r.print_reservation()
  r.take_orders()

  r.make_reservation()
  r.print_reservation()


# Entry point of the program
main()
