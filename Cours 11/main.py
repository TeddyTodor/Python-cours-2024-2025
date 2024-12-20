current_list = [2,4,3,1]

def simple_sort_algo(my_list : list) :
    print(my_list)
    print("Init")

    for i in range (0,len(my_list)-1) :
        for j in range (i+1,len(my_list)) :
            if my_list[j] < my_list[i] :
                my_list[j], my_list[i] = my_list[i], my_list[j]
                print(my_list)
        print("Changement de challenger")

simple_sort_algo(my_list=current_list)