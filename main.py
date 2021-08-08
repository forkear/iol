#! /usr/bin/python
# -*- encoding: utf-8 -*-

from models.iol import Iol
import config 
import os


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def print_menu():
    
    menu = f"\
        \n---------------------------------------------------------\
        \n OPCIONES\n \
        \n\t t - ver token\
        \n\t e - estado de la cuenta\
        \n\t q - salir\n\
        \n---------------------------------------------------------\
        \n\
    "
    print(menu)



def estado_cuentas(iol):
    cuentas = iol.estadocuentas()

    print("CUENTAS: ")
    for cuenta in cuentas:
        print("\n---------------------------------------------------------+")
        print(f" Tipo: \t\t\t {cuenta.tipo}\n Moneda: \t\t {cuenta.moneda}\n Estado: \t\t {cuenta.estado}\n Saldo: \t\t {cuenta.saldo}\n Titulos valorizados: \t {cuenta.titulosValorizados}")
        print(" Saldos: ")
        for saldo in cuenta.saldos:
            print(f"\t liquidacion: {saldo.liquidacion[:7]} \t {saldo.saldo}")
        print(f"\n TOTAL: {cuenta.total}")
        print("---------------------------------------------------------+")
        
    

def ver_token(iol):
    print(f"{iol.token}")


def main():

    
    try:
        iol = Iol(config.username, config.password)
    except Exception as e:
        print(f"{e}\n")
        exit(1)

    acciones = {
        't': lambda iol: ver_token(iol),
        'e': lambda iol: estado_cuentas(iol),
    }

    opcion = None

    while(opcion!='q'):

        print_menu()

        opcion = input('ingrese una opcion: ')

        try:
            
            clear()
            acciones[opcion](iol)

        except KeyError:
            pass 

        


if __name__ == "__main__":
    main()