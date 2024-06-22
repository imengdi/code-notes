# Name: Mengdi Zhu
# Lab: Lab6

import sys
import re

from ranking import Ranking


class UI:
  def __init__(self):
    rank_file_name = "lab6.txt"
    rank_lang_num = 0

    while True:
      self.__rank_obj = Ranking(rank_file_name)
      if self.__rank_obj.is_obj_ready():
        rank_lang_num = self.__rank_obj.get_rank_lang_num()
        break
      rank_file_name = input("Enter a valid input filename: ")
      print()

    myiter = iter(self.__rank_obj)
    for i in myiter:
      print(i)

    print("Ranking for {} languages from {}\n".format(rank_lang_num, rank_file_name))


  def print_ui_menu(self):
    print("r. Languages by ranking")
    print("c. Languages by change")
    print("l. Language info")
    print("q. Quit")


  def view_lang_by_ranking(self):
    print("Printing one language at a time")
    print("After each language, press Enter to continue, any other key to stop\n")


  def view_lang_by_change(self):
    pass


  def view_lang_info(self):
    pass


  def run(self):
    while True:
      self.print_ui_menu()
      user_choice = input("Enter choice: ")
      user_choice = user_choice.lower()

      if user_choice == "q":
        break

      elif user_choice == "r":
        self.view_lang_by_ranking()

      elif user_choice == "c":
        self.view_lang_by_change()

      elif user_choice == "l":
        self.view_lang_info()

      else:
        print("r, c, l, or q only\n")


# Entry point of the program
if __name__ == '__main__':
  UI().run()
