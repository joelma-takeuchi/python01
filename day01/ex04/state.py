import sys
#Você obtém os mesmos dicionários do exercício anterior. Você tem que copiá-los
def biblioteca() :
    
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    
    if verifica(capital_cities) == True:
        cidade = trazendoEstado(capital_cities, sys.argv[1])
        estado = procurandoUF(states, cidade)
        print(estado)
    else :
        print("Unknown capital city")

def procurandoUF(capital_cities, cidade): #Salem value
            for k,v in capital_cities.items():
                if cidade == v :
                    return k
     
        
        
def trazendoEstado(states,estado):
            for k,v in states.items():
                if estado == v :
                    return k
            
def verifica(capital_cities):
    valid = False
    
    if len(sys.argv) != 2:
        sys.exit()
    for k, v in capital_cities.items():
        if(sys.argv[1]) == v:
            valid = True
    return(valid)



if __name__ == '__main__':
  biblioteca()

#Crie um programa que usa a capital como argumento e exibe o
#estado desta vez. O restante dos comportamentos do seu programa deve permanecer o mesmo que no
#exercício anterior