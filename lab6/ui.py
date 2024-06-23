# Name: Mengdi Zhu
# Lab: Lab6

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

    print("Ranking for {} languages from {}\n".format(rank_lang_num, rank_file_name))

    self.__task_list = {"r": self.view_lang_by_ranking,
                        "c": self.view_lang_by_change,
                        "l": self.view_lang_info,
                        "q": exit}


  def print_ui_menu(self):
    print("r. Languages by ranking")
    print("c. Languages by change")
    print("l. Language info")
    print("q. Quit")


  def view_lang_by_ranking(self):
    print("Printing one language at a time")
    print("After each language, press Enter to continue, any other key to stop\n")

    rkg = self.__rank_obj.lang_ranking_generator()
    idx = 0
    while True:
      if input() != "":
        print()
        break

      idx += 1
      try:
        rank_info = next(rkg)
      except StopIteration:
        print(" END OF MESSAGE")
        print()
        break

      print(" {} {}\t\t\t{}".format(idx, rank_info[0], rank_info[1]))


  def view_lang_by_change(self):
    while True:
      print("p. Positive change")
      print("n. Negative change")
      user_choice = input("Enter choice: ")
      user_choice = user_choice.lower()
      if user_choice == "p" or user_choice == "1":
        rkg_dir = True
        break

      if user_choice == "n" or user_choice == "2":
        rkg_dir = False
        break

    rkg = self.__rank_obj.lang_change_generator(rkg_dir)
    for rank_info in rkg:
      print("{}\t\t\t{}".format(rank_info[0], rank_info[-1]))
    print()


  def view_lang_info(self):
    while True:
      user_choice = input("Enter language names, separated by comma: ")
      user_choice = user_choice.lower()
      choices = [word.strip() for word in re.split(r',', user_choice) if word.strip()]
      if len(choices) > 0:
        break

    print("  Language            Rank   Change")
    for lang_name in choices:
      res = self.__rank_obj.lang_info_search(lang_name)
      if res is None:
        print("{} not found".format(lang_name))
      else:
        print(res)
    print()


  def run(self):
    while True:
      self.print_ui_menu()
      user_choice = input("Enter choice: ")
      user_choice = user_choice.lower()

      if user_choice not in self.__task_list:
        print("r, c, l, or q only\n")
      else:
        self.__task_list[user_choice]()


# Entry point of the program
if __name__ == '__main__':
  UI().run()
