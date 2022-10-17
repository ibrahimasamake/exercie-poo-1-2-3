class Put:
    __name = ""
    __animalType = ""
    __age = 0

    def __init__(self ):
        name = input("Entre le nom  : ")
        typeanimal = input("Entre le type d'animal : ")
        age = input("Entre l'age  : ")
        self.__name = name
        self.__age =age
        self.__animalType = typeanimal


    def Affcher(self):
        print(f"Nom  : {self.__name}")
        print(f"Type Animal  : {self.__animalType}")
        print(f"Age  : {self.__age}")



aminal1 = Put()

aminal1.Affcher()

















