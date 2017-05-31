def merge_sort(it):

    if len(it) == 1:
        return it

    d = round(len(it) / 2)

    l = merge_sort(it[:d])
    r = merge_sort(it[d:])

    srtd = list()
    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            srtd.append(l[i])
            i += 1
        else:
            srtd.append(r[j])
            j += 1

    rest = l[i:] if i < len(l) else r[j:]
    srtd += rest

    return srtd
