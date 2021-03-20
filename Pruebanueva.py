import requests
import json

url = "https://reqres.in/api/users"

def ListarUsuarios():
    while True:
        pagina = input("Que pagina de usuarios desea ver?")
        listar = "?page=" + pagina
        response = requests.get(url + listar)
        response_json = json.loads(response.text)
        if response.status_code:
            data = response_json['data']
            print(data)
        else:
            print(response.status_code)
        resp = input("¿DESEA EFECTUAR OTRA CONSULTA (S/N):?")
        if resp.upper() == 'S':
            continue
        else:
            print("FIN DEL PROGRAMA...")
            break

def ListarUsuario():
    while True:
        pagina = input("Que usuario desea ver?")
        listar = "/" + pagina
        response = requests.get(url + listar)
        response_json = json.loads(response.text)
        if response.status_code:
            data = response_json['data']
            print(data)
        else:
            print(response.status_code)
            print("Usuario no encontrado")
        resp = input("¿DESEA EFECTUAR OTRA CONSULTA (S/N):?")
        if resp.upper() == 'S':
            continue
        else:
            print("FIN DEL PROGRAMA...")
            break
            
def AddUsuario():
    while True:
        nombre = input("Ingrese un nombre:")
        job = input("Ingrese una ocupacion:")
        data = nombre + job
        response = requests.post(url, data = data )
        response_json = json.loads(response.text)
        if response.status_code:
            print(response.content)
        else:
            print(response.status_code)
        resp = input("¿DESEA AGREGAR OTRO USUARIO (S/N):?")
        if resp.upper() == 'S':
            continue
        else:
            print("FIN DEL PROGRAMA...")
            break

def UpdateUsuario():
    while True:
        pagina = input("Que usuario desea Actualizar?")
        listar = "/" + pagina
        nombre = input("Ingrese un nombre:")
        job = input("Ingrese una ocupacion:")
        data = nombre + job
        response = requests.put(url, data = data )
        response_json = json.loads(response.text)
        if response.status_code:
            print(response.content)
        else:
            print(response.status_code)
        resp = input("¿DESEA ACTUALIZAR OTRO USUARIO (S/N):?")
        if resp.upper() == 'S':
            continue
        else:
            print("FIN DEL PROGRAMA...")
            break

def DeleteUsuario():
    while True:
        pagina = input("Que usuario desea Eliminar?")
        eliminar = "/" + pagina
        response = requests.put(url + eliminar)
        response_json = json.loads(response.text)
        if response.status_code:
            print(response.content)
        else:
            print(response.status_code)
        resp = input("¿DESEA ELIMINAR OTRO USUARIO (S/N):?")
        if resp.upper() == 'S':
            continue
        else:
            print("FIN DEL PROGRAMA...")
            break

while True:
    print("Escoja una de las siguientes opciones")
    print("1-Ver paginas de usuarios")
    print("2-Ver usuario en especifico")
    print("3-Agregar usuario")
    print("4-Actualizar usuario")
    print("5-Eliminar Usuario")
    var = input("=")
    
    if var == '1':
        ListarUsuarios()
    elif var == '2':
        ListarUsuario()
    elif var == '3':
        AddUsuario()
    elif var == '4':
        UpdateUsuario()
    elif var == '5':
        DeleteUsuario()
    else:
        print("Opcion no Valida")
    resp = input("¿DESEA ESCOGER OTRA OPCION (S/N):?")
    if resp.upper() == 'S':
        continue
    else:
        print("FIN DEL PROGRAMA...")
        break

            
            
        
