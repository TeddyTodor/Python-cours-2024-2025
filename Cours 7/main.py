def exo1 () :
    age = 10
    name = "Jojo"
    travail = ["infuenceur", "ingenieur"]

    print(f"""Bonjour je suis {name}
    J'ai {age} ans
    Je suis {travail}
    """)

def exo2 (a, b) :
    add = a + b
    sous = a - b
    mult = a*b
    div = a/b
    div_entiere = a//b
    reste_div = a%b
    puiss = a**b

    sentence = f"""    Resultat :
    Addition : {add}
    Soustraction : {sous}
    Multiplication : {mult}
    Division : {div}
    Division entiere : {div_entiere}
    Reste : {reste_div}
    Puissance : {puiss}"""
    
    print(sentence)

def exo3 () :

    my_list = [10,20,30,40,50,60,70,80,90]
    number_exist = False

    for i in range(len(my_list)) :
        print(f"{i} : {my_list[i]}")
        if my_list[i] == 50 :
            number_exist = True


    index = 0
    while (index<len(my_list)) :
        print(f"{index} : {my_list[index]}")
        if my_list[i] == 50 :
            number_exist = True
            break
        index += 1

    sentence = f"found in index {i}" if number_exist else "bruh, nothing"
    print(sentence)

