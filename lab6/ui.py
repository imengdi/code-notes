# Name: Mengdi Zhu
# Lab: Lab6

import sys
import re

from ranking import Ranking


class UI:
  def __init__(self):
    self.__rank_obj = Ranking()
    self.__rank_obj.print_lang_rank()

  def run(self):
    print("run the UI")


def main():
  UI().run()


# Entry point of the program
if __name__ == '__main__':
  main()
