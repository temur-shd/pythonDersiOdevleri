"""Ters Lehçe Notasyonu ile hesap makinesi tasarlanacaktır"""

import sys


def main():
    liste = [23, 19, 7, 8, "+", 3, "-", "/", "s", "+", "s", "x"]
    print(f'Sonuc:{rpn_calculator(liste)}')  # Fonksiyon çağrısı


def rpn_calculator(element_list):
    """Verilen listedeki elemanları ters lehce notasyonu kullanarak yığın ile hesaplar"""
    # Elemanların saklanacağı liste(yığın)
    stack = []
    # Operatörler listesi
    operators = ["+", "-", "*", "/"]
    # Operandların tutulacağı değişkenler
    first_element = 0
    second_element = 0

    for element in element_list:
        if element == "x":
            print("Program sonlandi..")
            return stack[-1]
            sys.exit(-1)

        if element == "s":
            print(f'Yığın:>{stack}')
            # else bloğuna girmeden adımı atla
            continue

            # Listedeki eleman bir operatör değilse ?
        if element not in operators:
            # Yığına ekle
            stack.append(element)
            print(stack)

        # Listedeki eleman bir sayı ise ?
        else:
            # Elemanları yığından çıkar
            first_element = stack.pop()
            second_element = stack.pop()

            # Listede sıradaki işleme göre operandları uygun operasyona sok ve sonucu yığına ekle
            if element == "+":
                stack.append(first_element + second_element)
            elif element == "-":
                stack.append(first_element - second_element)
            elif element == "*":
                stack.append(first_element * second_element)
            else:
                stack.append(first_element / second_element)

    # Hesaplama sonucunu döndür
    return stack[-1]


main()
