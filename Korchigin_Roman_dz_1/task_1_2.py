def sum_list_1(dataset: list) -> int:
    div_on_7 = 0
    for i in range(len(dataset)):
        sum = 0
        elem = dataset[i]
        while elem!=0:
            sum = sum + elem%10
            elem=elem//10
        if sum%7==0:
            div_on_7=div_on_7 + dataset[i]
    return div_on_7
def sum_list_2 (dataset: list) -> int:
    div_on_7_2 = 0
    for i in range(len(dataset)):
        dataset [i] = dataset [i] + 17
    for i in range(len(dataset)):
        sum = 0
        elem = dataset[i]
        while elem!=0:
            sum = sum + elem%10
            elem=elem//10
        if sum%7==0:
            div_on_7_2 = div_on_7_2 + dataset[i]
    return div_on_7_2
my_list = [i**3 for i in range (1, 1001, 2)]
#my_list = [n**3]
#   for n in range (1, 1001, 2):
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)

