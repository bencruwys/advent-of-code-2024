import bisect
from pathlib import Path


def get_input(day, remove_start_whitespace=False):
  day_string = "{:02}".format(day)
  filepath_string = f"inputs/day{day_string}.txt"

  path = Path(filepath_string)
  
  with open(path, "r") as file:
    raw_file_text = file.read()
    if remove_start_whitespace:
      raw_file_text = raw_file_text.strip()
  
  return [x for x in raw_file_text.splitlines() if x]


# Splits input line by line by a delimiter and return two sorted lists.
def split_input_and_sort(data, delimiter=" "):
  left_list, right_list = [], []
  
  for line in data:
    left_num, right_num = line.split(delimiter)
    
    # Insert each value, keeping the list in order.
    left_insertion_point = bisect.bisect_left(left_list, left_num)
    left_list.insert(left_insertion_point, left_num)
    
    right_insertion_point = bisect.bisect_left(right_list, right_num)
    right_list.insert(right_insertion_point, right_num)

  return left_list, right_list