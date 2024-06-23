# Name: Mengdi Zhu
# Lab: Lab6

import re

from ranking import Ranking


class UI:
  def __init__(self):
    self.__task_list = {"r": self.view_lang_by_ranking,
                        "c": self.view_lang_by_change,
                        "l": self.view_lang_info,
                        "q": exit}

    rank_file_name = "lab6.txt"
    while True:
      self.__rank_obj = Ranking(rank_file_name)
      if self.__rank_obj.is_obj_ready():
        rank_lang_num = self.__rank_obj.get_rank_lang_num()
        break
      rank_file_name = input("Enter a valid input filename: ")
      print()

    print("Ranking for {} languages from {}\n".format(rank_lang_num, rank_file_name))


  def view_lang_by_ranking(self):
    print("Printing one language at a time")
    print("After each language, press Enter to continue, any other key to stop\n")

    for count, rank_info in enumerate(self.__rank_obj.lang_ranking_generator()):
      print(" {} {}\t\t\t{}".format(count + 1, rank_info[0], rank_info[1]))
      if input() != "":
        print()
        break
    else:
      print(" ---END OF MESSAGE---")
      print()


  def view_lang_by_change(self):
    while True:
      print("p. Positive change")
      print("n. Negative change")
      user_choice = input("Enter choice: ")
      user_choice = user_choice.lower()
      if user_choice == "p" or user_choice == "1":
        direction = True
        break

      if user_choice == "n" or user_choice == "2":
        direction = False
        break

    for rank_info in self.__rank_obj.lang_change_generator(direction):
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
      print("r. Languages by ranking")
      print("c. Languages by change")
      print("l. Language info")
      print("q. Quit")
      user_choice = input("Enter choice: ")
      user_choice = user_choice.lower()

      if user_choice not in self.__task_list:
        print("r, c, l, or q only\n")
      else:
        self.__task_list[user_choice]()


# Entry point of the program
if __name__ == '__main__':
  UI().run()
