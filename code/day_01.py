import bisect
import utils


# Calculate difference between each set of values.
def part1(left, right):
  total_difference = 0
  
  if len(left) != len(right):
    raise ValueError("Lists are different lengths.")

  for l, r in zip(left, right):
    difference = abs(int(l)-int(r))
    total_difference += difference

  return total_difference


def part2(left, right):
  similarity_score = 0

  for value in left:
    counter = right.count(value)
    similarity_score += (counter * int(value))

  return similarity_score


data = utils.get_input(1)
left, right = utils.split_input_and_sort(data, "   ")

p1 = part1(left, right)
p2 = part2(left, right)

print(f"Day 1 Part 1: {p1}")
print(f"Day 1 Part 2: {p2}")