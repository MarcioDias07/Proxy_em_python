from socket import *

from datetime import date
from datetime import datetime

import socket
#from socket import *

host = '127.0.0.1'
port = 3128
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
bloq = ["facebook.com","youtube.com","xvideos.com"]
a=[]

def katri(x):
    	
	ipBlock=gethostbyname(x)
	return ipBlock


for x in bloq:
	a.append(katri(x))



while True:
	now = datetime.now()
	data_atual = date.today()
	h = now.hour, now.minute, now.second
	def verIP(msg):
	    	for r in a:
		 	if(str(msg)==str(r)):
				#print("i1")
				return True
			else:
				#print("e1")
				return False


	def verDominio(msg):
		for r in bloq:
		    if(str(msg)==str(r)):
				#print("i2")
				return True
		else:
				#Sprint("e2")
				return False

	connClient, addrClient = s.accept()
	msg = connClient.recv(1024)
	op=addrClient

	if (msg == 'exit'):
		s.close()
		socket.socket.close(s)
		break
	if( verIP(msg) or verDominio(msg) ):
    		print("ih mermao ta bloqueado");
		arquivo = open('bloqueios.txt', 'a')
		arquivo.write  ( "Bloqueado: "+msg +","+ " Ip  e porta do cliente: "+str(addrClient) +"-> horario:" + str(now.hour) + "h:" + str(now.minute) + "m:" + str(now.second) + "s" + " Data: " + str(data_atual)+'\n')
		arquivo.close()
		msg='exit'
		if (msg == 'exit'):
			s.close()
			socket.socket.close(s)
			break
		
		
	else:
		serv= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serv.connect(('10.42.0.90', 3129))
		serv.send(msg)
		msg1 = serv.recv(1024)
		##abrindo e escrevendo em um arquivo de texto
		arquivo = open('log.txt', 'a')
		arquivo.write(msg1+'\n')
		arquivo.close()
		### Pegar a resposta e retornar para o cliente
		connClient.send(msg1)



