class QuickSorter:
    def __init__(self):
        pass

    @staticmethod
    def _swap(lst, i, j):
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp

    def quick_sort_lomuto(self, lst):
        if len(lst) <= 1:
            return lst

        lower, upper = self._partition_lomuto(lst)

        # print(len(lst), len(lower), len(upper))
        return self.quick_sort_lomuto(lower) + self.quick_sort_lomuto(upper)


    def quick_sort_hoare(self, lst):
        if len(lst) <= 1:
            return lst

        low, up = self._partition_hoare(lst)

        return self.quick_sort_hoare(low) + self.quick_sort_hoare(up)

    def quick_sort_fat(self, lst):

        if len(lst) <= 1:
            return lst

        low, up = self._fat_partition(lst)
        # print(low, up)
        # print(lst[:low], lst[up + 1:], lst[low:up + 1])

        return self.quick_sort_fat(lst[:low]) + lst[low:up + 1] + self.quick_sort_fat(lst[up + 1:])

    def _fat_partition(self, lst):
        high = len(lst) - 1
        low = 0

        pivot = lst[round((low + high) / 2)]

        i = low

        while i <= high:
            if lst[i] < pivot:
                self._swap(lst, low, i)
                i += 1
                low += 1
            elif lst[i] > pivot:
                self._swap(lst, high, i)
                high -= 1
            else:
                i += 1

        # print(pivot)
        # print(lst, low, high + 1)
        return low, high



    def _partition_lomuto(self, lst):
        high = len(lst) - 1
        low = 0
        pivot = lst[high]
        i = low - 1

        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                self._swap(lst, j, i)

        self._swap(lst, high, i + 1)

        return lst[:i + 1], lst[i + 1:]

    def _partition_hoare(self, lst):
        high = len(lst) - 1
        low = 0

        pivot = lst[round((low + high) / 2)]

        while True:

            while lst[low] < pivot:
                low += 1

            while lst[high] > pivot:
                high -= 1

            if low >= high:
                return lst[:high + 1], lst[high + 1:]

            self._swap(lst, low, high)
