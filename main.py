my_list = [67, 18, 35, 92, 108, 85, 17, 2, 33]

def test_list (my_list : list) :
    even_list = []
    odd_list = []
    zeros = 0

    for i in range (len(my_list)) :
        if my_list[i]%2 == 0 :
            even_list.append(my_list[i])
        elif my_list[i] == 0 : 
            zeros += 1
        else :
            odd_list.append(my_list[i])

    return even_list, odd_list, zeros

#even_list, odd_list, zeros = test_list(my_list)


def pop_vs_remove (my_list : list, nbr : int) :
    print(f"BEFORE.... my_list : {my_list}")
    #pop at the index
    my_list.pop(nbr) #pop the element at index 7
    print(f"AFTER pop({nbr}).... my_list : {my_list}")
    #remove the element
    my_list.remove(nbr) #remove the 7 from the list
    print(f"AFTER remove({nbr}).... my_list : {my_list}")

def find_min_max(my_list : list):
    import math
    current_min = math.inf
    current_max = -math.inf

    min_index = 0
    max_index = 0

    for i in range(len(my_list)) :
        current_value = my_list[i]

        if current_min > current_value :
            current_min = current_value
            min_index = i
        if current_max < current_value :
            current_max = current_value
            max_index = i

    return current_min, current_max, current_value
current_min, current_max, min_index, max_index = find_min_max(my_list)

print(f"""Hehe it seems that:
            -For the given list : {my_list}
            -current_min : {current_min} at index : {min_index}
            -current_max : {current_max} at index : {max_index}
            """)