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


  def add_items(self, item, price):
    self.__menu[item] = price


  def make_reservation(self, people_num):
    pass


  def take_orders(self):
    pass


  def print_menu(self):
    print("\nName\tPrice")
    for i in self.__menu:
      print("{}\t{}".format(i, self.__menu[i]))


  def print_reservation(self):
    print("\nAvailable Table List")
    print("#NO.\tSeats")
    for i in self.__tables:
      if self.__tables[i][1] is False:
        print("{}\t{}".format(i, self.__tables[i][0]))


  def print_orders(self):
    pass


r = Restaurant()
r.add_items("abc", 10)
r.print_menu()
r.print_reservation()
