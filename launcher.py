import bot
import os
import requests

repositorio = 'https://raw.githubusercontent.com/mateoinc/LCBoTQ/master/'
textos = repositorio + 'textos/'
directorio = os.getcwd()

verActual = open(directorio + '/changelog.txt','r')
verVirtual = requests.get(repositorio + 'changelog.txt')

if verActual != verVirtual:
    url = textos + 'ayuda.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/ayuda.txt'
    with open(destino,'w') as file:
        file.write(archivo.content)

    url = textos + 'frases.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/frases.txt'
    with open(destino,'w') as file:
        file.write(archivo.content)

    url = textos + 'lugares.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/lugares.txt'
    with open(destino,'w') as file:
        file.write(archivo.content)

    url = textos + 'puteadas.txt'
    archivo = requests.get(url)
    destino = directorio + 'textos/puteadas.txt'
    with open(destino,'w') as file:
        file.write(archivo.content)

    url = repositorio + 'changelog.txt'
    archivo = requests.get(url)
    destino = directorio + 'changelog.txt'
    with open(destino,'w') as file:
       file.write(archivo.content)

    os.system('python3 bot.py')

elif verActual == verVirtual:
    os.system('python3 bot.py')
