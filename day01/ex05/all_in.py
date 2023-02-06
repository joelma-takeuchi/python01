import sys

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

      
    if recebeArgumentos(capital_cities) == True:
        cidade = trazendoEstado(capital_cities, sys.argv[1]).split()
        estado = procurandoUF(states, cidade)
        for estado in capital_cities:
            if ',' in capital_cities or ' ' in capital_cities or "." in capital_cities :
                print(estado[:-1])
            else:
                print(estado)
    else:
        print("Unknown capital city")

def procurandoUF(capital_cities, cidade): #Salem value
            for k,v in capital_cities.items():
                if cidade == v :
                    return k
     
        
        
def trazendoEstado(states,estado):
            for k,v in states.items():
                if estado == v :
                    return k

            
def recebeArgumentos(capital_cities):
    valid = False
   
    if len(sys.argv) != 2:
        sys.exit()
    for k, v in capital_cities.items():
        if(sys.argv[1]) == v:
            valid = True
    return(valid)



if __name__ == '__main__':
  biblioteca()      
    


#O programa deve receber como argumento uma string contendo tantas expressões quanto
#procuramos, separados por uma vírgula.
#• Para cada expressão nesta string, o programa deve detectar se é uma maiúscula, um estado
#ou nenhum deles.
#• O programa não deve diferenciar maiúsculas de minúsculas. Não deve ocupar vários espaços em con-
#sideração também.
#• Se não houver parâmetro ou muitos parâmetros, o programa não exibe
#qualquer coisa.
#• Quando há duas vírgulas sucessivas na string, o programa não exibe
#qualquer coisa.
#• O programa deve exibir os resultados separados por um retorno de carro e usar estritamente
#o seguinte formato:
