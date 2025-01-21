def find_number (list, number):
    low = 0
    high = len(list)-1
    middle = 0

    while low <= high:
        middle = (high +low) // 2
        if list[middle] < number:
            low = middle + 1
        elif list[middle] > number:
            high = middle - 1
        else:
            return middle


    return -1

list_for_search = [4,9,1,6,2,8,15,48,54,7]
number_for_searching = 15
result = find_number(list_for_search, number_for_searching)

if result != -1:
    i = str(result)
    y = int(i)
    x = list_for_search[y]
    print ("индекс искомого числа =", i, "и число:", x)
else:
    print("Искомого числа нет в данном списке")
