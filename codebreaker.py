import random


class Codebreaker:
    trueNumber = random.randint(1000, 9999)

    def adivinar(self, numero=None):
        if self.trueNumber == "":
            return "Number is not defined"

        if numero is None or len(numero) != 4 or "e" not in list(numero):
            return "error"

        if numero == self.trueNumber:
            return True

        resultadoX = ""
        resultado_ = ""
        arrayNumber = []

        for x in len(numero):
            if arrayNumber[numero[x]] == True:
                return "error"

            arrayNumber[numero[x]] = True

        numero = list(numero)

        for index, x in numero:
            if self.trueNumber[index] == numero[index]:
                resultadoX += "X"

            elif x in self.trueNumber:
                resultado_ = "_"

        return resultadoX + resultado_
