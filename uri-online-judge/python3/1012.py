#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1012


def main():
    A, B, C = map(float, input().split(' '))

    pi = 3.14159
    TRIANGULO = (A * C) / 2
    CIRCULO = pi * C ** 2
    TRAPEZIO = ((A + B) * C) / 2
    QUADRADO = B ** 2
    RETANGULO = A * B

    print("TRIANGULO:", format(TRIANGULO, '.3f'))
    print("CIRCULO:", format(CIRCULO, '.3f'))
    print("TRAPEZIO:", format(TRAPEZIO, '.3f'))
    print("QUADRADO:", format(QUADRADO, '.3f'))
    print("RETANGULO:", format(RETANGULO, '.3f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
