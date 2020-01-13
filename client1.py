import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =raw_input('digite o ip de conexao: ')   # server address
port = 3128  # server port
s.connect((host, port))
mensagem = raw_input("digite uma mensagem para enviar ao servidor")
s.send(mensagem)
msg = s.recv(1024)
print (msg)
s.close()



