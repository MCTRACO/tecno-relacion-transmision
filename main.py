
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

# Create the menu
menu = ConsoleMenu("Elige el tipo de transmision",exit_option_text="Salir")

def calculos(tipo:str):
    
    if tipo == "f" :#ruedas friccion
        t = "rueda de friccion"
        d= "de la"
        i = "diametro"
    if tipo == "e": #engranajes
        t = "engranaje"
        d= "del"
        i = "nº dientes"
    if tipo == "p": #poleas
        t = "polea"
        d= "de la"
        i = "diametro"
        
    _1 = float(input(f"Cual es el {i} {d} {t} motriz: "))
    _2 = float(input(f"Cual es el {i} {d} {t} conducid@: "))
    print(f"La relacion de transmision es de {_2/_1}, presiona cualquier tecla para volver al menu")
    input()
    menu.show()

f = FunctionItem("Ruedas de friccion", calculos, ["f"])
e = FunctionItem("Engranajes", calculos, ["e"])
p = FunctionItem("Poleas", calculos, ["p"])

for i in [f,e,p]:
    menu.append_item(i)

menu.show()
