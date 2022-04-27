#create class for character object

class Character:
    def _init_(self, name, gender, species, origin, status, image, number_of_episodes):
        self.name = name
        self.gender = gender
        self.origin = origin 
        self.status = status 
        self.image_url = image 
        self.number_of_episodes = number_of_episodes

#create temp method
    def show_character(self):
        print(self.name, self.gender)

