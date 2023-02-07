import sys


def biblioteca(state) :
    
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
    
     
    if state not in states :
        print("Unknown state")
    else :

        argumentoEstado= states[state] #Oregon value
        
        argumentoCidade = capital_cities[argumentoEstado]
        print(argumentoCidade)
  

#linha 33 quantidade de argumentos (tamanho da string "uhauyayasg"= 1string)
if __name__ == '__main__':
    if len(sys.argv) == 2:
        biblioteca(sys.argv[1])
    

