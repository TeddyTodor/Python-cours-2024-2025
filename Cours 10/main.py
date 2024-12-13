def exo1 () :  

    for i in range (1, 11) :
        for j in range (i) :
            print(i,end =' ')
        print("")


def exo2 (value_1, value_2) :

    min_value = min(value_1, value_2)

    for i in range (1,min_value) :
        if value_1%i==0 and value_2%i==0 :
            print(i)


def exo3() :   
    names = ["A","B","C","D","E"]
    nbr = [1,2,3]

    for i in range (len(nbr)) :
        for j in range (len(names)) :
            print(f"{nbr[i]}:{names[j]}", end = "   |")
        print("\n"+"_"*50)


names = ["A","B","C","D","E"]
numbers = [1,2,3]
row = ["_"]*len(names)
matrix = []
for i in range(len(names)) :
    matrix.append(row)

for i in range(len(matrix)) :
    for j in range(len(matrix[i])) :
        matrix[i][j] = f"{numbers[i]}:{names[j]}"

    print(matrix[i][j])