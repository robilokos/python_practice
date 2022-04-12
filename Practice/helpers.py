def sum_of_two_int(a, b):
    return a + b

def for_loop_on_list(my_list):
    for i in my_list:
        print(f"{i}")

def while_loop_on_list(my_list):
    counter = 0
    while counter < len(my_list):
        print(my_list[counter])
        counter+=1

def fill_up_list_with_numbers_from_one_to_five():
    my_list = []
    #range(from, to - 1, steps)
    for i in range(1,6):
        my_list.append(i)
        print(i)
    return my_list

def for_loop_on_dict(my_dict):
    for key, value in my_dict.items():
        print(f"{key}: {value}")

def search_in_list(my_list, element):
    if element in my_list:
        print("The element is in the list!")
    else:
        print("The element is not in the list!")

def search_in_dict(my_dict, element):
    if element in my_dict.keys():
        print("The element is in the keys!")
    else:
        if element in my_dict.values():
            print("The element is in the values!")
        else:
            print("The element is not in the dict!")

if __name__ == '__main__':
    print("sum of two number\n")
    sum = sum_of_two_int(2, 4)
    print(f"{sum}\n")

    my_list = [1,2,3,4,5,6]
    my_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6
    }

    print("for loop on list\n")
    for_loop_on_list(my_list)
    print()

    print("while loop on list\n")
    while_loop_on_list(my_list)
    print()

    print("fill up list with numbers from one to ten\n")
    my_list2 = fill_up_list_with_numbers_from_one_to_five()
    print()

    print("for loop on dict\n")
    for_loop_on_dict(my_dict)
    print()

    print("search in list\n")
    search_in_list(my_list, 3)
    print()

    print("search in list\n")
    search_in_list(my_list, 10)
    print()

    print("search in dict\n")
    search_in_dict(my_dict, 'c')
    print()

    print("search in dict\n")
    search_in_dict(my_dict, 4)
    print()

    print("search in dict\n")
    search_in_dict(my_dict, "nope")