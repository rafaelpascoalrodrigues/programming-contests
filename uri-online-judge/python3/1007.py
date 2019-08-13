#!/bin/python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1007


def main():
    A, B, C, D = int(input()), int(input()), int(input()), int(input())

    DIFERENCA = (A * B) - (C * D)

    print("DIFERENCA =", DIFERENCA)


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
