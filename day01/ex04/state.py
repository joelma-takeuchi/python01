import sys
#Você obtém os mesmos dicionários do exercício anterior. Você tem que copiá-los
def biblioteca(cidade) :
    
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
    #sigla key capital_cities
    sigla = procurandoUF(capital_cities,cidade)
    #sigla será value no trazendo estado
    estadoEncontrado= trazendoEstado(sigla)

def procurandoUF(capital_cities, cidade): #Salem value
        if cidade in capital_cities :
            for k,v in capital_cities.items():
                if cidade == v :
                    return k
        else :
             print("Unknown capital city")
             sys.exit(1)
        
        
def trazendoEstado(states,estado):
        if estado in states.items() :
            for k,v in states:
                if estado == v :
                    return k
        else :
             print("Unknown capital city")
             sys.exit(1)        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        biblioteca(sys.argv[1])
print(estadoEncontrado)

#Crie um programa que usa a capital como argumento e exibe o
#estado desta vez. O restante dos comportamentos do seu programa deve permanecer o mesmo que no
#exercício anterior