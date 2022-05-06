import psycopg2
import json
import requests

# Se conecta a una bd existente
connection = psycopg2.connect(user="postgres", password="postgres", host="localhost", port="5432", database="TareaPython1")

# Crea cursor para llevar a cabo database operations
cursor = connection.cursor()

#tomamos el codigo del api 
def get(name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{name}/")
    return response.json()

#toma y concatena las propiedades
def get_concat(data): #to_string
    lista = []
    for dato in data:
        if dato == 'geo':
            dato= get_concat(data[dato])
            lista.append(dato)
        else:
            lista.append(data[dato])
    
    return ','.join(lista)

#toma y concatena las propiedades
def data_fun(json, script):
    print
    for dta in json: 
        data = []
        for v in dta:
            if v == 'address' or v == 'company':
                d = get_concat(dta[v])
            else:
                d = dta[v]
            data.append(d)
        
        cursor.execute(script, tuple(data))
    connection.commit()
    
# Inserta datos a la base de datos

Tabla_photos = """INSERT INTO photos VALUES (%s, %s, %s, %s, %s);"""
                  
Tabla_users = """INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
                                   
Tabla_comments = """INSERT INTO comments VALUES (%s, %s, %s, %s, %s);"""
                                      
Tabla_albums = """INSERT INTO albums VALUES (%s, %s, %s);"""
                  
Tabla_todos = """INSERT INTO todos VALUES (%s, %s, %s, %s);"""                  
                  
Tabla_posts = """INSERT INTO posts VALUES (%s, %s, %s, %s);"""
                                  
tables = {'Exito Tabla_photos': Tabla_photos,
          'Exito Tabla_albums': Tabla_albums, 
          'Exito Tabla_comments': Tabla_comments, 
          'Exito Tabla_posts': Tabla_posts, 
          'Exito Tabla_users': Tabla_users
         }

for x in tables:
    print(x)
    api = get(x) 
    data_fun(api, tables[x])
    
cursor.execute("select*from photos")
cursor.execute("select*from comments")
cursor.execute("select*from todos")
cursor.execute("select*from posts")
myresult = cursor.fetchall()

for x in myresult:
    print(x)         
    
