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

    
    
    lst = recebeArgumentos()
   
    for i in range (len(lst)) :

        line1 = lst[i].title()
        line2 = " ".join(line1.split())

        b = procurandoCity(states, capital_cities, line2)
        if not b :
            b = procurandoEstado (states, capital_cities, line2)
        if not b :
            if not lst[i] == "" : # para todo espeaço que não for null, deve imprimir a msg. "entende que é null"
                print(lst[i] + " is neither a capital city nor a state ")

    

def procurandoCity(states, capital_cities, city): #Salem value
    for k,v in capital_cities.items():
        if str(city) == str(v) :
            for k2, v2 in states.items() :
                if k == v2 :
                    print( v + " is the capital of " + k2)
                    return True
    return False
      
def procurandoEstado(states, capital_cities, state): #devolve K
    for k,v in states.items():
        if state == k :
            for k2, v2 in capital_cities.items() :
                if k2 == v :
                    print(v2 + " is the capital of " + k)
                    return True
    return False  
            
                  

            
def recebeArgumentos():
    if len(sys.argv) != 2:
        sys.exit() 
    lst = sys.argv[1].split(",")
    for i in range (len(lst)) :
        lst[i] = lst[i].strip()
  #  for k, v in capital_cities.items():
  #      if(sys.argv[1]) == v:
  #          valid = True
    return(lst)



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
