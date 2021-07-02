################################################################
#                                                              #
#                        [ Creditos ]                          #
#                                                              #
################################################################
#                                                              #
#                 Codigo hecho por xNetting                    #
#                                                              #
#                Dev: xNetting / Grupo: Panic Squad            #
#                                                              #
################################################################

# Coded By xNetting
# PanicSquad

from itertools import product
import string
import os
import sys

os.system('color 1')
print('''

    ██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
    ██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝

                Dev: xNetting // Grupo: Panic Squad
                                                                                                                                                
    ''')

def wordlistgen():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │    Ingrese el minimo de letras de las contraseñas   │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    min_let = int(input('''
    
    root@xnetting: ~# '''))

    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │    Ingrese el maximo de letras de las contraseñas   │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    
    ''')

    max_let = int(input('''
    
    root@xnetting: ~# '''))

    contador = 0

    caracter = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

    archivo = open('wordlist.txt', 'w')

    for i in range(min_let, max_let+1):
        for j in product(caracter, repeat=i):
            let = ''.join(j) # le asigno let por letra mas corto, no porque me confundi entre JS, espero lo entiendas y no seas tan anormal XD
            archivo.write(let)
            archivo.write('\n')
            contador += 1
    print('WordList ha sido creado, genero {} contraseñas'.format(contador)) 

def main():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga la herramienta que quiere usar              │                      
    │                                                     │
    │        1 - Generar WordLists                        │
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    
    ''')

    opciones = input('''
    
    root@xnetting: ~# ''')

    if opciones == '1':
        wordlistgen()
    else:
        sys.exit()

main()
