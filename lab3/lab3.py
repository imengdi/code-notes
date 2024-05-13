# Name: Mengdi Zhu
# Lab: Lab3

all_data_list = []
country_info_map = {}
population_country_map = {}
area_country_map = {}
population_list = []
area_list = []


def data_reading(file_path):
  try:
    inputfile = open(file_path, "r")
  except:
    return False

  # Bypasss the first line of data in text
  inputfile.readline()

  # Loop through the rest rest data in text
  for line in inputfile:
    items = line.split('\t')
    all_data_list.append(items)

  # Close file and return
  inputfile.close()
  return True


def data_process():
  for items in all_data_list:
    # Get country name as string
    country_name = items[0]
    country_name_query = country_name.lower()

    # Cast population and area as int
    try:
      country_population = int(items[1])
      country_area = int(items[5])
    except:
      return False

    # Map of country name to packed info
    country_info_map[country_name_query] = (country_name, country_population, country_area)

    # Map of population data to country
    if country_population in population_country_map:
      population_country_map[country_population].append(country_name)
    else:
      population_country_map[country_population] = [country_name]

    # Map of area data to country
    if country_area in area_country_map:
      area_country_map[country_area].append(country_name)
    else:
      area_country_map[country_area] = [country_name]

    # List of population data
    if country_population not in population_list:
      population_list.append(country_population)

    # List of area data
    if country_area not in area_list:
      area_list.append(country_area)

  # Sort population and area list in reverse order
  population_list.sort(reverse=True)
  area_list.sort(reverse=True)

  return True


def info_query_start():
  info_mode_query = ""
  while info_mode_query != "country" and info_mode_query != "ranking":
    info_mode = input("Do you want to see info based on a country or ranking?\n")
    info_mode_query = info_mode.lower()

  if info_mode_query == "country":
    run_country_query()

  else:
    run_ranking_query()


def run_country_query():
  country_name_query = ""
  while country_name_query not in country_info_map:
    country_name = input("Which country do you want to see?\n")
    country_name_query = country_name.lower()

  info_pack = country_info_map[country_name_query]
  the_name = info_pack[0]
  the_population = info_pack[1]
  the_area = info_pack[2]

  # Print out the query info of country population and area
  print("The {} has population {} and land area {} sq km.".format(the_name, the_population, the_area))


def run_ranking_query():
  rank_base_query = ""
  while rank_base_query != "population" and rank_base_query != "land area":
    rank_base = input("Do you want to see the associated country based on population or land area rank?\n")
    rank_base_query = rank_base.lower()

  rank_num = -1
  if rank_base_query == "population":
    while rank_num < 1 or rank_num > len(population_list):
      try:
        rank_num = int(input("What ranking country do you want to see based on {}?\n".format(rank_base_query)))
      except:
        continue

    the_key = population_list[rank_num - 1]
    the_value = population_country_map[the_key]

  else:
    while rank_num < 1 or rank_num > len(area_list):
      try:
        rank_num = int(input("What ranking country do you want to see based on {}?\n".format(rank_base_query)))
      except:
        continue

    the_key = area_list[rank_num - 1]
    the_value = area_country_map[the_key]

  # Print out the query info of ranking
  show_ranking_info(rank_num, rank_base_query, the_value)


def show_ranking_info(rank_num, rank_base, country_list):
  print("The country ranking # {} by {} is ".format(rank_num, rank_base), end='')
  # Print countries if that rank has multiple entries
  for country in country_list:
    print(country, end=' ')
  # Print a newline at the end of the info display
  print()


def main():
  if not data_reading("population_by_country_2020.txt"):
    print("Error in data file reading ...")
    return

  if not data_process():
    print("Error in data file processing ...")
    return

  info_query_start()


# Entry point of the program
main()
