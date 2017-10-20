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

puteadas = ['Yo les doy todas las herramientas, y no estudian','Para que me esfuerzo tanto','Los químicos son los únicos que les va bien','La verdad chiquillos hoy no estoy muy contenta que digamos... \
    yo le dije una y una y otra vez, estudien chiquillos, y nada , yo les envio mi material, me compré un libro para que ustedes estudien, pero nisiquiera pero nisiquiera ven el material que yo les envio. ',
    'Nunca pero nunca en todas las generaciones habia hecho una prueba tan estúpida como esta. Asi que antes de que digan por el patio que la profe hizo una tremenda , piénsenlo, asi que ojo, yo no puedo \
    hacer nada, yo les envie hace que rato el material, es resposabilidad de ustedes si no estudian, ahora la metodología es que ustedes hagan la clase, no yo']
frases = ['EL LiAlH4 es un reductor PO-DE-RO-SÍ-SI-MO','El NaNH2 es una base Tremendamente fuerte','enlace sigma :handshake: fuerte , en cambio el pi:raised_hands: como que si , como que no']
comandos = '    !aiuda: Da lista de comandos \n\
            !putear: Putea \n\
            !frase: Se manda una frase\n\
            !terremoto: Predice un terremoto\n\
            !quim nombre "Nombre del compuesto": busca un químico en pubchem\n\
            !wiki "busqueda": busca en wikipedia y entrega un resumen'
            
lugares = ['Chile','Japòn','México','India','Haití','Tu poto']

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
        yield from client.send_message(message.author, comandos)
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

if __name__ == '__main__':
    client.run(mail,password)
