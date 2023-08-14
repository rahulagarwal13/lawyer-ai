### gpt3.5 generated code 

class LawyerBot:
    def __init__(self, name):
        self.name = name
        self.specialties = []
       
    def introduce(self):
        print(f"Hello! I am {self.name}, your lawyer bot.")
       
    def add_specialty(self, specialty):
        self.specialties.append(specialty)
        print(f"{specialty} has been added to my specialties.")
       
    def provide_legal_advice(self, user_question):
        if any(specialty in user_question for specialty in self.specialties):
            print("Here is some legal advice based on your question.")
        else:
            print("I'm sorry, I might not be well-versed in that area of law.")

# Creating instances of LawyerBot
bot1 = LawyerBot("LegalEagle")
bot2 = LawyerBot("JurisConsult")

# Introducing the lawyer bots
bot1.introduce()
bot2.introduce()

# Adding specialties to lawyer bots
bot1.add_specialty("Intellectual Property")
bot2.add_specialty("Family Law")
bot2.add_specialty("Criminal Law")

# Providing legal advice based on specialties
user_question = "Can you help with a divorce case?"
bot1.provide_legal_advice(user_question)

user_question = "I've been charged with theft. What should I do?"
bot2.provide_legal_advice(user_question)