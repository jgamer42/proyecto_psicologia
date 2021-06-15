import os
from dotenv import load_dotenv
load_dotenv() 

def escribir(modelo):
    base = os.getenv("PROJECT_PATH")
    file = open(base+f"/src/corpus/{modelo['medio']}/txt/{modelo['titulo']}.txt", 'w+')
    file.write(f"titulo: {modelo['titulo']}\n")
    file.write(f"Link: {modelo['link']}\n")
    file.write(f"fecha: {modelo['fecha']}\n")
    file.write(f"contenido: {modelo['contenido']}\n")
    file.write(f"aux: {modelo['aux']}\n")
    file.write(f"actores: {modelo['actores']}\n")
    file.write(f"palabras_clave: {modelo['palabras_clave']}")
    file.close()