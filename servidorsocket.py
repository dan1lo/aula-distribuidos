import socket 
host = '' 
port = 5555
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria o socket
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reseta o socket se tiver ocupad
serv_socket.bind(addr) #define o ip e o a porta 
serv_socket.listen(2) #limite de conexoes
print 'aguardando conexao' 
con, cliente = serv_socket.accept() # esperando para ser conectado
print 'cliente conectado' 
recebe = ""
while (recebe != 'sair') :
	print "aguardando mensagem" 
	recebe = con.recv(1024) # recebendo a mensagem
	con.send("chegou a mensagem no servidor")
	print "mensagem recebida: "+ recebe 
serv_socket.close() # fechando o socket