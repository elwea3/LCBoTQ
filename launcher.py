import os
import requests

repositorio = 'https://raw.githubusercontent.com/mateoinc/LCBoTQ/master/'
textos = repositorio + 'textos/'
directorio = os.getcwd() + '/'
verActual = open(directorio + 'version.txt','r').read()
verVirtual = requests.get(repositorio + 'version.txt').content

if verActual !=  verVirtual:
    url = textos + 'ayuda.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/ayuda.txt'
    with open(destino,'w') as file:
        file.write(archivo.text)

    url = textos + 'frases.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/frases.txt'
    with open(destino,'w') as file:
        file.write(archivo.text)

    url = textos + 'lugares.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/lugares.txt'
    with open(destino,'w') as file:
        file.write(archivo.text)

    url = textos + 'puteadas.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/puteadas.txt'
    with open(destino,'w') as file:
        file.write(archivo.text)

    url = repositorio + 'changelog.txt'
    archivo = requests.get(url)
    destino = directorio + 'changelog.txt'
    with open(destino,'w') as file:
       file.write(archivo.text)

    url = repositorio + 'version.txt'
    archivo = requests.get(url)
    destino = directorio + 'version.txt'
    with open(destino,'w') as file:
       file.write(archivo.text)
       
    url = repositorio + 'bot.py'
    archivo = requests.get(url)
    destino = directorio + 'bot.py'
    with open(destino,'w') as file:
       file.write(archivo.text)
              
    os.system('python3 bot.py')

elif verActual == verVirtual:
    os.system('python3 bot.py')

