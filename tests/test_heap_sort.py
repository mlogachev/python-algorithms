from timeit import default_timer as timer
from heap_sort.heap_sort import Heap
import numpy.random as nprnd

test_values = list(nprnd.randint(-1000, 1000, 10000))

# Heap Sort test
## Usage example

values = [3, 2, 4, 1, 5]

sorted_values = Heap(values).sort()
print('Example on HeapSort')
print('Initial values: {}'.format(" ".join([str(i) for i in values])))
print('Sorted Values: {}'.format(" ".join([str(i) for i in sorted_values])))
print('===========', '\n')

## timeit

# print('Testing HeapSort algorithm')
# print('Test on array of length {}'.format(len(test_values)))
# h = Heap(test_values)
# t = timeit.timeit('h.sort()', setup='from __main__ import h')
# print('Total time : {} seconds'.format(t))

print('Testing HeapSort algorithm')
print('Test on array of length {}'.format(len(test_values)))
start = timer()
h = Heap(test_values)
h.sort()
end = timer()
print('Total time : {} seconds'.format(end - start), '\n\n')

