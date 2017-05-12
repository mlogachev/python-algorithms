def insertions_sort(to_sort):

    it = to_sort[:]

    for i in range(1, len(it)):
        key = it[i]

        j = i - 1

        while j >= 0 and key < it[j]:
            it[j + 1] = it[j]
            j -= 1

        it[j + 1] = key

    return it