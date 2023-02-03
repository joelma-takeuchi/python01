if __name__ == '__main__':
  
    arquivo = open("numbers.txt")
    linha = arquivo.readlines()
    print(linha) 

    letters= linha[0].replace(',','\n')
    print(letters)
    
    





