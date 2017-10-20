import discord
import asyncio
import random
import pubchempy as pcp
import wikipedia

wikipedia.set_lang("es")
client = discord.Client()

with open("credenciales.txt") as file: #No incluiré la contraseña acá
    mail = file.readline()
    password = file.readline()

#Agregar al repertorio de frases no requiere editar el código    
with open("textos\frases.txt",'r') as file:
    frases = file.readlines()
with open("textos\lugares.txt",'r') as file:
    lugares = file.readlines()
with open("textos\puteadas.txt",'r') as file:
    puteadas = file.readlines()
with open("textos\ayuda.txt",'r') as file:
    ayuda = file.read()
with open("textos\cambios.txt",'r') as file:
    cambios = ""
    cambios += "Versión" + file.readline()
    for line in file:
        if line[0] == ">":
            break
        else:    
            cambios += '\n' + line
            
@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_member_join(member):
    server = member.server
    fmt = 'Bienvenido {0.mention} a {1.name}!'
    yield from client.send_message(server, fmt.format(member, server))

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user: #Para que no responda a si mismo
        return    
    elif message.content.startswith('!aiuda'):
        yield from client.send_message(message.author, ayuda)
    elif message.content.startswith('!cambios'):
        yield from client.send_message(message.author, cambios)
    elif message.content.startswith('!putear'):
        yield from client.send_message(message.channel, random.choice(puteadas))
    elif message.content.startswith('!frase'):
        yield from client.send_message(message.channel, random.choice(frases))        
    elif message.content.startswith('!terremoto'):
        yield from client.send_message(message.channel, 'Yo les digo, con los niveles de la ionósfera cualquiera día de estos habrá un terremoto grado %s en %s' % (random.randint(5,10), random.choice(lugares)))
    elif message.content.startswith('!quim nombre'):
        busqueda = pcp.get_compounds(message.content[12:],'name')
        yield from client.send_message(message.channel, "Resultados posibles" + str(busqueda))
        for i in busqueda:     
            yield from client.send_message(message.channel, 'Código %s \n Nombre IUPAC: %s \n Fórmula: %s \n Peso: %s \n Carga: %s' % (i, i.iupac_name, i.molecular_formula, i.molecular_weight, i.charge) ) 
#    elif "Tejos" or "Marisol" or "tejos" or "marisol" in message.content:
#        yield from client.send_message(message.channel, "¡Ya me andan pelando!¡Yo que les he dado de todo!")
    elif message.content.startswith('!wiki'):
        busqueda = wikipedia.search(message.content[6:])
        yield from client.send_message(message.channel, str(busqueda))
        input = yield from client.wait_for_message(timeout=15.0)
        if input in busqueda:
            yield from client.send_message(message.channel, wikipedia.summary(input))

client.run(mail,password)
