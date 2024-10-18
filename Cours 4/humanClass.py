class Human():
    def __init__(self, new_name, new_age, new_activities) -> None :
        self.name = new_name
        self.age = new_age
        self.activities = new_activities

        self.friend_list = []
    
    def presentation(self) :
        sentence = f"""
        Mon nom est {self.name}
        J'ai {self.age} ans
        J'aime bien {self.activities}
        """
        print(sentence)

my_first_human = Human("Jaja", 24, ["Oooooooh","manger"])
my_first_human.presentation()

my_second_human = Human("Jiji", 200, ["sport", "rotir du poulet"])
my_second_human.presentation()

