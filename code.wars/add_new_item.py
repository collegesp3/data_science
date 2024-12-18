def add_extra(list_of_numbers):
    newList = list_of_numbers
    newList.append(42)
    return list_of_numbers

print(len(add_extra([78])))