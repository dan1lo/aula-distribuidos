import socket 
ip = raw_input('digite o ip de conexao: ') 
port = 5555
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #prepara a conecao
client_socket.connect(addr) #conecta ao ip e endereco
mensagem = ''
while mensagem != 'sair' :
	mensagem = raw_input("digite uma mensagem para enviar ao servidor") 
	client_socket.send(mensagem) #manda a mensage
	print 'mensagem enviada' 
	recebida=client_socket.recv(1024)
	print recebida
client_socket.close() # fecha a conecao