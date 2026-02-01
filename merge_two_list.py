def merge_two_list(ls1, ls2):
    merged = []
    i, j = 0, 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            merged.append(ls1[i])
            i+=1
        else:
            merged.append(ls2[j])
            j+=1
    merged+=ls1[i:]
    merged+=ls2[j:]
    return merged


print(merge_two_list(["bread", "bread", "milk"], ["milk", "milk"]))
