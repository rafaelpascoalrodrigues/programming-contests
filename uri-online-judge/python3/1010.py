#!/bin/python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1010


def main():
#   NUMBER, HOURS, PER_HOUR = int(input()), int(input()), float(input())
    _, Q1, P1 = map(float, input().split(' '))
    _, Q2, P2 = map(float, input().split(' '))

    VALUE  = 0
    VALUE += Q1 * P1
    VALUE += Q2 * P2

    print("VALOR A PAGAR: R$", format(VALUE, '.2f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
