import re

def data_reading(file_path):
  try:
    inputfile = open(file_path, "r")
  except IOError as exception:
    print("IO error info: ", str(exception))
  except ValueError as exception:
    print("Value error info: ", str(exception))
  except RuntimeError as exception:
    print("Runtime error info: ", str(exception))

  # Loop through the data in text
  pattern = r"^<tr><td>"
  line_buf = []

  for line in inputfile:
    if re.search(pattern, line):
      line_buf.append(line)

  p1 = r'<tr>(.*?)</tr>'
  p2 = r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>'
  lang_rank = []

  matches = re.findall(p1, line_buf[0])
  for m in matches:
    sub_m = re.findall(r'<td>(.*?)</td>', m)
    lang_rank.append((sub_m[3], sub_m[-1]))

  matches = re.findall(p2, line_buf[1])
  for m in matches:
    lang_rank.append((m[1], None))

  # Close file and return
  inputfile.close()

  return lang_rank


def main():
  res = data_reading("lab6.txt")
  for i in range(len(res)):
    print(i + 1, res[i])


# Entry point of the program
if __name__ == '__main__':
  main()
