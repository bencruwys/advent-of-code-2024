import utils

MIN_CHANGE = 1
MAX_CHANGE = 3


def line_is_safe(line):
  comparisson_pairs = [(x, y) for x, y in zip(line, line[1:])]
  differences = [(i - j) for i, j in comparisson_pairs]

  all_decreasing = all(d > 0 for d in differences)
  all_increasing = all(d < 0 for d in differences)

  if all_decreasing or all_increasing:
    if min(differences) >= MIN_CHANGE and max(differences) <= MAX_CHANGE:
      return True
    elif min(differences) >= (-1 * MAX_CHANGE) and max(differences) <= (-1 * MIN_CHANGE):
      return True
    
  return False


# Work out if reports are "safe".
def part1(data):
  total_safe = 0

  for line in data:
    numbers = [int(character) for character in line.split(" ")]

    if line_is_safe(numbers):
      total_safe += 1

  return total_safe


def part2(data):
  total_safe = 0

  for line in data:
    numbers = [int(character) for character in line.split(" ")]

    if line_is_safe(numbers):
      total_safe += 1
    else:
      for index in range(0, len(numbers)):
        short_numbers = numbers[:index] + numbers[index+1:]
        if line_is_safe(short_numbers):
          total_safe += 1
          break
  
  return total_safe
  

data = utils.get_input_lines(day=2)

p1 = part1(data)
p2 = part2(data)

print(p1)
print(p2)
