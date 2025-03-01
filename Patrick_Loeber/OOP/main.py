# %%
from pathlib import Path

print(Path.cwd())

class Dog:

    AGE = 1
    SPEED = 25

    def __init__(self, name: str, race: str, fur_clean: bool = False):
        self.name = self.check_name_race(name)
        self.race = self.check_name_race(race)
        self.fur_clean = fur_clean

    def check_name_race(self, word):
        if not isinstance(word, str):
            print("Error: Name must be a string.")
            return None
        
        if any(i.isdigit() for i in word):
            print("Error: Name contains digit.")
            return None
        
        return word.title()
    
    def clean(self):
        if self.fur_clean:
            print("Already clean fur.")
            return None
        
        self.fur_clean = True
        print(f"{self.name}'s fur is now cleaned.")
        return None
        


    def __str__(self):
        return f"Name: {self.name}, Race: {self.race}"


if __name__ == "__main__":

    dog1 = Dog("Pepe", "Maltipoo")
    dog2 = Dog("CURLY", "Mischling", fur_clean=True)



# %%
