class Human():
    def __init__(self, new_name, new_age, new_activities) -> None :
        self.name = new_name
        self.age = new_age
        self.activities = new_activities

        self.friend_list = []
        self.a = 0
        self.b = 0
    
    def presentation(self) :
        sentence = f"""
        Mon nom est {self.name}
        J'ai {self.age} ans
        J'aime bien {self.activities}
        """
        print(sentence)

    def presente_mes_potes(self):
        for pote in self.friend_list:
            pote.presentation()
    
    def sommes_a_b(self) :
        result = self.a + self.b
        print(f"""Hi I am {self.name} and I got {result} tankynes""")

my_first_human = Human("Jaja", 24, ["Oooooooh","manger"])
my_first_human.presentation()

my_second_human = Human("Jiji", 200, ["sport", "rotir du poulet"])
my_second_human.presentation()

my_third_human = Human("Juju", 87, ["sport", "rotir du poulet"])
my_fourth_human = Human("Adel", 4000, ["sport", "rotir du poulet"])
my_fifth_human = Human("Mario", 3, ["sport", "rotir du poulet"])

my_first_human.friend_list.append(my_second_human) #ajouter my_second_human a la list d'amis de my_first_human
my_first_human.friend_list.append(my_third_human) #ajouter my_second_human a la list d'amis de my_first_human
my_first_human.friend_list.append(my_fourth_human) #ajouter my_second_human a la list d'amis de my_first_human
my_first_human.friend_list.append(my_fifth_human) #ajouter my_second_human a la list d'amis de my_first_human

my_first_human.presente_mes_potes()

my_second_human.sommes_a_b()
my_second_human.a = 100
my_second_human.b = 50
my_second_human.sommes_a_b()

my_first_human.sommes_a_b()


