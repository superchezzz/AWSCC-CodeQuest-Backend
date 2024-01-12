
import math
import os
import random
import re
import sys


def avg(numbers):
  return sum(numbers) / len(numbers)

while True:
  user_input = input("")
  try:
    nums = list(map(int, user_input.split()))
    break
  except ValueError:
    print("Invalid input, please enter numbers separated by spaces")


result = avg(nums)
print(result)