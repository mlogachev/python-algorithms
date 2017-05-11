import timeit

from heap_sort.heap_sort import Heap
from tests.arr import test_values

# Heap Sort test
## Usage example

values = [3, 2, 4, 1, 5]

sorted_values = Heap(values).sort()
print('Example on HeapSort')
print('Initial values: {}'.format(" ".join([str(i) for i in values])))
print('Sorted Values: {}'.format(" ".join([str(i) for i in sorted_values])))
print('===========', '\n')

## timeit

print('Testing HeapSort algorithm')
print('Test on array of lenght {}'.format(len(test_values)))
h = Heap(test_values)
t = timeit.timeit('h.sort()', setup='from __main__ import h')
print('Total time : {} seconds'.format(t))

