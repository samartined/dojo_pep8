import random

true_number = "".join(random.sample("0123456789", 4))


class Codebreaker:
    def adivinar(self, numero=true_number):
        if true_number == "":
            return "Number is not defined"

        if numero is None or len(numero) != 4:
            return "error"

        if numero == true_number:
            return True

        resultado_x = ""
        resultado_ = ""
        array_number = [False] * 10

        for index, x in enumerate(true_number):
            array_number[int(x)] = True

        numero = list(numero)
        true_number_list = list(true_number)

        for index, x in enumerate(numero):
            if x in true_number_list:
                if true_number_list[index] == x:
                    resultado_x += "X"
                    true_number_list[index] = None
                else:
                    resultado_ += "_"
                    true_number_list[
                        true_number_list.index(x)
                    ] = None  # Para evitar que se repita el mismo numero

        return resultado_x + resultado_
