age = 22
#print("salut, mon age c'est" + age)
#print(f"salut, mon age c'est {age}")

#print("salut, mon age c'est " + str(age))
name = "gabi"
#print("salut, mon non c'est %s mon age c'est %d" %(name, age))

age = 14
name = "Théodore"
ecole = "EEB1"
adresse = "Flagey"
couleur = "rouge"
print("""Salut, je m'apelle %s 
j'ai %d ans 
mon école est %s 
j'habite a %s 
et m'as couleur préférer est le %s""" %(name, age, ecole, adresse, couleur))

while (True) :
    name = input("Quelle est ton nom ? ")
    if name == "done" :
        break
    note = input("Quelle est t'as note ? ")
    if note == "done" :
        break
    elif float(note) > 10 :
        print("Les notes sont sur 10")
    elif float(note) >= 9 :
        print("L'éleve %s a eu A" %name)
    elif float(note) >= 8 :
        print("L'éleve %s a eu B" %name)
    elif float(note) >= 7 : 
        print("L'éleve %s a eu C" %name)
    elif float(note) >= 6 :
        print("L'éleve %s a eu D" %name)
    elif float(note) >= 5 :
        print("L'éleve %s a eu E" %name)
    elif float(note) >= 3 :
        print("L'éleve %s a eu F" %name)
    elif float(note) >= 0 :
        print("L'éleve %s a eu Fx" %name)
    else :
        print("La machine n'accepte pas les point négatif")
        break

