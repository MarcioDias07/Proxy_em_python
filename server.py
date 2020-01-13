from datetime import date
from datetime import datetime

import socket
host = "10.42.0.90"
port = 3129
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
while True:
    now = datetime.now()
    data_atual = date.today()
    h = now.hour, now.minute, now.second
    connCliente, addrCliente = s.accept()
    msg = connCliente.recv(1024)
    print(addrCliente, "IP do Cliente")
    print(msg)
    ##ENVIANDO MSG COM RESPOTA AO PROXY
    connCliente.send(
        "obrigado pela mensagem: " + msg + "-> horario:" + str(now.hour) + "h:" + str(now.minute) + "m:" + str(
            now.second) + "s" + " Data: " + str(data_atual))
    # if (msg == "exit"):
    #     s.close()
    #     socket.socket.close(s)
    #     break

