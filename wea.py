
from shutil import which


print("Bienvendio a la wea de mierda")
print("1.- Registrar trabajador")
print("2.- Listar a todos los trabajadores")
print("3.- Imprimir planilla de sueldos")
print("4.- Salir")
trabajadores=[]
CARGOS= ['ceo','desarrollador','analista de datos']


def registrar_trabajador(trabajadores):
    nombre=input("Ingrese nombre ")
    cargo=input("Ingrese cargo ")
    while cargo not in CARGOS:
        print ("Ingrese cargo valido")
        cargo=int("Ingrese cargo ")
    sueldobruto=int(input("Ingrese sueldo "))
##calcular descueto
    dscoSalud= sueldobruto*0.07
    dscoAFP=sueldobruto*0.12
    liquidopagar= sueldobruto-dscoSalud-dscoAFP

    trabajadores.append({
        'Nombre':nombre,
        'Cargo': cargo,
        'sueldobruto':sueldobruto,
        'dscoSalud': dscoSalud,
        'dscoAFP': dscoAFP,
        'liquidopagar':liquidopagar
        
    })

def listar_trabajadores(trabajadores):
    print ("Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)

def imprimir_plantilla():
    cargoSeleccionado=input("Ingrese cargo")
    if cargoSeleccionado=="":
        trabajadores_a_imprimir=trabajadores
        nombreArchivo='planilla_todos.txt'
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir=[]
        for trabajador in trabajadores:
            if trabajador['cargo']==cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo=f'planilla_{cargoSeleccionado}.txt '
    else:
        print("Cargo no valido")
        return

    with open(nombreArchivo,'w') as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre y apellido: {trabajador['Nombre']} \n")
            archivo.write(f"Cargo: {trabajador['Cargo']} \n")
            archivo.write(f"Sueldo bruto: {trabajador['sueldobruto']} \n")
            archivo.write(f"Descuento de salud: {trabajador['dscoSalud']} \n")
            archivo.write(f"Descuento AFP: {trabajador['dscoAFP']} \n")
            archivo.write(f"Liquido a pagar: {trabajador['liquidopagar']} \n")

while True:
    opc=int(input("Ingrese opcion "))
    
    if opc==1:
        registrar_trabajador(trabajadores)
    elif opc==2:
        listar_trabajadores(trabajadores)
    elif opc==3:
        imprimir_plantilla()
    elif opc==4:
        print("SALIENDO")
        break
    else:
        print ("Ingrese opcion correcta ")
        
        

