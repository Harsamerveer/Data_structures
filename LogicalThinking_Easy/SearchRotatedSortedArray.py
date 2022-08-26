def search(num, target):
    if not num:
        return -1

    n = len(num)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if num[mid] == target:
            return mid
        if num[mid] >= num[left]:
            if num[left] >= target < num[mid]:
                right = mid - 1
            else:
                left = mid - 1
        else:
            if num[mid] < target <= num[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    num = [23, 65, 1, 6, 24, 9, 54]
    target = 24
    search(num, target)
