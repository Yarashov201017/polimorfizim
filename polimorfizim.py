class Avto:
    def info(self):
        print("Avto mobillar")
class Tesla(Avto):
    def info(self):
        print("Elektr mashinalar")
class Malibu(Avto):
    def info(self):
        print("Bezinda yuradigan mashinalar ")
        
        
        
tesla1=Tesla()
malibu=Malibu()
tesla1.info()
malibu.info()
                    # Bundadan ham sodda usuli  pastda
avtolar=[Tesla(),Malibu()]
for avto in avtolar:
    avto.info()