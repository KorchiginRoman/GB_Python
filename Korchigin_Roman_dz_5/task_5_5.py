def get_uniq_numbers(src: list):
    unique_src = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_src.add(el)
        else:
            unique_src.discard(el)
        tmp.add(el)
    #print(unique_src)
    unique_src_ord = [el for el in src if el in unique_src]
    #print(unique_src_ord)
    return [unique_src_ord]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))

#unique_scr = [el for el in src if src.count(el) == 1]
#print(unique_scr)
# print(*get_uniq_numbers(src))
