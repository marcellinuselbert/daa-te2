import json
import time
import tracemalloc

def partition_values_from_index(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err):
    # If start_index is beyond the end of the array,
    # then all entries have been assigned.
    if start_index >= len(values):
        # We're done. See if this assignment is better than
        # what we have so far.
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            # This is an improvement. Save it.
            best_err[0] = test_err
            best_assignment.clear()
            best_assignment.extend(test_assignment)

            # print(best_err[0])
    else:
        # See if there's any way we can assign
        # the remaining items to improve the solution.
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            # There's a chance we can make an improvement.
            # We will now assign the next item.
            unassigned_value -= values[start_index]

            # Try adding values[start_index] to set 1.
            test_assignment[start_index] = True
            partition_values_from_index(values, start_index + 1,
                                        total_value, unassigned_value,
                                        test_assignment, test_value + values[start_index],
                                        best_assignment, best_err)

            # Try adding values[start_index] to set 2.
            test_assignment[start_index] = False
            partition_values_from_index(values, start_index + 1,
                                        total_value, unassigned_value,
                                        test_assignment, test_value,
                                        best_assignment, best_err)





# Read lists from text files
with open('random_list_10.txt', 'r') as file:
    list_10 = json.loads(file.read())

with open('random_list_40.txt', 'r') as file:
    list_40 = json.loads(file.read())

with open('random_list_80.txt', 'r') as file:
    list_80 = json.loads(file.read())

for lst in [list_10,list_40,list_80]:
  start_time = time.time()

# Example usage:
  values = lst
  start_index = 0
  total_value = sum(values)
  unassigned_value = total_value
  test_assignment = [False] * len(values)
  test_value = 0
  best_assignment = [False] * len(values)
  best_err = [float('inf')]  
  tracemalloc.start()  
  partition_values_from_index(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err)
  end_time = time.time()
  current, peak = tracemalloc.get_traced_memory()
  tracemalloc.clear_traces()

  print(f"Peak memory usage: {peak / 10**6} MB")
  print(f"Time taken with dataset list_{len(lst)}: {(end_time - start_time) * 1000} ms")
