inGame = True
rooms = []
items = []
stage = 0

def stage_0(stage, inGame) :
    sentence = "Vous remarquez une porte entre ouverte, voulez vous entrez ? "
    answer = input(sentence)
    if (answer == "oui") :
        print("""Outch...Il semblerait que vous soyer tomber dans un piège macabre. Votre jambe gauche est brisé .
        C'est à ce moment la que vous sentez une corde proche de vous. """)
        sentence = "Vous la prenez ?? "
        answer = input(sentence)
        if (answer == "oui") :
            print("Eh bien! Courageux le bg! Il est sorti de son trou")
            stage = 1
        else :
            print("Vous avez choisi la mort dans ce trou à rat...Eh bah courage pour la suite")
            inGame = False
    else :
        print("Hehe malin le gamin, tu es sorti sans te blesser mais tu n'auras jamais le fin mot de cette histoire. LACHE !!")
        inGame = False

while inGame :
    if stage == 0:
       stage_0(stage, inGame)
    if stage == 1 : 
        pass