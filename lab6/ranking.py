# Name: Mengdi Zhu
# Lab: Lab6

import re


def data_reading(file_path):
  try:
    input_file = open(file_path, "r")
  except IOError as exception:
    print("IO error info: ", str(exception))
  except ValueError as exception:
    print("Value error info: ", str(exception))
  except RuntimeError as exception:
    print("Runtime error info: ", str(exception))

  # Loop through the data in text
  lang_rank = []
  outline_pattern = r'<tr>(.*?)</tr>'
  detail_pattern = r'<td>(.*?)</td>'

  for line in input_file:
    if re.search(outline_pattern, line):
      matches = re.findall(outline_pattern, line)
      for m_items in matches:
        sub_m = re.findall(detail_pattern, m_items)
        if len(sub_m) == 6:
          lang_rank.append((sub_m[3], sub_m[-1]))
        elif len(sub_m) == 3:
          lang_rank.append((sub_m[1], None))
        else:
          continue

  # Close file and return
  input_file.close()
  return lang_rank


def main():
  res = data_reading("lab6.txt")
  for i in range(len(res)):
    print(i + 1, res[i])


# Entry point of the program
if __name__ == '__main__':
  main()
