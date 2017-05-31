from merge_sort.merge_sort import merge_sort
from timeit import default_timer as timer
import numpy.random as nprnd

test_values = list(nprnd.randint(-1000, 1000, 10000))

values = [1, 3, 2, 5, 4]
sorted_values = merge_sort(values)

print('Example on Insertions Sort')
print('Initial values: ', values)
print('Sorted Values: ', sorted_values)
print('===========', '\n')

print('Testing Merge Sort algorithm')
print('Test on array of length {}'.format(len(test_values)))
start = timer()
merge_sort(test_values)
end = timer()
print('Total time : {} seconds'.format(end - start), '\n\n')
