def merge_sort(arr, key):
    size = len(arr)

    if size == 1:
        return arr

    left_list = merge_sort(arr[0:size // 2], key)
    right_list = merge_sort(arr[size // 2:], key)
    sorted_list = merge(left_list, right_list, key)

    return sorted_list


def merge(a, b, key):

    merged = []

    while len(a) > 0 and len(b) > 0:
        if a[0][key] >= b[0][key]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))

    while len(a) > 0 and len(b) > 0:
        if a[0][key] <= b[0][key]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))

    merged.extend(a)
    merged.extend(b)
    return merged

if __name__ == "__main__":

    e = [3, 62, 665, 22, 61, 2, 4, 422, 7]

    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]

    sorted_list = merge_sort(elements, key='time_hours')
    print(sorted_list)
