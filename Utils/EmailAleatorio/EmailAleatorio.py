from random import *

class Email_Aleatorio:

    def Radom(self):

        random.seed()  # inicia a semente dos número pseudo randômicos
        random.randrange(100, 1500, 100)  # pares entre 0 e 9
        random.choice('abcdefghij')  # seleciona um dos elementos aleatoriamente
        items = [1000,1001,1002,1003,0114,1005,1006,1007,1008,1009,1010]
        random.shuffle(items)  # embaralha os itens aleatoriamente