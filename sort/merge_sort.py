def merge(arr, lf, mid, rg):
    res = []
    left = lf
    right = mid
    while left < mid and right < rg:
        if arr[left] <= arr[right]:
            res.append(arr[left])
            left += 1
        else:
            res.append(arr[right])
            right += 1
    res += arr[left:mid] + arr[right:rg]
    arr[lf:rg] = res
    return arr


def merge_sort(arr, lf, rg):
    if rg - lf == 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


test()
