# Name: Mengdi Zhu
# Lab: Lab6

import re

TABLE_ONE_ITEMS = 6
TABLE_TWO_ITEMS = 3


class Ranking:
  def __init__(self, file_path="lab6.txt"):
    self.__lang_rank_t1 = []
    self.__lang_rank_t2 = []
    self.__lang_rank_all = []

    try:
      input_file = open(file_path, "r")
    except IOError as exception:
      print("IO error info: ", str(exception))
      return
    except ValueError as exception:
      print("Value error info: ", str(exception))
      return
    except RuntimeError as exception:
      print("Runtime error info: ", str(exception))
      return

    # Loop through the data in text
    outline_pattern = r'<tr>(.*?)</tr>'
    detail_pattern = r'<td>(.*?)</td>'

    for line in input_file:
      if re.search(outline_pattern, line):
        matches = re.findall(outline_pattern, line)
        for m_items in matches:
          sub_m = re.findall(detail_pattern, m_items)
          if len(sub_m) == TABLE_ONE_ITEMS:
            self.__lang_rank_t1.append((sub_m[0], sub_m[3], sub_m[-1]))
          elif len(sub_m) == TABLE_TWO_ITEMS:
            self.__lang_rank_t2.append((sub_m[0], sub_m[1], None))
          else:
            continue

    # Close input file
    input_file.close()

    # Post data processing
    self.__lang_rank_all.extend(self.__lang_rank_t1)
    self.__lang_rank_all.extend(self.__lang_rank_t2)


  def print_lang_rank(self):
    for item in self.__lang_rank_all:
      print(item)
