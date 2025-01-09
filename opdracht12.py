class Klant:    
    class Rekening:
        def __init__(self, iban, status, saldo=0.00):
            self._iban=iban
            self.status=status
            self.saldo=saldo
            self.limit=self.saldo + Klant.get_limit()

        def get_details(self):
            return f"Het saldo van rekening **************{self._iban[13:15]} is {self.saldo:.2f} euro"

        def geld_storten(self):
            bedrag = float (input("Hoeweel geld wil je storten?"))
            if bedrag < 0:
                print ("Ongeldig nummer")
            else:
                self.saldo += bedrag
            

        def geld_opvragen(self):
            bedrag = float (input("Hoeweel geld wil je opvragen?"))
            
            


    limit=0.00
    def __init__(self, naam, voornaam, lidstatus):
        self.naam=naam
        self.voornaam=voornaam
        self.lidstatus=lidstatus
        self.rekeningen = []

    def toevoegen_rekening (self, iban, status):
        nieuw_rekening=self.Rekening(iban, status)
        self.rekening.append(nieuw_rekening)

    def get_limit(self):
        if self.lidstatus=="GOLD":
                self.limit+=5000.00
        elif self.lidstatus=="SILVER":
                self.limit+=2500.00
        else:
                self.limit+=0.00      
   

    
klant1=Klant('John', 'Johnson', 'GOLD')
klant2=Klant('Addy', 'Addyson', 'SILVER')
klant3=Klant('Bob', 'Button', 'BRONZE')





