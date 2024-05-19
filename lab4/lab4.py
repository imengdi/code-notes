# Name: Mengdi Zhu
# Lab: Lab4

import random


NUM_OF_TABLE = 20

class Restaurant:
  def __init__(self):
    self.__menu = {}
    self.__tables = {}
    for i in range(1, NUM_OF_TABLE + 1):
      self.__tables[i] = (random.randint(1, 10), False)


  def add_items(self):
    user_enter = ""
    while user_enter != "done":
      user_enter = input("Enter the item <NAME> and <PRICE>, 'done' to exit: ")
      enter_items = user_enter.split()

      if len(enter_items) != 2:
        continue

      try:
        enter_price = float(enter_items[1])
        enter_name = enter_items[0]
      except ValueError:
        continue

      self.__menu[enter_name] = enter_price


  def make_reservation(self, people_num):
    pass


  def take_orders(self):
    pass


  def print_menu(self):
    if len(self.__menu) == 0:
      print("\nNo items in the menu ...")
      return

    print("\nItem Name\t\tItem Price")
    print("---------\t\t----------")
    for i in self.__menu:
      print("{}\t\t\t{}".format(i, self.__menu[i]))


  def print_reservation(self):
    print("\nAvailable Table List")
    print("#NO.\tSeats")
    for i in self.__tables:
      if self.__tables[i][1] is False:
        print("{}\t{}".format(i, self.__tables[i][0]))


  def print_orders(self):
    pass


r = Restaurant()
r.add_items()
r.print_menu()
# r.print_reservation()
