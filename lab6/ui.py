# Name: Mengdi Zhu
# Lab: Lab6

import sys
import re

from ranking import Ranking


class UI:
  def __init__(self):
    rank_file_name = "not_exist.txt"
    rank_lang_num = 0

    while True:
      self.__rank_obj = Ranking(rank_file_name)
      if self.__rank_obj.is_obj_ready():
        rank_lang_num = self.__rank_obj.get_rank_lang_num()
        break
      rank_file_name = input("Enter a valid input filename: ")
      print()

    # myiter = iter(self.__rank_obj)
    # for i in myiter:
    #   print(i)

    print("Ranking for {} languages from {}\n".format(rank_lang_num, rank_file_name))

    print("r. Languages by ranking")
    print("c. Languages by change")
    print("l. Language info")
    print("q. Quit")



  def run(self):
    print("run the UI")


def main():
  UI().run()


# Entry point of the program
if __name__ == '__main__':
  main()
