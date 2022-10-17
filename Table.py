class Table:
    __prix_fabrication = ""
    __nbTable = 0


    def __init__(self,reference,matiere_table,poid,hauteur,longeur,largeur,prix_vente,prix_fabrication,nb_table_en_stock):
        self.reference = reference
        self.matiere_table=matiere_table
        self.poid = poid
        self.hauteur = hauteur
        self.longeur = longeur
        self.largeur = largeur
        self.prix_vente = prix_vente
        self.__prix_fabrication = prix_fabrication
        self.__nbTable = nb_table_en_stock

    def setPrixFabrication(self,prixFab):
         self.__prix_fabrication = prixFab


    def  getPrix_fabricatione(self):
        return self.__prix_fabrication

    def getNbTable(self):
         return self.__prix_fabrication

    def setNbTable(self,prix):
         self.__prix_fabrication = prix


    def Affiche(self):
        print(f" References: {self.reference}")
        print(f" Matiere de la table: {self.matiere_table}")
        print(f"La longueur : {self.longeur}")
        print(f"La largeur : {self.largeur}")
        print(f" Hauteur : {self.hauteur} cm")
        print(f" Poids  : {self.poid}")
        print(f"Prix de vente : {self.prix_vente} f")
    def calculgaint(self):
            gain = self.prix_vente - self.__prix_fabrication
            return  print(f"Gain  : {gain} f")

table1 = Table("R1","Bois","5 kg",5 ,"3 m","2 m",100000,75000,10)

table1.setPrixFabrication(50000)
table1.Affiche()

table1.calculgaint()

































