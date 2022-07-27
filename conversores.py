from operator import truediv
from pickle import TRUE


continua = True
n = 0

def operacoes(numero):
    match numero:
        case 1:
            ncovertido = int(input('Digite quantos quilômetros serão convertidos: ')) 
            print(ncovertido / 1.609, ' mi')
        case 2:
            nconvertido = int(input('Digite quantos quilômetros serão convertidos: '))
            print(nconvertido * 1000, 'm')
        case 3:
            ncovertido = int(input('Digite quantos quilômetros serão convertidos: '))
            print(ncovertido * 100000, ' cm')
        case 4:
            nconvertido = int(input('Digite quantos quilômetros serão convertidos: '))
            print(nconvertido * 1000000, ' mm')
        case 5:
            ncovertido = int(input('Digite quantos metros  serão convertidos: '))
            print(ncovertido / 1000, ' Km')
        case 6:
            ncovertido = int(input('Digite quantos metros  serão convertidos: '))
            print(ncovertido * 100, ' cm')
        case 7:
            nconvertido = int(input('Digite quantos metros  serão convertidos: '))
            print(nconvertido * 1000, ' mm')
        case 8:
            nconvertido = int(input('Digite quantos centímetros  serão convertidos: '))
            print(nconvertido / 100000,' km')
        case 9:
            nconvertido = int(input('Digite quantos centímetros  serão convertidos: '))
            print(nconvertido / 100,' m')
        case 10:
            nconvertido = int(input('Digite quantos centímetros  serão convertidos: '))
            print(nconvertido * 10,' mm')
        case 11:
            nconvertido = int(input('Digite quantos milímetros  serão convertidos: '))
            print(nconvertido / 1000000,' Km')
        case 12:
            nconvertido = int(input('Digite quantos milímetros  serão convertidos: '))
            print(nconvertido / 1000,' m')
        case 13:
            nconvertido = int(input('Digite quantos milímetros  serão convertidos: '))
            print(nconvertido / 10,' cm')
        case 14:
            nconvertido = int(input('Digite quantas milhas  serão convertidos: '))
            print(nconvertido / 1.609,' km')
            


def opcoes():
    print('1.Quilometro para milhas')
    print('2.Quilometro para metros')
    print('3.Quilometro para centimetros')
    print('4.Quilometro para milimetros')
    print('5.Metros para quilometros')
    print('6.Metros para centimetros')
    print('7.Metros para milimetros')
    print('8.centimetros para quilometros')
    print('9.centimetros para metros')
    print('10.centimetros para milimetros')
    print('11.milimetros para quilometros')
    print('12.milimetros para metros')
    print('13.milimetros para centimetros')
    print('14.milhas para quilometros')
    n = int(input('Para escolher uma conversão digite o numero: '))
    operacoes(n)

def continuar():
    con = input('Você quer continuar usando o conversor? S/N ')
    if con == 'S':
        continua = True
    elif con == 'N':
        continua = False
    else:
        print('Letra digitada errado, saindo do conversor...')
        continua = False
       


while(continua):
    opcoes()
    continuar()

        
