class Personne :

    def __init__(self,nom:str,prenom:str,cin:str):
        self.nom = nom
        self.prenom = prenom
        self.cin = cin


    def ToString(self):
         return print(f"nom : {self.nom} , prenom : {self.prenom} cin: {self.cin}")


class Vaccine(Personne) :

        def __init__(self, nom,prenom,cin,codeVaccination:int,nomVaccin :str):
            super().__init__(nom,prenom,cin)
            self.__code = codeVaccination
            self.__nonVaccin = nomVaccin

        def setCode(self, code):
            self.__code = code

        def getCode(self):
            return self.__code

        def getNomVaccin(self):
            return self.__nonVaccin

        def setNonVaccin(self, nom):
            self.__nonVaccin = nom

        def ToString(self):
            super().ToString()
            print(f"Code : {self.__code}")
            print(f"Nom Vaccin : {self.__nonVaccin}")

class Vaccin(Personne):
    def __init__(self,nom,prenom,age, code,nomVaccin,dure):
        super().__init__(nom,prenom,age)
        self.code = code
        self.nomVaccin = nomVaccin
        self.dure = dure

    def ToString(self):
        super().ToString()
        print(f"Code : {self.code}")
        print(f"nom : {self.nom}")
        print(f"dure : {self.dure} Heure")

personne = Personne("Samake","Ibrahima",23)

personne.ToString()

vaccine = Vaccine("SALI","TRAore","AAAA",23,"letanol")

vaccine.ToString()

vacin1 = Vaccin("samake","ibra",28,33,"Paracetamol",2)
vacin1.ToString()