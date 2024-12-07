class Animal:
    def make_sound(self):
        return f"{self.__class__.__name__} está";

class Gato(Animal):
    
    def meow(self):
        makeSound = super().make_sound()
        return f"{makeSound} miando!";

class Cachorro(Animal):
    
    def latir(self):
        makeSound = super().make_sound()
        return f"{makeSound} latindo!";

if __name__ == "__main__":
    cat: Gato = Gato()
    print(cat.meow())
    
    dog: Cachorro = Cachorro()
    print(dog.latir())
