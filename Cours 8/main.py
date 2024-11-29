def exo1 (a : int, b : int) :
    add = a+b
    sous = a-b
    diviEnt = a//b
    divi = a/b
    reste = a%b
    mult = a*b
    puiss = a**b
    shift_right = a>>b
    shift_left = a<<b

    sentence = f"""    
    Resultat avec a = {a} et b = {b}
    Addition : {add}
    Soustraction : {sous}
    Division entiere : {diviEnt}
    Division : {divi}
    Reste : {reste}
    Multiplication : {mult}
    Puissance : {puiss}
    Shift right : {shift_right}
    Shift left : {shift_left}
    """
    print(sentence)

def exo2 () :
    my_list = [10,20,30,40,50,60,70,80,90]

    for index in range (len(my_list)) : 
        print(f"{index} : {my_list[index]}")

    for element in my_list : 
        print(element)

    for index,element in enumerate(my_list) : 
        print(f"Pour l'indice {index}, voicis l'element correspondant {element}")

exo2()