#!/bin/bash

#Busca data atual
DATE_TIME=`date +"%d-%m-%Y %T"`

#Verifica se pacote já esta instalado
if [ -d "./local_lib/path" ] && [ -d "./local_lib/path-16.6.0.dist-info" ]; then
    echo -e "###########################################################\n"
    echo -e "Pacote já instalado, finalizando a execução do script\n"
    echo -e "$DATE_TIME - Pacote já instalado, finalizando a execução do script" >> installer.log
    echo -e "###########################################################"
    exit 1
else
    echo -e "###########################################################\n"
    echo -e "Pacote não instalado, realizando a instalação\n"
    echo -e "$DATE_TIME - Pacote não instalado, realizando a instalação" >> installer.log
    echo -e "-----------------------------------------------------------\n"
fi

#Busca versão do PIP
PIP_VERSION=`pip --version | awk '{print $2}'`

echo -e "Versão do Pip: $PIP_VERSION\n"
echo -e "$DATE_TIME - Versão do Pip: $PIP_VERSION" >> installer.log

#Instala pacote path
pip install path -t ./local_lib --log installer.log

if [ -d "./local_lib/path" ] && [ -d "./local_lib/path-16.6.0.dist-info" ]; then
    echo -e "-----------------------------------------------------------\n"
    echo -e "Pacote Path Instalado com Sucesso!\n"
    echo -e "$DATE_TIME - Pacote Path Instalado com Sucesso!" >> installer.log
    echo -e "-----------------------------------------------------------\n"
    echo -e "Executando Script my_program.py\n"
    echo -e "$DATE_TIME - Executando Script my_program.py" >> installer.log

    #Executa script python
    python3 ./my_program.py

    echo "###########################################################"
    exit 1
else
    echo -e "-----------------------------------------------------------\n"
    echo -e "Erro ao instalar o Pacote!\n"
    echo -e "$DATE_TIME - Erro ao instalar o Pacote!\n" >> installer.log
    echo "###########################################################"
fi