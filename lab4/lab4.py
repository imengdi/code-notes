# Name: Mengdi Zhu
# Lab: Lab4

import random

NUM_OF_TABLE = 5
MAX_TABLE_SEATS = 10
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
      self.__tables[table_id] = [random.randint(1, MAX_TABLE_SEATS), False]
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
    if self.__table_num == 0:
      print("\nNo table left for reservation ...")
      return

    self.print_reservation()
    print("\n*****START your RESERVATION*****\n")

    while True:
      if self.__table_num == 0:
        print("Exit, since no table left for reservation ...")
        break

      user_enter = input("The <NUM> of people come to restaurant, 'done' to exit: ")
      if user_enter == "done":
        break

      try:
        people_num = int(user_enter)
      except ValueError:
        print("Invalid people <NUM>, please enter again ...")
        continue

      opt_table_id = -1
      opt_seats = MAX_TABLE_SEATS + 1

      for table_id in self.__tables:
        table_status = self.__tables[table_id][TABLE_RESVE]
        table_seats = self.__tables[table_id][TABLE_SEATS]

        if table_status is False and table_seats >= people_num:
          # Check if the minimum table seat can match the people number
          if opt_seats > table_seats:
            opt_table_id = table_id
            opt_seats = table_seats

      if opt_table_id != -1:
        self.__tables[opt_table_id][TABLE_RESVE] = True
        self.__table_num -= 1
        print("Reservation success!!!")

        self.print_reservation()
        print()
      else:
        print("No table to reserve for {} people ...".format(people_num))


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
  r.take_orders()
  r.make_reservation()


# Entry point of the program
main()
