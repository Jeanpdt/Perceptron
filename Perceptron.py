# verificar quais entradas o algoritimo deve possuir.
class Perceptron:
    def __init__(self, erroDesejado, taxaAprendizagem):
        self._w1 = 0
        self._w2 = 0
        self._wb = 0
        self._bias = 1
        self._erroDesejado = erroDesejado
        self._taxaAprendizagem = taxaAprendizagem

    # qual é a entrada da base treino ?
    def treina(self, baseTreino):
        continua = True
        while(continua):
            # oque é o erro inter ?
            erroIter = 0 
            # porque é feito um loop por toda a base de treino ?
            for i in range(0,len(baseTreino)):
                # por que é feito o ajuste de pesos ?
                # po que é incremento o erroIter ?
                erroIter+= abs(self.ajustaPesos(baseTreino[i]))
            # qual é o motivo de existir o erro médio ?
            # e por que ele é realizado dessa maneira ?
            erroMedio = erroIter / len(baseTreino)

            print("Erro medio: ",erroMedio,len(baseTreino))
            print("W1: ",self._w1," W2: ",self._w2, " Wb: ",self._wb)
            if(erroMedio <= self._erroDesejado):
                continua = False


    # oque é a subBaseTreino
    def ajustaPesos(self, subBaseTreino):
        # o que é o err ?
        # oque é a subBaseTreino[2], oque deve existir lá dentro ?
        # por que o err é subBaseTreino[2] -  a avaliação da subbase treino ?
        err = subBaseTreino[2] - self.avalia(subBaseTreino)

        # por que se o erro for 0 é retornado 0 ?
        if(err == 0):
            return 0

        # oque fazem essas três linhas abaixo ?
        self._w1 = self._w1 + self._taxaAprendizagem * err * subBaseTreino[0]
        self._w2 = self._w2 + self._taxaAprendizagem * err * subBaseTreino[1]
        self._wb = self._wb + self._taxaAprendizagem * err * self._bias
        
        return err


    def avalia(self, entrada):
        val = entrada[0] * self._w1 + entrada[1] * self._w2 + self._bias * self._wb
        if(val <= 0):
            return 0
        else:
            return 1