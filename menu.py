from banner import *
from tabulate import tabulate 
from os import system
import sys
import time
import pandas as pd
import pyautogui as pg
import webbrowser as web
def menuPrincipal():
    banner()
    opciones = {'Opciones':['Introducir manalmente un numero y mensaje',
                            'Introducir un archivo "CSV"',
                            'Salir del programa'],
                'Index':[1,2,3]}
    print("°-=| Elije una opción |=-°")
    print("")
    print(tabulate(opciones, headers='keys',tablefmt='grid'))
    try:
        varDeOpcion = int(input("\n°-=| Digita una opción |=-°\n"))
    except NameError or ValueError:
        print("\n°-=| Digita una opción |=-°\n")
    try:
        if varDeOpcion == 1:
            print("ESTA OPCIÓN ES EXCLUSIVA PARA ENVIAR UN MENSAJE A UN NUMERO ESPECIFICO")
            print("DEBERÁS DIGITAR EL NUMERO CON SU CORRESPONDIENTE LADA DESPUES DE UN '_'\n")
            print("pulsa '00' para salir\n")
            try:
                numeroDeTel = int(input("INTRODUCE EL NUMERO DE TELEFONO CAN LADA (01_numero)\n"))
                if numeroDeTel == 00:
                    system("cls")
                    menuPrincipal()
            except ValueError:
                print("\n°-=| Esa no es un numero |=-°")
                print("°-=| En 3 segundos volveras |=-°\n")
                time.sleep(3)
                system("cls")
                menuPrincipal()
            mensajeAEnviar = str(input("INTRODUCE EL MENSAJE\n"))
            try:
                repeticiones = int(input("CUANTAS VECES QUIERES ENVIAR EL MENSJAE?\n"))
            except ValueError:
                print("\n°-=| Esa no es un numero |=-°")
                print("°-=| En 3 segundos volveras |=-°\n")
                time.sleep(3)
                system("cls")
                menuPrincipal()
            botManual(telefonoMAN=numeroDeTel,mensajeMAN=mensajeAEnviar,repeticionesMAN=repeticiones)
        else:
            if varDeOpcion == 2:
                print("ESTA OPCIÓN ES EXCLUSIVA PARA ENVIAR UN MENSAJES USANDO UN ARCHIVO '.csv'")
                print("EL ARCHIVO DEVERA ESTAR ESTRUCURADO DE ESTA FORMA EXACTAMENTE:\n")
                instrucciones = {'celular':['AQUÍ PONER EL NUMERO TELEFONICO CON LADA',
                                            '12_1111111111',
                                            '12_2222222222'],
                                'Mensaje':['AQUÍ PONER EL MENSAJE','AQUÍ PONER EL MENSAJE','AQUÍ PONER EL MENSAJE']}
                print(tabulate(instrucciones, headers='keys',tablefmt='grid'))
                print("PUEDES ELEVORAR UN ARCHIVO CSV EN EXEL Y GUARDARLO CON ESA EXTENCIÓN")
                print("\nEL NUMERO DE TELEFONO DEVE DE SER DE 10 DÍGITOS SIN CONTAR LA LADA Y EL '_'")
                rutaCSV = str(input("\n°-=| pega la ruta del archivo aqui |=-°\n"))
                try:
                    numRep = int(input("\n°-=| numero ve veces que se repetiran los mensajes |=-°\n"))
                except ValueError:
                    print("\n°-=| Esa no es un numero |=-°")
                    print("°-=| En 3 segundos volveras |=-°\n")
                    time.sleep(3)
                    system("cls")
                    menuPrincipal()
                botCSV(ruta=rutaCSV, repeticiones=numRep)
            else:
                if varDeOpcion == 3:
                    print("\n°-=| SALIENDO... |=-°")
                    time.sleep(3)
                    system("cls") 
                    sys.exit()
                else:
                    print("\n°-=| Esa opcion no es valida |=-°")
                    print("°-=| En 3 segundos volveras |=-°\n")
                    time.sleep(3)
                    system("cls")
                    menuPrincipal()
    except UnboundLocalError:
        print("\n°-=| Esa opcion no es valida |=-°")
        print("°-=| En 3 segundos volveras |=-°\n")
        time.sleep(3)
        system("cls")   
        menuPrincipal()

def botCSV(ruta, repeticiones):
    try:
        index = 0
        count = 0
        msm = 0
        while index < repeticiones:
            data = pd.read_csv(ruta)
            data_dict = data.to_dict('list')
            celulares = data_dict['Celular']
            mensajes = data_dict['Mensaje']
            combo = zip(celulares,mensajes)
            first = True
            for celular,mensaje in combo:
                time.sleep(8)
                web.open("https://web.whatsapp.com/send?phone="+celular+"&text="+mensaje)
                if first:
                    time.sleep(8)
                    first=False
                width,height = pg.size()
                pg.click(width/2,height/2)
                time.sleep(10)
                msm+=1
                pg.press('enter')
                print("mensaje: "+str(msm)+" ENVIADO")
                time.sleep(6)
                pg.hotkey('ctrl', 'w')
            count+=1
            index+=1
            if count == repeticiones:
                print("\n°-=| SE ENVIARON "+str(msm)+" CON EXITO |=-°")
                print("°-=| Espere 10 segundos |=-°\n")
                time.sleep(10)
                system("cls")
                menuPrincipal()
                               
    except FileNotFoundError:
        print("\n°-=| ruta no encontrada o mal escrita |=-°")
        print("°-=| Espere 3 segundos |=-°\n")
        time.sleep(3)
        system("cls")
        menuPrincipal()

def botManual(telefonoMAN,mensajeMAN,repeticionesMAN):
    index = 0
    count = 0
    msm = 0
    while index < repeticionesMAN:
        celulares = telefonoMAN
        mensajes = mensajeMAN
        first = True
        time.sleep(8)
        web.open("https://web.whatsapp.com/send?phone="+str(celulares)+"&text="+mensajes)
        if first:
            time.sleep(8)
            first=False
        width,height = pg.size()
        pg.click(width/2,height/2)
        time.sleep(10)
        msm+=1
        pg.press('enter')
        print("mensaje: "+str(msm)+" ENVIADO")
        time.sleep(6)
        pg.hotkey('ctrl', 'w')
        index+=1
        count+=1
        if count == repeticionesMAN:
            print("\n°-=| SE ENVIARON "+str(msm)+" CON EXITO |=-°")
            print("°-=| Espere 10 segundos |=-°\n")
            time.sleep(10)
            system("cls")
            menuPrincipal()

menuPrincipal()


