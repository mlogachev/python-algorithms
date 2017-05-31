from quick_sort.quick_sort import QuickSorter
from timeit import default_timer as timer
import numpy.random as nprnd

test_values_1 = list(nprnd.randint(-1000, 1000, 10000))
test_values_2 = list(nprnd.randint(-1000, 1000, 10000))
test_values_3 = list(nprnd.randint(-1000, 1000, 10000))


print('QuickSort with Lomuto Partition')
a = QuickSorter().quick_sort_lomuto([4, 3, 6, 1, 4, 5])
print('>>>>', a)

print('Starting on array of length :{}'.format(len(test_values_1)))
start = timer()
q = QuickSorter().quick_sort_lomuto(test_values_1)
end = timer()
print("Lomuto partition took :{}".format(end - start), '\n\n')

print('QuickSort with fat partition')
print('Starting on array of length :{}'.format(len(test_values_2)))
start = timer()
r = QuickSorter().quick_sort_fat(test_values_2)
end = timer()
print("Fat partition took :{}".format(end - start), '\n\n')


a = QuickSorter().quick_sort_hoare([1, 6, 2, 5, 3])
print('>>>>', a)

print('QuickSort with Hoare partition')
print('Starting on array of length :{}'.format(len(test_values_3)))
start = timer()
p = QuickSorter().quick_sort_hoare(test_values_3)
end = timer()
print("Hoare partitions took :{}".format(end - start), '\n\n')

