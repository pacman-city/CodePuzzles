def merge(list1, list2):  # объединить 2 отсортированных массива

    first, second = list1[:], list2[:]  # копируем списки и выдираем из них по элементу
    result = []

    while first and second:  # если один список закончился(and) - то всторой просто добавить(extend)
        if first[0] <= second[0]:
            item = first.pop(0)
        else:
            item = second.pop(0)
        result.append(item)  # добавляем меньший к result

    result.extend(first if first else second)
    return result


def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(
            list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


if __name__ == '__main__':
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [1, 2, 3, 4, 5]

    result = merge(list_1, list_2)
    print(result)

    result_1 = quick_merge(list_1, list_2)
    print(result_1)
