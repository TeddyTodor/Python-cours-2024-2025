name = "Teddy"
age = 19
job = ["ingenieur", "informaticien"]

def math () : 
    a = 4
    b = 5

    sum = a+b
    sous = a-b
    mult = a*b
    divi = a/b
    divi_rest = a%b
    puiss = a**b

    print(f"""  Addition : {sum}
    Soustraction : {sous}
    Multiplication : {mult}
    Division : {divi}
    Reste : {divi_rest}
    Puissance : {puiss}""") 
math()


print (f"""Bonjour,
Je m'apelle {name}
J' ai {age} ans
Je suis un {job[0]} et un {job[1]}""")


my_list = [1,2,3,4,5,6,7,8,9]
my_list_lenght = len(my_list) #longueur de la liste

for i in range(0, my_list_lenght, 1) :
    print(f"{i} : {my_list[i]}")


target_value = 3
for i in range(len(my_list)) :
    if (my_list[i] == target_value) :
        print("Yes, la valeur %d est bien dans la liste" %(target_value))