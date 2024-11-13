number = 1
#while True :
    #print(number)
    #number += 1

number_2 = 1
sum = 0
while number_2 < 11 :
    print(number_2)
    sum += number_2
    number_2 += 1
print(sum)

num = 78456
count = 0
while num !=  0:
    num //= 10
    count += 1
print(f"Nombre de chiffre : {count}")

num = 42
guessnum = int(input("How many guesses should you have ?\n"))
guess = 0
while guessnum > 0 and guess != num :
    guess = int(input("Take a guess \n"))
    if guess < num :
        print ("Bigger")
    elif guess > num :
        print ("Smaller")
    guessnum -= 1
    print(f"You have {guessnum} chances left.")
if guess == num :
    print("You win")
else :
    print("You lose")

num = 0
num2 = 1
i = 0
while i < 100 :
    print (num)
    temp = num + num2
    num = num2
    num2 = temp
    i += 1