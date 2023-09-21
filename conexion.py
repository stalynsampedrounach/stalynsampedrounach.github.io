import paho.mqtt.client as mqtt
import time
import random
def conectado(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe('stalyn64sampedro@yahoo.es/t2')#suscrito al t2

# La devolución de llamada para cuando se recibe un mensaje PUBLICAR desde el servidor.
def nuevoMensaje(client, userdata, msg):
    #los mensajes recibidos son de tipo binario
    print(msg.topic+" "+str(msg.payload))
    #envia el mensaje que se recibio
    client.publish('stalyn64sampedro@yahoo.es/t1', 'recibido:'+msg.payload.decode('utf-8'))
    mensaje=msg.payload.decode('utf-8')
    if mensaje=='ON':
        print('encendido')

    if mensaje=='OFF':
        print('apagado')

client = mqtt.Client()
client.username_pw_set('stalyn64sampedro@yahoo.es', password='1234')
client.on_connect = conectado
client.on_message = nuevoMensaje

client.connect("maqiatto.com", 1883, 60)

n=0
while 1:
    time.sleep(1)
    valor1=random.randint(1,10)
    valor2=random.randint(10,20)
    client.publish('stalyn64sampedro@yahoo.es/t1', str(n)+' ; '+str(valor1)+' ; '+str(valor2))
    n=n+1
    client.loop()
