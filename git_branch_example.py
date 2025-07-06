<<<<<<< HEAD
import math
def median (input_list):
  sorted_list = sorted(input_list)
  n = len(sorted_list)
  if n %2 == 1:
    return sorted_list[n//2]
  else:
    mid1 = sorted_list[n//2-1]
    mid2 = sorted_list[n//2]
    return (mid1 + mid2)/2

print(median(my_list))
