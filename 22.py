# count number 4 in a list



def count_number_four(number):
    count = 0
    for num in number:
        if num == 4:
            count += 1
        else:
            count += 0
    return print(count)

count_number_four([1,4,4,4,5,2,6,2,4,5,2,4,7])
