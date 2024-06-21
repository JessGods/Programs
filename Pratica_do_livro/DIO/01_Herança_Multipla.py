class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas;

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join ([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
      

class Mamifero(Animal):
    def __init__(self, n_patas):
        self.n_patas = n_patas;

        super().__init__(n_patas);

class Cachorro(Mamifero):
    def __init__(self, n_patas):
        self.n_patas = n_patas;
       
        super().__init__(n_patas);

class Gato(Mamifero):
    pass

class Ave(Animal):
    pass

class Onitorrinco(Mamifero, Ave):
    pass

gato = Gato(4);
print(gato);