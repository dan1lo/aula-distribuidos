from threading import Thread
import time
#este codigo foi adaptado da internet

def corrida(velocidade,nome):
    distancia = 0
    while distancia <= 20:
        print("O corredor :",nome,distancia)
        distancia += velocidade
        time.sleep(0.5)

carredor1 = Thread(target=corrida,args=[1.1,"Hugo"])
carredor2 = Thread(target=corrida,args=[1.4,"Felipe"])
carredor3 = Thread(target=corrida,args=[1.9,"Danilo"])


carredor1.start()
carredor2.start()
carredor3.start()