from timeit import default_timer as timer
from tests.arr import test_values
from insertions_sort.insertions_sort import insertions_sort

values = [3, 2, 4, 1, 5]

sorted_values = insertions_sort(values)

print('Example on Insertions Sort')
print('Initial values: ', values)
print('Sorted Values: ', sorted_values)
print('===========', '\n')

print('Testing Insertions Sort algorithm')
print('Test on array of length {}'.format(len(test_values)))
start = timer()
insertions_sort(test_values)
end = timer()
print('Total time : {} seconds'.format(end - start))