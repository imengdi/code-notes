# Name: Mengdi Zhu
# Lab: Lab6

import re

TABLE_ONE_ITEMS = 6
TABLE_TWO_ITEMS = 3

LANG_NAME = 0
LANG_RATE = 1
LANG_CHGE = 2


class Ranking:
  def __init__(self, file_path="lab6.txt"):
    """Initialize the Ranking object with data from the input file."""
    self.__lang_rank_t1 = []
    self.__lang_rank_t2 = []
    self.__lang_rank_all = []
    self.__lang_rank_by_change = []
    self.__lang_list_dic = None
    self.__lang_rank_len = 0
    self.__iter_idx = 0

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
            self.__lang_rank_t1.append((sub_m[3], float(sub_m[-2].strip('%')), float(sub_m[-1].strip('%'))))
          elif len(sub_m) == TABLE_TWO_ITEMS:
            self.__lang_rank_t2.append((sub_m[1], float(sub_m[2].strip('%')), None))
          else:
            continue

    # Close input file
    input_file.close()

    # Post data processing
    self.__lang_rank_all.extend(self.__lang_rank_t1)
    self.__lang_rank_all.extend(self.__lang_rank_t2)
    self.__lang_rank_len = len(self.__lang_rank_all)
    self.__lang_rank_by_change = sorted(self.__lang_rank_t1, key=lambda item: item[LANG_CHGE], reverse=True)
    self.__lang_list_dic = {rank[LANG_NAME].lower(): rank for rank in self.__lang_rank_all}


  def __iter__(self):
    """Override the iterator, just for fun here."""
    return self


  def __next__(self):
    """Override the next method returns the next data, just for fun here."""
    if self.__iter_idx < self.__lang_rank_len:
      idx = self.__iter_idx
      self.__iter_idx += 1
      return self.__lang_rank_all[idx]
    else:
      self.__iter_idx = 0
      raise StopIteration


  def is_obj_ready(self):
    """Check the initialize status of the Ranking object."""
    if self.__lang_rank_len == 0:
      return False
    return True


  def get_rank_lang_num(self):
    """The length of the data items from the input file."""
    return self.__lang_rank_len


  def lang_ranking_generator(self):
    """Return a generator of languages and ratings, sorted by ranking."""
    return ((rank[LANG_NAME], rank[LANG_RATE]) for rank in self.__lang_rank_all)


  def lang_change_generator(self, direction):
    """Generator method that yields languages, sorted by change for top 20 languages."""
    for rank_info in self.__lang_rank_by_change:
      if direction and rank_info[LANG_CHGE] >= 0 or not direction and rank_info[LANG_CHGE] < 0:
        yield (rank_info[LANG_NAME], rank_info[LANG_CHGE])


  def lang_info_search(self, lang_name):
    """Method that accept one or more languages as input arguments for a search of rank info."""
    if lang_name in self.__lang_list_dic:
      return self.__lang_list_dic[lang_name]
    return None
